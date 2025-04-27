select i.name, i.datetime
from animal_ins i
left outer join animal_outs o
on i.ANIMAL_ID = o.ANIMAL_ID
where o.ANIMAL_ID is null
order by i.datetime
limit 3