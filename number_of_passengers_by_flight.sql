select
    ap.code,
    concat(ap.manufacturer, ' ', ap.model) airplane,
    (select count(*)
    from app_booking
    where flight_schedule_id in (fs.id)) reserved,
    ao.name origin,
    ad.name destination
from app_flightschedule fs
left join app_airplane ap on ap.id = fs.airplane_id
left join app_airport ao on ao.id = fs.airport_origin_id
left join app_airport ad on ad.id = fs.airport_destination_id