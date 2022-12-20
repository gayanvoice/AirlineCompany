from django.db import models


# Create your models here.
class Airplane(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10)
    manufacturer = models.CharField(max_length=20)
    model = models.CharField(max_length=20)

    def __str__(self):
        return self.code + ' - ' + self.manufacturer + ' / ' + self.model


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name


class Passenger(models.Model):
    id = models.AutoField(primary_key=True)
    passport_no = models.CharField(max_length=10)
    full_name = models.CharField(max_length=200)
    country = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    JOB_CHOICES = [
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE')
    ]
    sex = models.CharField(
        max_length=6,
        choices=JOB_CHOICES,
        default=MALE,
    )
    place_of_birth = models.CharField(max_length=20)
    date_of_issue = models.DateField()
    date_of_expiry = models.DateField()

    def __str__(self):
        return self.passport_no + ' - ' + self.country + '/' + self.full_name


class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    origin = models.CharField(max_length=20, null=True)
    destination = models.CharField(max_length=20, null=True)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    ARRIVE = 'ARRIVE'
    DEPARTURE = 'DEPARTURE'
    IDLE = 'IDLE'
    CANCEL = 'CANCEL'
    STATUS_CHOICES = [
        (ARRIVE, 'ARRIVE'),
        (DEPARTURE, 'DEPARTURE'),
        (IDLE, 'IDLE'),
        (CANCEL, 'CANCEL')
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=IDLE,
    )

    def __str__(self):
        return str(self.id) + ' - ' + str(self.airplane) + ' / ' + str(self.origin) + ' (' + str(
            self.departure.date()) + ') / ' + str(self.destination) + ' (' + str(
            self.arrival.date()) + ')'


class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pilot_rating = models.CharField(max_length=20, null=True)
    HOST = 'HOST'
    PILOT = 'PILOT'
    STAFF = 'STAFF'
    JOB_CHOICES = [
        (HOST, 'HOST'),
        (PILOT, 'PILOT'),
        (STAFF, 'STAFF')
    ]
    job = models.CharField(
        max_length=6,
        choices=JOB_CHOICES,
        default=STAFF,
    )

    def __str__(self):
        return str(self.id) + ' - ' + str(self.airplane) + ' (' + str(self.employee) + ') / ' + self.job


class Assign(models.Model):
    id = models.AutoField(primary_key=True)
    employee_contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    ASSIGN = 'ASSIGN'
    CANCEL = 'CANCEL'
    STATUS_CHOICES = [
        (ASSIGN, 'ASSIGN'),
        (CANCEL, 'CANCEL')
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=ASSIGN,
    )

    def __str__(self):
        return str(self.id) + ' - ' + str(self.employee_contract) + '/' + str(
            self.schedule) + ' / ' + self.status


class Package(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return str(self.id) + ' - ' + str(self.name) + ' / ' + str(self.schedule) + ' / ' + str(self.price)


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)
    is_connect = models.BooleanField()

    def __str__(self):
        return str(self.id) + ' - ' + str(self.schedule) + ' - ' + str(self.passenger) + ' / ' + str(self.is_connect)
