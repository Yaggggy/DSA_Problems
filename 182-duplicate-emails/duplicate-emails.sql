# Write your MySQL query statement below
select distinct(a.email) as Email 
from person a
join person b 
where a.email = b.email and a.id <> b.id ; 