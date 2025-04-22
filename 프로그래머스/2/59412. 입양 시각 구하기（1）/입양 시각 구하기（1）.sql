select HOUR(DATETIME) as HOUR, count(ANIMAL_TYPE) as COUNT
from ANIMAL_OUTS
group by HOUR(DATETIME)
having HOUR>=9 and HOUR <= 19
order by HOUR
