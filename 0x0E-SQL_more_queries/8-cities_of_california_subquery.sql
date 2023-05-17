-- a script that lists all cities of California
-- hat can be found in the database

SELECT id, name
	FROM cities
	WHERE  state_id IN (SELECT id FROM states WHERE name = "California")
ORDER BY id ASC;
