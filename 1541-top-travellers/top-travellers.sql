SELECT name,sum(
	if(distance is NULL,0,distance)
	) as travelled_distance
FROM Users u
LEFT JOIN Rides r ON u.id=r.user_id
GROUP BY User_id
ORDER BY travelled_distance desc,name asc