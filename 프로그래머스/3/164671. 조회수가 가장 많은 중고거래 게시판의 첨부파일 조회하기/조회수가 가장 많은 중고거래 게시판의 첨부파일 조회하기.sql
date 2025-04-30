select concat('/home/grep/src/',b.BOARD_ID,'/',f.FILE_ID,f.FILE_NAME,f.FILE_EXT) as FILE_PATH
from USED_GOODS_BOARD b
left outer join USED_GOODS_FILE f on b.BOARD_ID = f.BOARD_ID
where views = (select max(VIEWS) from USED_GOODS_BOARD)
order by f.FILE_ID desc