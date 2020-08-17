-- setup_mysql_test
-- Creates the database hbnb_test_db and the user hbnb_test

# Creates a database called 'hbnb_test_db' if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
# Creates user 'hbnb_test@localhost' if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
# Gives usage in every database for 'hbnb_test@localhost'
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost';
# Gives all privileges in the database 'hbnb_test_db' to 'hbnb_test@localhost'
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
# Gives select privileges in 'perforcmance_schema' to 'hbnb_test@localhost'
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
