select
    pa.passport_no,
    pa.full_name,
    pa.country,
    pr.price,
    cl.name,
    concat(ao.name, ' ',fs.departure_time) departure,
       concat(ad.name, ' ', fs.arrival_time) arrival,
       fs.status,
       IF(bk.is_connect, "YES", "NO") is_connecting
from app_booking bk
left join app_flightschedule fs on fs.id = bk.flight_schedule_id
left join app_passenger pa on pa.id = bk.passenger_id
left join app_price pr on pr.id = bk.price_id
left join app_airplane ap on ap.id = fs.airplane_id
left join app_airport ao on ao.id = fs.airport_origin_id
left join app_airport ad on ad.id = fs.airport_origin_id
left join app_class cl on cl.id = pr.classes_id
order by bk.id asc