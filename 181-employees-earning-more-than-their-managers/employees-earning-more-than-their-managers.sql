# Write your MySQL query statement below
select e.name as Employee
from Employee e 
Join Employee m
on m.id=e.managerId
where e.salary>m.salary;
