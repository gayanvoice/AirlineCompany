from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .models import Airplane
from .models import Airport
from .models import Employee
from .models import Passenger
from .models import FlightSchedule
from .models import EmployeeContract
from .models import EmployeeSchedule
from .models import Class
from .models import Price
from .models import Booking

admin.site.register(Airplane)
admin.site.register(Airport)
admin.site.register(Employee)
admin.site.register(Passenger)
admin.site.register(FlightSchedule)
admin.site.register(EmployeeContract)
admin.site.register(EmployeeSchedule)
admin.site.register(Class)
admin.site.register(Price)
admin.site.register(Booking)
admin.site.unregister(Group)
admin.site.unregister(User)