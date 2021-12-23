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
        cursor.execute(
            f"select * from check_out_list where `credit_card`='{request.args['credit_card']}' and `status`='waiting'"
        )
        result = cursor.fetchone()
        if result != None:
            return Response(code=400, data={"msg": "购物车已存在"}).toJson()
        cursor.execute(
            f"INSERT INTO `check_out_list` (`credit_card`, `status`) VALUES ('{request.args['credit_card']}', 'waiting');"
        )
        conn.commit()
        return Response(code=200, data={"msg": "创建购物车成功"}).toJson()

    @app.route("/shopping_basket/delete", methods=["GET"])
    def delete():
        cursor.execute(
            f"DELETE S.*, C.* FROM `shopping_item` as SLEFT JOIN `check_out_list` as C ON S.check_out_list_id = C.id WHERE AND S.owner_id = {request.args['owner_id']};"
        )
        conn.commit()
        return Response(code=200, data={"msg": "删除成功"}).toJson()

    @app.route("/shopping_basket/get", methods=["GET"])
    def get():
        cursor.execute(
            f"""SELECT C.id,S.id, S.book_isbn,S.quantities FROM `shopping_item` AS S, `check_out_list` AS C
    WHERE
    S.check_out_list_id = C.id
    AND C.status = 'waiting'
    AND S.owner_id = {request.args['owner_id']}
                       """
        )
        checkoutListId = cursor.fetchone()[0]
        bookList = []
        for row in cursor.fetchall():
            bookList.append(
                {"item_id": row[1], "book_isbn": row[2], "quantities": row[3]}
            )
        return Response(
            code=200, data={"checkoutListId": checkoutListId, "bookList": bookList}
        ).toJson()

    @app.route("/shoppingBasket/abort", methods=["GET"])
    def abort():
        cursor.execute(
            f"""
UPDATE 
    `shopping_item` AS S,
    `check_out_list` AS C
SET C.status='abort'
WHERE
    S.check_out_list_id = C.id
    AND C.status = 'waiting'
    AND S.owner_id={request.args['owner_id']}"""
        )
        conn.commit()
        return Response(code=200, data={"msg": "取消成功"}).toJson()

    @app.route("/shoppingBasket/pay", methods=["GET"])
    def pay():
        cursor.execute(
            f"""
UPDATE 
    `shopping_item` AS S,
    `check_out_list` AS C
SET C.status='abort'
WHERE
    S.check_out_list_id = C.id
    AND C.status = 'success'
    AND S.owner_id={request.args['owner_id']}"""
        )
        conn.commit()
        return Response(code=200, data={"msg": "取消成功"}).toJson()

    @app.route("/shoppingBasket/updateItem", methods=["GET"])
    def updateItem():
        cursor.execute(
            f"""
UPDATE 
    `shopping_item`
SET quantities = {request.args['quantities']}
WHERE
    id = {request.args['item_id']}"""
        )
        conn.commit()
        return Response(code=200, data={"msg": "修改成功"}).toJson()

    @app.route("/shoppingBasket/deleteItem", methods=["GET"])
    def deleteItem():
        cursor.execute(
            f"""DELETE FROM `shopping_item` WHERE id = {request.args['item_id']}"""
        )
        conn.commit()
        return Response(code=200, data={"msg": "删除成功"}).toJson()

    @app.route("/shoppingBasket/addItem", methods=["GET"])
    def addItem():
        cursor.execute(
            f"""
SELECT
	C.id
FROM 
    `shopping_item` AS S,
    `check_out_list` AS C
WHERE
    S.check_out_list_id = C.id
    AND C.status = 'waiting'
    AND S.owner_id={request.args['owner_id']}"""
        )
        checkOutListId = cursor.fetchone()[0]
        if checkOutListId == None:
            return Response(code=400, data={"ms": "请先创建购物车"}).toJson()
        cursor.execute(
            f"INSERT INTO `database_course_project`.`shopping_item` (`quantities`, `book_isbn`, `owner_id`, `check_out_list_id`) VALUES (1, '{request.args['book_isbn']}', '{request.args['owner_id']}', {checkOutListId});"
        )
        conn.commit()
        return Response(code=200, data={"msg": "添加成功"}).toJson()


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
        sql = f"INSERT INTO `book` (`isbn`, `quality`, `title`, `author`, `price`) VALUES ('{request.args['isbn']}', '{request.args['quality']}', '{request.args['title']}', '{request.args['author']}', {request.args['price']});"
        cursor.execute(sql)
        conn.commit()
        return Response(code=200, data={"msg": "添加成功"}).toJson()
    @app.route("/book/delete", methods=["GET"])
    def deleteBook():
        cursor.execute(f"SELECT * FROM `book` WHERE isbn = '{request.args['isbn']}'")
        result = cursor.fetchone()
        if result == None:
            return Response(code=400, data={"msg": "该书不存在"}).toJson()
        cursor.execute(F"DELETE FROM `book` WHERE isbn = '{request.args['isbn']}'")
        conn.commit()
        return Response(code=200, data={"msg": "删除成功"}).toJson()


app.run(port="8848")
