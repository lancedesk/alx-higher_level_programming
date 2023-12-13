-- Create the database hbtn_0c_0 if it doesn't already exist
-- This query checks if the database exists before attempting to create it

-- Variable to hold the database name
SET @database_name = 'hbtn_0c_0';

-- Check if the database exists
-- Using the information_schema to query database names
SET @db_exists = (SELECT COUNT(*) FROM information_schema.schemata WHERE schema_name = @database_name);

-- If the database does not exist, create it
-- Using dynamic SQL to conditionally create the database
SET @create_query = IF(@db_exists = 0, CONCAT('CREATE DATABASE ', @database_name), '');

-- Execute the create query
-- This query will either create the database or do nothing if it already exists
PREPARE create_stmt FROM @create_query;
EXECUTE create_stmt;
DEALLOCATE PREPARE create_stmt;
