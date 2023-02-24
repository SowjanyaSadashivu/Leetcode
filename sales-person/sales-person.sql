# Write your MySQL query statement below

select name
from SalesPerson
where sales_id not in
    (select sales_id
    from Orders o
    left join company 
    on o.com_id = company.com_id
    where company.name = 'RED'
    )

        
