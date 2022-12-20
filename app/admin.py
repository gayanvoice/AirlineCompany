from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .models import Airplane
from .models import Employee
from .models import Passenger
from .models import Schedule
from .models import Contract
from .models import Assign
from .models import Package
from .models import Booking

admin.site.register(Airplane)
admin.site.register(Employee)
admin.site.register(Passenger)
admin.site.register(Schedule)
admin.site.register(Contract)
admin.site.register(Assign)
admin.site.register(Package)
admin.site.register(Booking)
admin.site.unregister(Group)
admin.site.unregister(User)
