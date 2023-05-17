-- a script that lists all shows contained in
-- hbtn_0d_tvshows that have at least one genre linked

SELECT t.title, g.genre_id
	FROM tv_shows t
INNER JOIN tv_show_genres g
	on t.id = g.show_id
ORDER BY t.title, g.genre_id ASC;
