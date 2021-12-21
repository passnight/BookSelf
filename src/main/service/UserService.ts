import { Connection, createConnection, getConnection, getRepository } from "typeorm";


class UserService {
    userRepository;

    async connect() {
        await createConnection({
            name: "default",
            type: "mysql",
            host: "localhost",
            port: 3306,
            username: "root",
            password: "123456",
            database: "database_course_project",
            entities: [__dirname + "\\..\\entity\\*.js"],
            synchronize: true
        }).catch(error => console.log(error));
        this.userRepository = getRepository("User");
        console.log("connect to database success");
    }
    addUser(user) {
        console.log(this.userRepository);
        this.userRepository.save(user);
    }
}


export default UserService;