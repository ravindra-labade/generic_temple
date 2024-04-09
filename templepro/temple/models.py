from django.db import models


class Temple(models.Model):
    temple_name = models.CharField(max_length=20)
    temple_address = models.CharField(max_length=20)
    total_distance = models.IntegerField()
    devotees_per_day = models.IntegerField()
    choice = [('Online', 'ONLINE'), ('Cash', 'CASH')]
    donation_mode = models.CharField(max_length=10, choices=choice)
