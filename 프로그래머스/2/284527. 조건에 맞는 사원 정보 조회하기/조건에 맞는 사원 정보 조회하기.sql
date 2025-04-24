select sum(SCORE) as SCORE, e.EMP_NO, e.EMP_NAME, e.POSITION, e.EMAIL
from HR_EMPLOYEES e
join HR_GRADE g on e.EMP_NO = g.EMP_NO
group by year,g.EMP_NO
having g.year = '2022'
order by SCORE desc
limit 1

