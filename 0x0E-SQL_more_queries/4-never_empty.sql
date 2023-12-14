-- Create the table id_not_null
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256),
    PRIMARY KEY (id)
) ENGINE=InnoDB;

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
