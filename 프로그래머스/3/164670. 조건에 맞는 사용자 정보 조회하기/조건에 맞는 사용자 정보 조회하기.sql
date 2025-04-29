select u.USER_ID, u.NICKNAME, concat(CITY," ",STREET_ADDRESS1," ",STREET_ADDRESS2)as 전체주소, concat(substr(u.TLNO,1,3),"-",substr(u.TLNO,4,4),"-",substr(u.TLNO,8,4)) as 전화번호

from USED_GOODS_BOARD b
join USED_GOODS_USER u on b.WRITER_ID = u.USER_ID
group by u.USER_ID
having count(BOARD_ID) >= 3
order by USER_ID desc