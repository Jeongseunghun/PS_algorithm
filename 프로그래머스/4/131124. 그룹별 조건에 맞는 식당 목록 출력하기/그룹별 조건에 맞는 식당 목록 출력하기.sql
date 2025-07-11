SELECT p.MEMBER_NAME,r.REVIEW_TEXT,date_format(r.REVIEW_DATE,"%Y-%m-%d")
from MEMBER_PROFILE p
join REST_REVIEW r
on p.MEMBER_ID = r.MEMBER_ID
where r.MEMBER_ID = (
select MEMBER_ID
from REST_REVIEW
group by MEMBER_ID
order by sum(REVIEW_SCORE) desc
limit 1
)
order by r.REVIEW_DATE, r.REVIEW_TEXT