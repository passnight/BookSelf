CREATE TABLE `user` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `username` VARCHAR(255) NULL,
    `password` VARCHAR(225) NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE `book`(
    `isbn` VARCHAR(225) NOT NULL,
    `quality` VARCHAR(255),
    `title` VARCHAR(255),
    `author` VARCHAR(255),
    `price` DOUBLE,
    PRIMARY KEY (`isbn`)
);

CREATE TABLE `check_out_list`(
    `id` INT NOT NULL AUTO_INCREMENT,
    `credit_card` VARCHAR(255),
    `status` VARCHAR(255),
    PRIMARY KEY (`id`)
);

CREATE TABLE `book_stock` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `book_isbn` VARCHAR(225) NOT NULL,
    `number` INT NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`book_isbn`) REFERENCES `book`(`isbn`)
);

CREATE TABLE `shopping_item` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `quantities` INT NULL,
    `book_isbn` VARCHAR(255) NULL,
    `owner_id` INT NULL,
    `check_out_list_id` INT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`owner_id`) REFERENCES `user`(`id`),
    FOREIGN KEY (`book_isbn`) REFERENCES `book`(`isbn`),
    FOREIGN KEY (`check_out_list_id`) REFERENCES `check_out_list`(`id`)
);


INSERT INTO `database_course_project`.`user` (`username`, `password`) VALUES ('name1', '123456');
INSERT INTO `database_course_project`.`user` (`username`, `password`) VALUES ('name2', '123456');

INSERT INTO `database_course_project`.`book` (`isbn`, `quality`, `title`, `author`, `price`) VALUES ('1', 'good', 'book1', 'author of book1', '998');
INSERT INTO `database_course_project`.`book` (`isbn`, `quality`, `title`, `author`, `price`) VALUES ('2', 'normal', 'book2', 'author of book2', '100');
INSERT INTO `database_course_project`.`book` (`isbn`, `quality`, `title`, `author`, `price`) VALUES ('3', 'bad', 'book3', 'author of book 3', '10');
