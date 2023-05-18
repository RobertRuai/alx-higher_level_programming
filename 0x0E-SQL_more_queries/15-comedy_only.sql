-- a script that lists all Comedy shows in the database hbtn_0d_tvshows

SELECT t.title
	FROM (tv_genres g JOIN tv_show_genres tg ON g.id = tg.genre_id)
	JOIN tv_shows t ON tg.show_id = t.id
	WHERE g.name = "Comedy"
ORDER BY t.title ASC;
