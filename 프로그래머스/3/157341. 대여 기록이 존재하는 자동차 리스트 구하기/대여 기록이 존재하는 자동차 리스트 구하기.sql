select distinct c.CAR_ID
from CAR_RENTAL_COMPANY_CAR c
join CAR_RENTAL_COMPANY_RENTAL_HISTORY r
on c.CAR_ID = r.CAR_ID
where c.CAR_TYPE = '세단' and r.START_DATE >= '2022-10-01'
order by c.CAR_ID desc