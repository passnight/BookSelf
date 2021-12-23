import re
from flask import Flask, request
from flask_cors import cross_origin, CORS
import json
import pymysql

app = Flask(__name__, static_folder="http", static_url_path="/pages")
CORS(app, supports_credentials=True)

conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    passwd="123456",
    port=3306,
    db="database_course_project",
    charset="utf8",
)
cursor = conn.cursor()


class Response:
    def __init__(self, code=200, data={}):
        self.code = code
        self.data = data

    def toJson(self):
        return json.dumps({"code": self.code, "data": self.data}, ensure_ascii=False)


class UserController:
    @app.route("/user/login", methods=["GET"])
    @cross_origin(supports_credentials=True)
    def login():
        cursor.execute(
            f"select id from user where username='{request.args['username']}' and password='{request.args['password']}'"
        )
        result = cursor.fetchone()
        if result == None:
            return Response(code=400, data={"msg": "用户名或密码错误"}).toJson()
        else:
            return Response(
                code=200, data={"msg": "登录成功", "user_id": result[0]}
            ).toJson()

    @app.route("/user/register", methods=["GET"])
    def register():
        cursor.execute(
            f"select * from user where username='{request.args['username']}'"
        )
        result = cursor.fetchone()
        if result != None:
            return Response(code=400, data={"msg": "用户已存在"}).toJson()
        cursor.execute(
            f"insert into user(username, password) values('{request.args['username']}', '{request.args['password']}')"
        )
        conn.commit()
        return Response(code=200, data={"msg": "注册成功"}).toJson()


class ShoppingBasketController:
    @app.route("/shopping_basket/add", methods=["GET"])
    def addShopingBasket():
        cursor.execute(F"select * from check_out_list where `user_id`='{request.args['user_id']}' and `status`='waiting'")
        result = cursor.fetchone()
        if result != None:
            return Response(code=400, data={"msg": "购物车已存在"}).toJson()
        cursor.execute(F"INSERT INTO `check_out_list` (`credit_card`, `status`, `user_id`) VALUES ('{request.args['credit_card']}', 'waiting', '{request.args['user_id']}');")
        conn.commit()
        return Response(code=200, data={"msg": "创建购物车成功"}).toJson()


    @app.route("/shopping_basket/clear", methods=["GET"])
    def delete():
        cursor.execute(F"SELECT `id` FROM `check_out_list` WHERE `user_id` = {request.args['user_id']} AND `status`='waiting';")
        result = cursor.fetchone()
        if result == None:
            return Response(code=400, data={"msg": "购物车不存在"}).toJson()
        cursor.execute(F"DELETE FROM `shopping_item` WHERE `check_out_list_id` = {result[0]}")
        conn.commit()
        conn.commit()
        return Response(code=200, data={"msg": "清空购物车成功"}).toJson()

    @app.route("/shopping_basket/get", methods=["GET"])
    def getShoppingBasket():
        cursor.execute(F"SELECT C.id,S.id,S.book_isbn,S.quantities,C.credit_card FROM `check_out_list` AS C, `shopping_item` AS S WHERE C.user_id={request.args['user_id']} AND C.status='waiting' AND S.check_out_list_id=C.id")
        bookList = cursor.fetchall()
        if bookList.__len__() <= 0:
            return Response(code=400, data={"msg": "购物车为空或不存在"}).toJson()        
        checkOutListId = bookList[0][0]
        checkOutList=[]
        for row in bookList:
            checkOutList.append({
                "item_id": row[1],
                "book_isbn": row[2],
                "quantities": row[3]
            })
        creditCard = bookList[0][4]
        return Response(code=200, data={"msg": "获取购物车成功", "check_out_list_id": checkOutListId, "check_out_list": checkOutList, "credit_card": creditCard}).toJson()

    @app.route("/shopping_basket/abort", methods=["GET"])
    def abortShoppingBasket():
        cursor.execute(F"select * from check_out_list where `id`={request.args['check_out_list_id']} AND `status`='waiting'")
        result = cursor.fetchone()
        if result == None:
            return Response(code=400, data={"msg": "购物车不存在"}).toJson()
        cursor.execute(F"UPDATE `check_out_list` SET `status` = 'abort' WHERE (`id` = '{request.args['check_out_list_id']}');")
        conn.commit()
        return Response(code=200, data={"msg": "取消成功"}).toJson()

    @app.route("/shopping_basket/pay", methods=["GET"])
    def payShoppingBasket():
        cursor.execute(F"SELECT C.id,S.id,S.book_isbn,S.quantities,C.credit_card FROM `check_out_list` AS C, `shopping_item` AS S WHERE C.user_id={request.args['user_id']} AND C.status='waiting' AND S.check_out_list_id=C.id")
        bookList = cursor.fetchall()
        if bookList.__len__() <= 0:
            return Response(code=400, data={"msg": "购物车为空或不存在"}).toJson()     
        checkOutListId = bookList[0][0]   
        checkOutList=[]
        for row in bookList:
            checkOutList.append({
                "item_id": row[1],
                "book_isbn": row[2],
                "quantities": row[3]
            })
            cursor.execute(F"SELECT `number` FROM book_stock WHERE `book_isbn`='{row[2]}';")
            stock = cursor.fetchone()[0]
            cursor.execute(F"UPDATE `book_stock` SET `number` = {stock - row[3]} WHERE (`book_isbn` = '{row[2]}');")
            if row[3] > stock:
                conn.rollback()
                return Response(code=400, data={"msg": "库存不足"}).toJson()
        cursor.execute(F"UPDATE `check_out_list` SET `status` = 'success' WHERE (`id` = {checkOutListId});")
        
        conn.commit()
        return Response(code=200, data={"msg": "支付成功"}).toJson()

    @app.route("/shopping_basket/add_item", methods=["GET"])
    def addItem():
        cursor.execute(F"SELECT * FROM `book` where `isbn` = '{request.args['book_isbn']}'")
        book = cursor.fetchone()
        if book == None:
            return Response(code=400, data={"msg": "书不存在"}).toJson()
        
        cursor.execute(F"select id from check_out_list where `user_id`='{request.args['user_id']}' and `status`='waiting'")
        checkOutList = cursor.fetchone()    
        if checkOutList == None:
            return Response(code=400, data={"msg": "购物车不存在，请先创建购物车"}).toJson()
        
        cursor.execute(F"SELECT * FROM `check_out_list` AS C, `shopping_item` AS S WHERE C.user_id={request.args['user_id']} AND C.status='waiting' AND S.check_out_list_id=C.id AND S.book_isbn = '{request.args['book_isbn']}'")
        bookInBasket = cursor.fetchone()
        if bookInBasket != None:
            return Response(code=400, data={"msg": "书已存在购物车中"}).toJson()
        
        cursor.execute(F"INSERT INTO `shopping_item` (`quantities`, `book_isbn`, `check_out_list_id`) VALUES (1, '{request.args['book_isbn']}', {checkOutList[0]});")
        conn.commit()
        return Response(code=200, data={"msg": "添加成功"}).toJson()

    @app.route("/shopping_basket/update_item", methods=["GET"])
    def updateItem():
        cursor.execute(F"SELECT * FROM `check_out_list` AS C, `shopping_item` AS S WHERE C.user_id={request.args['user_id']} AND C.status='waiting' AND S.check_out_list_id=C.id AND S.book_isbn = '{request.args['book_isbn']}'")
        bookInBasket = cursor.fetchone()
        if bookInBasket == None:
            return Response(code=400, data={"msg": "书籍不在购物车当中"}).toJson()
        cursor.execute(F"UPDATE `check_out_list` AS C, `shopping_item` AS S SET S.quantities = {request.args['number']}  WHERE C.user_id={request.args['user_id']} AND C.status='waiting' AND S.check_out_list_id=C.id AND S.book_isbn = '{request.args['book_isbn']}'")
        conn.commit()
        return Response(code=200, data={"msg": "更新成功"}).toJson()
        
        
        

    @app.route("/shopping_basket/delete_item", methods=["GET"])
    def deleteItem():
        cursor.execute(F"SELECT * FROM shopping_item WHERE `id`={request.args['item_id']};")
        bookInBasket = cursor.fetchone()
        if bookInBasket == None:
            return Response(code=400, data={"msg": "书籍不在购物车当中"}).toJson()
        cursor.execute(F"DELETE FROM `shopping_item` WHERE `id`={request.args['item_id']};")
        conn.commit()
        return Response(code=200, data={"msg": "删除成功"}).toJson()




class BookController:
    @app.route("/book/search", methods=["GET"])
    def searchBook():
        sql = (
            "SELECT `isbn`, `quality`, `title`, `author`, `price` FROM `book` WHERE 1=1"
        )
        if request.args["isbn"] != None:
            sql += " and isbn like '%" + request.args["isbn"] + "%'"
        if request.args["title"] != None:
            sql += " and title like '%" + request.args["title"] + "%'"
        if request.args["author"] != None:
            sql += " and author like '%" + request.args["author"] + "%'"
        bookList = []
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            bookList.append(
                {
                    "isbn": row[0],
                    "quality": row[1],
                    "title": row[2],
                    "author": row[3],
                    "price": row[4],
                }
            )
        return Response(code=200, data={"bookList": bookList}).toJson()

    @app.route("/book/add", methods=["GET"])
    def addBook():
        cursor.execute(f"SELECT * FROM `book` WHERE isbn = '{request.args['isbn']}'")
        result = cursor.fetchone()
        if result != None:
            return Response(code=400, data={"msg": "该书已存在"}).toJson()
        cursor.execute(F"INSERT INTO `book` (`isbn`, `quality`, `title`, `author`, `price`) VALUES ('{request.args['isbn']}', '{request.args['quality']}', '{request.args['title']}', '{request.args['author']}', {request.args['price']});")
        cursor.execute(F"INSERT INTO `book_stock` (`book_isbn`, `number`) VALUES ('{request.args['isbn']}', 100);")
        conn.commit()
        return Response(code=200, data={"msg": "添加成功"}).toJson()
    
    
    @app.route("/book/delete", methods=["GET"])
    def deleteBook():
        sql = F"SELECT * FROM `book` WHERE isbn = '{request.args['isbn']}'"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result == None:
            return Response(code=400, data={"msg": "该书不存在"}).toJson()
        cursor.execute(F"DELETE FROM `book_stock` WHERE book_isbn = '{request.args['isbn']}';")
        cursor.execute(F"DELETE FROM `book` WHERE isbn = '{request.args['isbn']}';")
        conn.commit()
        return Response(code=200, data={"msg": "删除成功"}).toJson()

class BookStockController:
    @app.route("/bookStock/set", methods=["POST"])
    def setBookStock():
        stockList = request.json["stockList"]
        for row in stockList:
            cursor.execute(F"UPDATE `book_stock` SET `number` = {row['number']} WHERE `book_isbn` = '{row['book_isbn']}';")
        conn.commit()
        return Response(code=200, data={"msg": "设置库存量成功"}).toJson()
app.run(port="8848")
