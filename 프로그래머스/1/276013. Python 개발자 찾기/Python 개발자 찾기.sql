select ID,EMAIL,FIRST_NAME,LAST_NAME
from DEVELOPER_INFOS
Where SKILL_1 = 'Python' or SKILL_2 = 'Python' or SKILL_3 = 'Python'
order by ID