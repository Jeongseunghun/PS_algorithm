select 
case 
when month(DIFFERENTIATION_DATE) in (1,2,3)
then concat(1,'Q')
when month(DIFFERENTIATION_DATE) in (4,5,6)
then concat(2,'Q') 
when month(DIFFERENTIATION_DATE) in (7,8,9)
then concat(3,'Q')
when month(DIFFERENTIATION_DATE) in (10,11,12)
then concat(4,'Q') 
end
as QUARTER, count(ID) as ECOLI_COUNT
from ECOLI_DATA
group by QUARTER
order by QUARTER