select o.ANIMAL_ID,o.NAME
from ANIMAL_INS i
right outer join ANIMAL_OUTS o
on i.ANIMAL_ID = o.ANIMAL_ID
where i.ANIMAL_ID is null
order by i.ANIMAL_ID

