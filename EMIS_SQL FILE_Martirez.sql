-- Create the Database
create database dbemployee;

-- Use the dbemployee
use dbemployee;

-- Create table for sex options
create table sex(
sex_id int auto_increment primary key,
sex varchar(50) not null
);
insert into sex (sex) values ("Male");
insert into sex (sex) values ("Female");

-- Create table for different departments
create table department(
dept_id int auto_increment primary key,
departments varchar(100) not null
);
insert into department (departments) values ("Finance"), 
("Marketing"),
("Information Technology"),
("Accounting"),
("Production/Operation Department");

-- Create table for employees
CREATE TABLE employee (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    MiddleName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Age INT NOT NULL,
    Sex_id INT,
    Address VARCHAR(255) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Department_id INT,
    FOREIGN KEY (Sex_id) REFERENCES sex(sex_id),
    FOREIGN KEY (Department_id) REFERENCES department(dept_id)
);
    









