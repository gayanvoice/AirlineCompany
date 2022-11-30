select e.full_name,
       ec.job,
       cast(SEC_TO_TIME(
       (select TIME_TO_SEC(timediff(fs.arrival_time, fs.departure_time))
        from app_flightschedule fs where fs.id = es.flight_schedule_id)) as char) time_difference
from app_employeeschedule es
left join app_employeecontract ec on ec.id = es.employee_contract_id
left join app_employee e on e.id = ec.employee_id
where ec.job in ('PILOT')