-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema porsche
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema porsche
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `porsche` DEFAULT CHARACTER SET utf8 ;
USE `porsche` ;

-- -----------------------------------------------------
-- Table `porsche`.`type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `porsche`.`type` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `brand` VARCHAR(10) NOT NULL,
  `type` VARCHAR(20) NOT NULL,
  `toevoeging` VARCHAR(50) NULL DEFAULT NULL,
  `jaar` INT(11) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 12
DEFAULT CHARACTER SET = utf8
COMMENT = 'zijn alle types die er zijn';


-- -----------------------------------------------------
-- Table `porsche`.`technical_details`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `porsche`.`technical_details` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `aantal_cyl` INT(11) NOT NULL,
  `inhoud_motor` VARCHAR(10) NOT NULL,
  `aantal_pk` VARCHAR(10) NOT NULL,
  `max_snelheid` VARCHAR(5) NOT NULL,
  `type_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`, `type_id`),
  INDEX `fk_technical_details_type_idx` (`type_id` ASC) VISIBLE,
  CONSTRAINT `fk_technical_details_type`
    FOREIGN KEY (`type_id`)
    REFERENCES `porsche`.`type` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
