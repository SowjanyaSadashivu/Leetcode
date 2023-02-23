# Write your MySQL query statement below
select a.email as Email
from
(select email, count(email) as counts
from Person 
group by email)a
where a.counts > 1