select i.NAME,i.DATETIME
from ANIMAL_INS i
left outer join ANIMAL_OUTS o on i.ANIMAL_ID = o.ANIMAL_ID
where o.NAME is null and i.Name is not null
order by i.DATETIME
limit 3

