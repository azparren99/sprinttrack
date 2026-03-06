from django.db import models
from django.contrib.auth.models import User


class TrainingSession(models.Model):
    SESSION_TYPES = [
        ('speed', 'Velocidad'),
        ('strength', 'Fuerza'),
        ('tempo', 'Tempo'),
        ('technique', 'Técnica'),
        ('competition', 'Competición'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    session_type = models.CharField(max_length=20, choices=SESSION_TYPES)
    distance_m = models.PositiveIntegerField()
    time_seconds = models.FloatField()
    rest_seconds = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def pace_display(self):
        if self.distance_m > 0 and self.time_seconds > 0:
            return round(self.time_seconds / self.distance_m, 3)
        return None

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.session_type}"