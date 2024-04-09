# Generated by Django 5.0.4 on 2024-04-09 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temple',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temple_name', models.CharField(max_length=20)),
                ('temple_address', models.CharField(max_length=20)),
                ('total_distance', models.IntegerField()),
                ('devotees_per_day', models.IntegerField()),
                ('donation_mode', models.CharField(choices=[('Online', 'ONLINE'), ('Cash', 'CASH')], max_length=10)),
            ],
        ),
    ]