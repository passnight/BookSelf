import { Column, Entity, PrimaryGeneratedColumn } from "typeorm";

@Entity()
class User {

    @PrimaryGeneratedColumn()
    id: number;

    @Column("varchar")
    username: string;

    @Column("varchar")
    password: string;
}

export default User;
