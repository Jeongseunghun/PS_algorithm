select round(sum(ifnull(length,10))/count(*),2) AS AVERAGE_LENGTH
from FISH_INFO