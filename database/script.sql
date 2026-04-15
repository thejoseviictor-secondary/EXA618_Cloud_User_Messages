CREATE SCHEMA IF NOT EXISTS `messages_schema` DEFAULT CHARACTER SET utf8mb3 ;
USE `messages_schema` ;

CREATE TABLE IF NOT EXISTS `messages_schema`.`messages_table` (
  `message_id` INT NOT NULL AUTO_INCREMENT,
  `action` VARCHAR(5) NOT NULL,
  `message` VARCHAR(255) NOT NULL,
  `author` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`message_id`)
);
