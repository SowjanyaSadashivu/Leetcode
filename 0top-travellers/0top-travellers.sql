# Write your MySQL query statement below

select Users.name, coalesce(sum(r.distance),0) travelled_distance
from Users 
left JOIN Rides r
on r.user_id = Users.id
group by Users.id
ORDER by travelled_distance desc, Users.name ASC