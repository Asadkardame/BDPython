-- Create database 

create database netflix;

-- use db netflix

use netflix;

-- Create table distribution_companies
CREATE TABLE distribution_companies (
    id INT PRIMARY KEY,
    company_name VARCHAR(100)
);

-- Insert data into distribution_companies
INSERT INTO distribution_companies (id, company_name) VALUES
(1, 'Columbia Pictures'),
(2, 'Paramount Pictures'),
(3, 'Warner Bros. Pictures'),
(4, 'United Artists'),
(5, 'Universal Pictures'),
(6, 'New Line Cinema'),
(7, 'Miramax Films'),
(8, 'Produzioni Europee Associate'),
(9, 'Buena Vista'),
(10, 'StudioCanal');


-- Create table movies
CREATE TABLE movies (
    id INT PRIMARY KEY,
    movie_title VARCHAR(100),
    imdb_rating FLOAT,
    year_released INT,
    budget FLOAT,
    box_office FLOAT,
    distribution_company_id INT,
    language VARCHAR(100),
    FOREIGN KEY (distribution_company_id) REFERENCES distribution_companies(id)
);

-- Insert data into movies
INSERT INTO movies (id, movie_title, imdb_rating, year_released, budget, box_office, distribution_company_id, language) VALUES
(1, 'The Shawshank Redemption', 9.2, 1994, 25.00, 73.30, 1, 'English'),
(2, 'The Godfather', 9.2, 1972, 7.20, 291.00, 2, 'English'),
(3, 'The Dark Knight', 9.0, 2008, 185.00, 1006.00, 3, 'English'),
(4, 'The Godfather Part II', 9.0, 1974, 13.00, 93.00, 2, 'English, Sicilian'),
(5, '12 Angry Men', 9.0, 1957, 0.34, 2.00, 4, 'English'),
(6, 'Schindler''s List', 8.9, 1993, 22.00, 322.20, 5, 'English, German, Yiddish'),
(7, 'The Lord of the Rings: The Return of the King', 8.9, 2003, 94.00, 1146.00, 6, 'English'),
(8, 'Pulp Fiction', 8.8, 1994, 8.50, 213.90, 7, 'English'),
(9, 'The Lord of the Rings: The Fellowship of the Ring', 8.8, 2001, 93.00, 898.20, 6, 'English'),
(10, 'The Good, the Bad and the Ugly', 8.8, 1966, 1.20, 38.90, 8, 'English, Italian, Spanish');



-- Select all data from the table distribution_companies.

SELECT *
FROM distribution_companies;

-- Selecting a Few Columns From a Table
-- For each movie, select the movie title, the IMDb rating, and the year the movie was released.

SELECT
  movie_title,
  imdb_rating,
  year_released
FROM movies;

-- Selecting a Few Columns and Filtering Numeric Data in WHERE

SELECT
  movie_title,
  box_office
FROM movies
WHERE box_office > 300;

-- Selecting a Few Columns and Filtering Text Data in WHERE

SELECT
  movie_title,
  imdb_rating,
  year_released
FROM movies
WHERE movie_title LIKE '%Godfather%';

-- Selecting a Few Columns and Filtering Data Using Two Conditions in WHERE?

SELECT
  movie_title,
  imdb_rating,
  year_released
FROM movies
WHERE year_released < 2001 AND imdb_rating > 9;

-- Filtering Data Using WHERE and Sorting the Output

-- Select the columns movie_title, imdb_rating, and year_released from the table movies. 
-- Show movies released after 1991. Sort the output by the year released in ascending order.

SELECT
  movie_title,
  imdb_rating,
  year_released
FROM movies
WHERE year_released > 1991
ORDER BY year_released ASC;

-- Grouping Data by One Column

-- Show the count of movies per each language category.

SELECT
  language,
  COUNT(*) AS number_of_movies
FROM movies
GROUP BY language;

-- Grouping Data by Multiple Columns
-- Exercise: Show the count of movies by year released and language. Sort results by the release date in ascending order.

SELECT
  year_released,
  language,
  COUNT(*) AS number_of_movies
FROM movies
GROUP BY year_released, language
ORDER BY year_released ASC;


-- Filtering Data After Grouping

-- Show the languages spoken and the average movie budget by language category. 
-- Show only the languages with an average budget above $50 million.

SELECT
  language,
  AVG(budget) AS movie_budget
FROM movies
GROUP BY language
HAVING AVG(budget) > 50;

-- Selecting Columns From Two Tables
-- Show movie titles from the table movies, each with the name of its distribution company.

SELECT
  movie_title,
  company_name
FROM distribution_companies dc
JOIN movies m
ON dc.id = m.distribution_company_id;