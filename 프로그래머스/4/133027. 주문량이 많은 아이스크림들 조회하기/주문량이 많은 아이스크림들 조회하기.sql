select f.flavor
from FIRST_HALF f
join JULY j
on f.FLAVOR = j.FLAVOR
group by FLAVOR
order by sum(j.TOTAL_ORDER) + sum(f.TOTAL_ORDER) desc
limit 3