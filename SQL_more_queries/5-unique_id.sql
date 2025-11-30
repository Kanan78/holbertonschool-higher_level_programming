-- It creates the table unique_id on MySQL server
CREATE table if NOT EXISTS unique_id (
	id int DEFAULT 1 UNIQUE,
	name varchar(256)
);
