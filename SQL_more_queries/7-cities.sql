-- It creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on server
CREATE database if NOT EXISTS hbtn_od_usa;
CREATE table if NOT EXISTS hbtn_0d_usa.cities(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	name varchar(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
);
