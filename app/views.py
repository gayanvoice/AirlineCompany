from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection


# Create your views here.
def booking_details(request):
    cursor = connection.cursor()
    cursor.execute('''select
    pa.passport_no,
    pa.full_name,
    pa.country,
    concat(fs.origin, ' ',fs.departure) departure,
       concat(fs.destination, ' ', fs.arrival) arrival,
       fs.status,
       IF(bk.is_connect, "YES", "NO") is_connecting
from app_booking bk
left join app_schedule fs on fs.id = bk.schedule_id
left join app_passenger pa on pa.id = bk.passenger_id
left join app_package pk on bk.id = bk.package_id
left join app_airplane ap on ap.id = fs.airplane_id
order by bk.id asc
''')
    rows = cursor.fetchall()
    return render(request, 'report/booking_details.html', {'rows': rows})


def airplane_pilot_details(request):
    cursor = connection.cursor()
    cursor.execute('''select em.full_name, em.address, em.phone,
       ec.job, ec.pilot_rating,
       concat(ap.manufacturer, ' ', ap.model) airplane,
       ap.code
from app_employee em
left join app_contract ec on ec.employee_id = em.id
left join app_airplane ap on ap.id = ec.airplane_id
where ec.job in ('PILOT')''')
    rows = cursor.fetchall()
    return render(request, 'report/airplane_pilot_details.html', {'rows': rows})


def passenger_bookings(request):
    cursor = connection.cursor()
    cursor.execute('''select
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
order by bk.id asc''')
    rows = cursor.fetchall()
    return render(request, 'report/passenger_bookings.html', {'rows': rows})


def pilot_schedule_by_month(request):
    cursor = connection.cursor()
    cursor.execute('''select
    ep.full_name,
    fs.departure from_time,
    fs.arrival to_time,
    es.status
from app_assign es
left join app_contract ec on ec.id = es.id
left join app_employee ep on ep.id = ec.employee_id
left join app_schedule fs on fs.id = es.schedule_id
where ec.job in ('PILOT')''')
    rows = cursor.fetchall()
    return render(request, 'report/pilot_schedule_by_month.html', {'rows': rows})


def number_of_passengers_by_flight(request):
    cursor = connection.cursor()
    cursor.execute('''select
    ap.code,
    concat(ap.manufacturer, ' ', ap.model) airplane,
    (select count(*)
    from app_booking
    where schedule_id in (fs.id)) reserved,
    fs.origin origin,
    fs.destination destination
from app_schedule fs
left join app_airplane ap on ap.id = fs.airplane_id''')
    rows = cursor.fetchall()
    return render(request, 'report/number_of_passengers_by_flight.html', {'rows': rows})


def number_of_working_hours_by_pilot(request):
    cursor = connection.cursor()
    cursor.execute('''select ae.full_name,
       ac.job,
       cast(SEC_TO_TIME(
       (select TIME_TO_SEC(timediff(a.arrival, a.departure)) from app_schedule a where a.id =
             (select an.schedule_id from app_assign an where an.employee_contract_id = 1))) as char) time_difference
from app_contract ac
left join app_employee ae on ac.employee_id = ae.id
where ac.job in ('PILOT')''')
    rows = cursor.fetchall()
    return render(request, 'report/number_of_working_hours_by_pilot.html', {'rows': rows})


def destinations_and_bookings(request):
    cursor = connection.cursor()
    cursor.execute('''select concat(ap.code, ' ', ap.manufacturer, ' ', ap.model) airplane,
       concat(fs.destination, ' ', fs.arrival) arrival,
       concat(fs.origin, ' ', fs.departure) departure
from app_schedule fs
left join app_airplane ap on ap.id = fs.airplane_id''')
    rows = cursor.fetchall()
    return render(request, 'report/destinations_and_bookings.html', {'rows': rows})
