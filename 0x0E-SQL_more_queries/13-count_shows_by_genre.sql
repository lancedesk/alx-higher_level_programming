-- List genres and the number of shows linked to each
SELECT genre, COUNT(*) AS number_of_shows
FROM tv_show_genres
GROUP BY genre
ORDER BY number_of_shows DESC;
