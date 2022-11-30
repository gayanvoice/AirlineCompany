select em.full_name, em.address, em.phone,
       ec.job, ec.pilot_rating,
       concat(ap.manufacturer, ' ', ap.model) airplane,
       ap.code
from app_employee em
left join app_employeecontract ec on ec.employee_id = em.id
left join app_airplane ap on ap.id = ec.airplane_id
where ec.job in ('PILOT')