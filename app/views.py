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
left join app_employeecontract ec on ec.employee_id = em.id
left join app_airplane ap on ap.id = ec.airplane_id
where ec.job in ('PILOT')''')
    rows = cursor.fetchall()
    return render(request, 'report/airplane_pilot_details.html', {'rows': rows})


def passenger_bookings(request):
    cursor = connection.cursor()
    cursor.execute('''select
    pa.passport_no,
    pa.full_name,
    cl.name,
    concat(ao.name, ' ',fs.departure_time) departure,
       concat(ad.name, ' ', fs.arrival_time) arrival,
       IF(bk.is_connect, "YES", "NO") is_connecting
from app_booking bk
left join app_flightschedule fs on fs.id = bk.flight_schedule_id
left join app_passenger pa on pa.id = bk.passenger_id
left join app_price pr on pr.id = bk.price_id
left join app_airplane ap on ap.id = fs.airplane_id
left join app_airport ao on ao.id = fs.airport_origin_id
left join app_airport ad on ad.id = fs.airport_origin_id
left join app_class cl on cl.id = pr.classes_id
order by bk.id asc''')
    rows = cursor.fetchall()
    return render(request, 'report/passenger_bookings.html', {'rows': rows})


def pilot_schedule_by_month(request):
    cursor = connection.cursor()
    cursor.execute('''select
    ep.full_name,
    fs.departure_time from_time,
    fs.arrival_time to_time,
    es.status
from app_employeeschedule es
left join app_employeecontract ec on ec.id = es.employee_contract_id
left join app_employee ep on ep.id = ec.employee_id
left join app_flightschedule fs on fs.id = es.flight_schedule_id
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
    where flight_schedule_id in (fs.id)) reserved,
    ao.name origin,
    ad.name destination
from app_flightschedule fs
left join app_airplane ap on ap.id = fs.airplane_id
left join app_airport ao on ao.id = fs.airport_origin_id
left join app_airport ad on ad.id = fs.airport_destination_id''')
    rows = cursor.fetchall()
    return render(request, 'report/number_of_passengers_by_flight.html', {'rows': rows})


def number_of_working_hours_by_pilot(request):
    cursor = connection.cursor()
    cursor.execute('''select e.full_name,
       ec.job,
       cast(SEC_TO_TIME(
       (select TIME_TO_SEC(timediff(fs.arrival_time, fs.departure_time))
        from app_flightschedule fs where fs.id = es.flight_schedule_id)) as char) time_difference
from app_employeeschedule es
left join app_employeecontract ec on ec.id = es.employee_contract_id
left join app_employee e on e.id = ec.employee_id
where ec.job in ('PILOT')''')
    rows = cursor.fetchall()
    return render(request, 'report/number_of_working_hours_by_pilot.html', {'rows': rows})


def destinations_and_bookings(request):
    cursor = connection.cursor()
    cursor.execute('''select concat(ap.code, ' ', ap.manufacturer, ' ', ap.model) airplane,
       concat(ao.name, ' ', fs.arrival_time) arrival,
       concat(ad.name, ' ', fs.departure_time) departure
from app_flightschedule fs
left join app_airplane ap on ap.id = fs.airplane_id
left join app_airport ao on ao.id = fs.airport_origin_id
left join app_airport ad on ad.id = fs.airport_destination_id''')
    rows = cursor.fetchall()
    return render(request, 'report/destinations_and_bookings.html', {'rows': rows})
