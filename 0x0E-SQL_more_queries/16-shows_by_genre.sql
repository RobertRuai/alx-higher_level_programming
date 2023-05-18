-- a script that lists all shows, and all genres
-- linked to that show, from the database

SELECT t.title, g.name
	FROM (tv_shows t LEFT JOIN tv_show_genres tg ON t.id = tg.show_id)
LEFT JOIN tv_genres g ON tg.genre_id = g.id
ORDER BY t.title, g.name ASC;
