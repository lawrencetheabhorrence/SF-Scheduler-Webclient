from django.db import models

# Create your models here.
class Game(models.Model):
    name=models.CharField(max_length=300)
    n_timeslots_per_round=models.IntegerField()
    priority_choices = [(a,a) for a in ['Major','Minor','Junior']]
    priority=models.CharField(choices=priority_choices,default='Minor')
