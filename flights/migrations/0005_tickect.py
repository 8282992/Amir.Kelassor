# Generated by Django 4.2 on 2023-12-30 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_alter_flight_flight_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tickect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('national_id', models.IntegerField()),
                ('seat_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
