CREATE DATABASE group3
USE group3;

CREATE TABLE IF NOT EXISTS branch(
    branch_id VARCHAR(55) NOT NULL,
    location VARCHAR(55) NOT NULL,
    PRIMARY KEY(branch_id));

-- INSERT INTO branch(branch_id)
-- VALUES
-- (Isle of Wight);

SELECT * FROM branch;
