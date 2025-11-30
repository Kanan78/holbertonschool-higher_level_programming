-- It creates a table second_table in the database hbtn_0c_0
CREATE table if NOT EXISTS second_table (
	id int,
	name varchar(256),
	score int
);

INSERT into second_table values
  (1, "John", 10),
  (2, "Alex", 3),
  (3, "Bob", 14),
  (4, "George", 8);
