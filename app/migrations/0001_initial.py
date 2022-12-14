# Generated by Django 4.1.3 on 2022-12-20 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10)),
                ('manufacturer', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('passport_no', models.CharField(max_length=10)),
                ('full_name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
                ('sex', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='MALE', max_length=6)),
                ('place_of_birth', models.CharField(max_length=20)),
                ('date_of_issue', models.DateField()),
                ('date_of_expiry', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('origin', models.CharField(max_length=20, null=True)),
                ('destination', models.CharField(max_length=20, null=True)),
                ('departure', models.DateTimeField()),
                ('arrival', models.DateTimeField()),
                ('status', models.CharField(choices=[('ARRIVE', 'ARRIVE'), ('DEPARTURE', 'DEPARTURE'), ('IDLE', 'IDLE'), ('CANCEL', 'CANCEL')], default='IDLE', max_length=10)),
                ('airplane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.airplane')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, null=True)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.schedule')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pilot_rating', models.CharField(max_length=20, null=True)),
                ('job', models.CharField(choices=[('HOST', 'HOST'), ('PILOT', 'PILOT'), ('STAFF', 'STAFF')], default='STAFF', max_length=6)),
                ('airplane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.airplane')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_connect', models.BooleanField()),
                ('package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.package')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.passenger')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.schedule')),
            ],
        ),
        migrations.CreateModel(
            name='Assign',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('ASSIGN', 'ASSIGN'), ('CANCEL', 'CANCEL')], default='ASSIGN', max_length=10)),
                ('employee_contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.contract')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.schedule')),
            ],
        ),
    ]
