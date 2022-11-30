select
    ep.full_name,
    fs.departure_time from_time,
    fs.arrival_time to_time,
    es.status
from app_employeeschedule es
left join app_employeecontract ec on ec.id = es.employee_contract_id
left join app_employee ep on ep.id = ec.employee_id
left join app_flightschedule fs on fs.id = es.flight_schedule_id
where ec.job in ('PILOT')



