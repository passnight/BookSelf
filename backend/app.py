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
    def login():
        cursor.execute(F"select * from user where username='{request.args['username']}' and password='{request.args['password']}'")
        result = cursor.fetchone()
        if(result == None):
            return Response(code=400, data={"msg": "用户名或密码错误"}).toJson()
        else:
            return Response(code=200, data={"msg": "登录成功"}).toJson()
    
    
    @app.route("/user/register", methods=["GET"])
    def register():
        cursor.execute(F"select * from user where username='{request.args['username']}'")
        result = cursor.fetchone()
        if(result != None):
            return Response(code=400, data={"msg": "用户已存在"}).toJson()
        cursor.execute(F"insert into user(username, password) values('{request.args['username']}', '{request.args['password']}')")
        conn.commit()
        return Response(code=200, data={"msg": "注册成功"}).toJson()

class ShoppingBasketController:
    @app.route("/shoppingBasket/add", methods=["GET"])
    def add():
        pass
    
    @app.route("/shoppingBasket/delete", methods=["GET"])
    def delete():
        pass
    
    @app.route("/shoppingBasket/get", methods=["GET"])
    def get():
        pass
        @app.route("/shoppingBasket/abort", methods=["GET"])
    def abort():
        pass
    
    @app.route("/shoppingBasket/updateItem", methods=["GET"])
    def updateItem():
        pass
    
    @app.route("/shoppingBasket/deleteItem", methods=["GET"])
    def deleteItem():
        pass
    
    @app.route("/shoppingBasket/addItem", methods=["GET"])
    def addItem():
        pass

class SearchController:
    @app.route("/search/get", methods=["GET"])
    def search():
        pass
app.run(port="8848")
