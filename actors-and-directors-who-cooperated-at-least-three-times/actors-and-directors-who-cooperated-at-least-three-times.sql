# Write your MySQL query statement below
select a.actor_id, a.director_id
from (select actor_id, director_id, count(actor_id) as actor_count, count(director_id) as director_count
from ActorDirector
group by  actor_id, director_id)a
where actor_count > 2