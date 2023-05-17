-- a script that lists all shows contained in hbtn_0d_tvshows

SELECT g.name AS genre, COUNT(tg.genre_id) AS number_of_shows
	FROM tv_genres g
JOIN tv_show_genres g
	on g.id = tg.genre_id
	WHERE genre IS NOT NULL
ORDER BY number_of_shows DESC;
