from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import SensorDataForm
from .models import SensorData
from django.contrib.auth.models import User
from ai_core.models import Diagnosis
import json
from django.db.models.functions import TruncDate
from django.db.models import Count

# Create your views here.

def home(request):
    return render(request, 'core/landing.html')

@login_required
def sensor_input(request):
    if request.method == 'POST':
        form = SensorDataForm(request.POST)
        if form.is_valid():
            sensor_data = form.save(commit=False)
            sensor_data.user = request.user
            sensor_data.save()
            return redirect('sensor_data_display')
    else:
        form = SensorDataForm()
    return render(request, 'core/sensor_input.html', {'form': form})

@login_required
def sensor_data_display(request):
    latest_data = SensorData.objects.filter(user=request.user).order_by('-created_at').first()
    return render(request, 'core/sensor_data_display.html', {'latest_data': latest_data})

def admin_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

@admin_required
def analytics_dashboard(request):
    total_users = User.objects.count()
    total_diagnoses = Diagnosis.objects.count()
    total_sensor = SensorData.objects.count()
    # Most common diseases
    from collections import Counter
    disease_list = Diagnosis.objects.values_list('result', flat=True)
    disease_counts = Counter(disease_list)
    top_diseases = disease_counts.most_common(5)
    # Bar chart data
    bar_labels = [d for d, _ in top_diseases]
    bar_data = [c for _, c in top_diseases]
    # Diagnoses per day (line chart)
    diagnoses_by_day = Diagnosis.objects.annotate(day=TruncDate('created_at')).values('day').annotate(count=Count('id')).order_by('day')
    line_labels = [str(d['day']) for d in diagnoses_by_day]
    line_data = [d['count'] for d in diagnoses_by_day]
    # User role distribution (pie chart)
    from accounts.models import Profile
    role_counts = Profile.objects.values('role').annotate(count=Count('id'))
    pie_labels = [r['role'].capitalize() for r in role_counts]
    pie_data = [r['count'] for r in role_counts]
    return render(request, 'core/analytics_dashboard.html', {
        'total_users': total_users,
        'total_diagnoses': total_diagnoses,
        'total_sensor': total_sensor,
        'top_diseases': top_diseases,
        'bar_labels': json.dumps(bar_labels),
        'bar_data': json.dumps(bar_data),
        'line_labels': json.dumps(line_labels),
        'line_data': json.dumps(line_data),
        'pie_labels': json.dumps(pie_labels),
        'pie_data': json.dumps(pie_data),
    })
