select ae.full_name,
       ac.job,
       cast(SEC_TO_TIME(
       (select TIME_TO_SEC(timediff(a.arrival, a.departure)) from app_schedule a where a.id =
             (select an.schedule_id from app_assign an where an.employee_contract_id = 1))) as char) time_difference
from app_contract ac
left join app_employee ae on ac.employee_id = ae.id
where ac.job in ('PILOT')