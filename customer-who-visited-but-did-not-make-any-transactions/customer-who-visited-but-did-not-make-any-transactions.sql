# Write your MySQL query statement below

select customer_id, count(v.customer_id) as count_no_trans
from Visits v
where not exists(
    select * 
    from Transactions t
    where v.visit_id = t.visit_id
)
group by v.customer_id
