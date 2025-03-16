select round((if(order_date = customer_pref_delivery_date, 0, 1) / count(customer_id) * 100),2) as immediate_percentage
from delivery
group by customer_id limit 1