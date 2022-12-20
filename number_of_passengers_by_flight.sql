select
    ap.code,
    concat(ap.manufacturer, ' ', ap.model) airplane,
    (select count(*)
    from app_booking
    where schedule_id in (fs.id)) reserved,
    fs.origin origin,
    fs.destination destination
from app_schedule fs
left join app_airplane ap on ap.id = fs.airplane_id