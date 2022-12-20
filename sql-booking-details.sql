select
    pa.passport_no,
    pa.full_name,
    pk.name,
    concat(fs.departure, ' ',fs.departure) departure,
       concat(fs.origin, ' ', fs.arrival) arrival,
       IF(bk.is_connect, "YES", "NO") is_connecting
from app_booking bk
left join app_schedule fs on fs.id = bk.schedule_id
left join app_passenger pa on pa.id = bk.passenger_id
left join app_airplane ap on ap.id = fs.airplane_id
left join app_package pk on pk.id = bk.package_id
order by bk.id asc