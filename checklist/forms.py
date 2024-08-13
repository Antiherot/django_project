from django.forms import ModelForm
from django import forms
from .models import *
from django import forms
from django.utils import timezone
from datetime import timedelta, time
from .models import MissionMonitoring, MissionType



class Postformactivityentry(forms.ModelForm):
    day = forms.DateField(
        initial=timezone.now,
        widget=forms.SelectDateWidget(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'})
    )

    worked_time = forms.TimeField(
        widget=forms.TimeInput(format='%H:%M', attrs={'class': 'form-control', 'placeholder': 'HH:MM'}),
        initial=time(0, 0)
    )

    class Meta:
        model = MissionMonitoring
        fields = ['day', 'mission_type', 'worked_time']
        widgets = {
            'mission_type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select a mission type'}),
        }

    def clean_worked_time(self):
        worked_time = self.cleaned_data.get('worked_time')
        if worked_time:
            # Convert time to timedelta
            return timedelta(hours=worked_time.hour, minutes=worked_time.minute)
        return timedelta()

    def __init__(self, *args, **kwargs):
        super(Postformactivityentry, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            worked_seconds = self.instance.worked_time.total_seconds()
            hours = int(worked_seconds // 3600)
            minutes = int((worked_seconds % 3600) // 60)
            self.initial['worked_time'] = time(hour=hours, minute=minutes)



class type_of_mission(ModelForm):
    class Meta:
        model = MissionType
        fields = ['mission']
