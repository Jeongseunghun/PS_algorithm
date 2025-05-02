with tbl as (
    select ID, PERCENT_RANK() over (order by SIZE_OF_COLONY desc) as R
    from ECOLI_DATA
)

select ID,
case 
when tbl.R <= 0.25
then 'CRITICAL'
when tbl.R <= 0.5
then 'HIGH'
when tbl.R <= 0.75
then 'MEDIUM'
else 'LOW'
end as COLONY_NAME
from tbl
order by ID
