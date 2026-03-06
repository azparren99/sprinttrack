from django import forms
from .models import TrainingSession

class TrainingSessionForm(forms.ModelForm):
    class Meta:
        model = TrainingSession
        fields = ['date', 'session_type', 'distance_m', 'time_seconds', 'rest_seconds', 'notes']