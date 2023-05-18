-- a script that lists all shows contained in hbtn_0d_tvshows

SELECT g.name AS genre, COUNT(tg.genre_id) AS number_of_shows
	FROM tv_genres g
JOIN tv_show_genres sg
	ON g.id = tg.genre_id
	WHERE number_of_shows > 0
ORDER BY number_of_shows DESC;
