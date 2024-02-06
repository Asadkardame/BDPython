
-- Tables:

-- Students: Contains information about students enrolled in the school.
-- Fields: student_id (Primary Key), name, age, class, etc.
-- Teachers: Contains information about teachers working in the school.
-- Fields: teacher_id (Primary Key), name, subject_taught, etc.
-- Courses: Contains information about the courses offered in the school.
-- Fields: course_id (Primary Key), course_name, teacher_id (Foreign Key), etc.
-- Grades: Contains information about the grades/grades of students in courses.
-- Fields: grade_id (Primary Key), student_id (Foreign Key), course_id (Foreign Key), grade, etc.



-- # Create databse for School

CREATE DATABASE school_management_system;

-- #Use the database to perform the operations 

USE school_management_system;

-- # Create a table structure for Students

CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    class VARCHAR(50)
);

-- # Create a table for Teachers

CREATE TABLE Teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    subject_taught VARCHAR(100)
);


-- # CReate a table for courses offered in the School

CREATE TABLE Courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100),
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
);


-- # Create a table for Student Grades

CREATE TABLE Grades (
    grade_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    grade FLOAT,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);


-- # Insert data into tables

INSERT INTO Students (name, age, class) VALUES ('John Doe', 15, '10th');
INSERT INTO Teachers (name, subject_taught) VALUES ('Jane Smith', 'Mathematics');
INSERT INTO Courses (course_name, teacher_id) VALUES ('Mathematics 101', 1);
INSERT INTO Grades (student_id, course_id, grade) VALUES (1, 1, 85.5);

-- # Retrive data from the tables  

SELECT * FROM Students;
SELECT * FROM Teachers;
SELECT * FROM Courses;
SELECT * FROM Grades;

-- # Update data into the tables

UPDATE Students SET class = '11th' WHERE student_id = 1;
UPDATE Grades SET grade = 90.0 WHERE grade_id = 1;

-- # Deleting records from the tables

-- DELETE FROM Students WHERE student_id = 1;
-- DELETE FROM Teachers WHERE teacher_id = 1;
-- DELETE FROM Courses WHERE course_id = 1;
-- DELETE FROM Grades WHERE grade_id = 1;
