-- setup_mysql_dev
-- Creates the database hbnb_dev_db and the user hbnb_dev

# Creates a database called 'hbnb_dev_db' if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
# Creates user 'hbnb_dev@localhost' if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
# Gives usage in every database for 'hbnb_dev@localhost'
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';
# Gives all privileges in the database 'hbnb_dev_db' to 'hbnb_dev@localhost'
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
# Gives select privileges in 'perforcmance_schema' to 'hbnb_dev@localhost'
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
