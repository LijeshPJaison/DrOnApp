# Generated by Django 4.0.3 on 2023-06-20 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=20)),
                ('select_hospital', models.CharField(max_length=200)),
                ('select_department', models.CharField(max_length=200)),
                ('select_doctor', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('mobile_number', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
                ('confirm_password', models.CharField(max_length=50)),
            ],
        ),
    ]
