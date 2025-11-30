-- It creates the table id_not_null on MySQL server
CREATE table if NOT EXISTS id_not_null (
	id int DEFAULT 1,
	name varchar(256)
);
