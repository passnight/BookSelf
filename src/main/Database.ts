import { Connection, createConnection, getConnection, getRepository } from "typeorm";




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

export default connection;