-- Create the table unique_id
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256),
    PRIMARY KEY (id)
) ENGINE=InnoDB;

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
