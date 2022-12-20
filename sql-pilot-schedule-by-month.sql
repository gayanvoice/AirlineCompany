select
    ep.full_name,
    fs.departure from_time,
    fs.arrival to_time,
    es.status
from app_assign es
left join app_contract ec on ec.id = es.id
left join app_employee ep on ep.id = ec.employee_id
left join app_schedule fs on fs.id = es.schedule_id
where ec.job in ('PILOT')