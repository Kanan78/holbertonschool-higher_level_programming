-- It creates the database hbtn_0d_usa and the table states( in the database hbtn_0d_usa) on server
CREATE database if NOT EXISTS hbtn_0d_usa;
CREATE table if NOT EXISTS hbtn_0d_usa.states (
	id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name varchar(256) NOT NULL
);
