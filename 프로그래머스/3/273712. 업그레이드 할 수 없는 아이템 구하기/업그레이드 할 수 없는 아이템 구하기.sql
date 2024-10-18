select A.ITEM_ID, A.ITEM_NAME, A.RARITY
from ITEM_INFO AS A
where ITEM_ID not in (select PARENT_ITEM_ID from ITEM_TREE
                     where not isnull(PARENT_ITEM_ID)
                     )

order by ITEM_ID desc