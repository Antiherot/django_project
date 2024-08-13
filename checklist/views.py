from django.shortcuts import render, redirect
from .models import MissionMonitoring, MissionType
from checklist.forms import Postformactivityentry
import pandas as pd
from django.db.models import F,Count,Sum
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import json
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy



def checklist(request):
    Acheivments_ = MissionMonitoring.objects.all()

    if request.method == 'POST':
        form = Postformactivityentry(request.POST)
        if form.is_valid():
            form.save()
            return redirect('checklist')  # Redirect back to the checklist view after form submission
    else:
        form = Postformactivityentry()
    
    
    for_pd = list(MissionMonitoring.objects.annotate(value_mission_type=F('mission_type__mission')).values('day','value_mission_type','worked_time'))
    df = pd.DataFrame(for_pd)
    missions_counts =   df['value_mission_type'].value_counts()
    Unique_misisons = missions_counts.index.tolist()
    Unique_misisons_count = missions_counts.values.tolist()
    
    # Convert lists to JSON
    from django.utils.html import escapejs
    Unique_misisons_json = json.dumps(Unique_misisons)
    Unique_misisons_count_json = json.dumps(Unique_misisons_count)
  

    # I need sum(worked_time) group by over the past 7 days/ 7
    from django.utils import timezone
    from datetime import timedelta

    Days_ago = timezone.now()- timedelta(days=7)

    
    worked_time_other_past_7 = list(MissionMonitoring.objects.filter(day__gt=Days_ago).values(
    ('mission_type__mission')).annotate(
        total_worked = Sum('worked_time')))
    mission_type = []
    mission_type_worked_time = []
    for x in worked_time_other_past_7:
        total_worked = x['total_worked']
        if isinstance(total_worked, timedelta):
            total_worked = (total_worked.total_seconds()/60)/60
        mission_type_worked_time.append(total_worked)
        mission_type.append(x['mission_type__mission'])
       
    
    mission_type = json.dumps(mission_type)
    mission_type_worked_time = json.dumps(mission_type_worked_time)

     
    return render(request, 'activities_entries.html', {
        'context_form': form,
        'Acheivments': Acheivments_,
        'Unique_misisons': Unique_misisons_json,
        'Unique_misisons_count': Unique_misisons_count_json,
        'mission_type': mission_type,
        'mission_type_worked_time': mission_type_worked_time
        
        })


class edit_entries(UpdateView):
    model = MissionMonitoring
    fields = ['worked_time']
    template_name = 'edit_entries.html'
    success_url = reverse_lazy('checklist')



