"""AirlineCompany URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from app.views import booking_details
from app.views import airplane_pilot_details
from app.views import passenger_bookings
from app.views import pilot_schedule_by_month
from app.views import number_of_passengers_by_flight
from app.views import number_of_working_hours_by_pilot
from app.views import destinations_and_bookings

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('admin:index'))),
    path('admin/', admin.site.urls),
    path('report/booking_details', booking_details),
    path('report/airplane_pilot_details', airplane_pilot_details),
    path('report/passenger_bookings', passenger_bookings),
    path('report/pilot_schedule_by_month', pilot_schedule_by_month),
    path('report/number_of_passengers_by_flight', number_of_passengers_by_flight),
    path('report/number_of_working_hours_by_pilot', number_of_working_hours_by_pilot),
    path('report/destinations_and_bookings', destinations_and_bookings)
]
