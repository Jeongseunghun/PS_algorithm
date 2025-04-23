select b.BOOK_ID, a.AUTHOR_NAME, date_format(b.PUBLISHED_DATE,'%Y-%m-%d') as PUBLISHED_DATE
from BOOK as b
join AUTHOR as a on b.AUTHOR_ID = a.AUTHOR_ID
where CATEGORY = '경제'
order by PUBLISHED_DATE