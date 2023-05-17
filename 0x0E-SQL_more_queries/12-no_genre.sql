-- a script that lists all shows contained in hbtn_0d_tvshows

SELECT t.title, g.genre_id
	FROM tv_shows t
LEFT OUTER JOIN tv_show_genres g
	on t.id = g.show_id
	WHERE g.show_id IS NULL
ORDER BY t.title, g.genre_id ASC;
