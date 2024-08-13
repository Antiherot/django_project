from django.db import models
from django.utils import timezone

# Create your models here.

class  MissionType(models.Model):
    mission = models.CharField(max_length=100)

    def __str__(self):
        return self.mission


class MissionMonitoring(models.Model):
    day = models.DateField(default=timezone.now)
    mission_type = models.ForeignKey(MissionType, on_delete= models.CASCADE) 
    worked_time = models.DurationField(default=timezone.timedelta(minutes=0))

    def formated_date(self):
         return self.day.strftime('%d-%m-%Y')
    
    def parsed_time(self):
        total_seconds = self.worked_time.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        return f'{hours:02}:{minutes:02}'  # Format as HH:MM

    def __str__(self):
        return f'{self.formated_date()} I did {self.parsed_time()} of {self.mission_type}!'