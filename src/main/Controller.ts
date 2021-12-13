import express from 'express';
import { Connection, createConnection, getConnection, getRepository } from "typeorm";
import User from "./entity/User";

async function initDatabase() {
    await createConnection({
        type: "mysql",
        host: "localhost",
        port: 3306,
        username: "root",
        password: "123456",
        database: "database_course_project",
        entities: [__dirname + "\\entity\\*.ts"],
        synchronize: true
    }).catch(error => console.log(error));
    console.log("connect to database success");
}
initDatabase();


const connection = getConnection();
const app = express();









function initExpress() {
    connection.getRepository(User)

    //设置跨域访问
    app.all('*', function (req, res, next) {
        res.header("Access-Control-Allow-Origin", "*");
        res.header("Access-Control-Allow-Headers", "X-Requested-With");
        res.header("Access-Control-Allow-Methods", "PUT,POST,GET,DELETE,OPTIONS");
        res.header("X-Powered-By", ' 3.2.1')
        res.header("Content-Type", "application/json;charset=utf-8");
        next();
    });


    app.get('/hello', (req, res) => res.send('Hello World!'))



    app.get("/test1", (req, res) => {
        res.send(JSON.stringify(connection.options));
    })





    app.listen(8848, () => {
        console.log("the backend is activated");
    })
}

// console.log(connection.options);

export default initExpress;