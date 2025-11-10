# core/models.py
from django.db import models
from django.conf import settings
from django.utils import timezone


class Prediction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    # Input fields
    age = models.PositiveIntegerField()
    sex = models.PositiveSmallIntegerField(help_text="1 = male, 0 = female")
    cp = models.PositiveSmallIntegerField(help_text="Chest pain type (0–3)")
    trestbps = models.PositiveIntegerField(help_text="Resting blood pressure")
    chol = models.PositiveIntegerField(help_text="Cholesterol level")
    fbs = models.PositiveSmallIntegerField(help_text="Fasting blood sugar (1 = true, 0 = false)")
    restecg = models.PositiveSmallIntegerField(help_text="Resting ECG results (0–2)")
    thalach = models.PositiveIntegerField(help_text="Maximum heart rate achieved")
    exang = models.PositiveSmallIntegerField(help_text="Exercise induced angina (1 = yes, 0 = no)")
    oldpeak = models.FloatField(help_text="ST depression induced by exercise")
    slope = models.PositiveSmallIntegerField(help_text="Slope of peak exercise ST segment")
    ca = models.PositiveSmallIntegerField(help_text="Number of major vessels colored by fluoroscopy")
    thal = models.PositiveSmallIntegerField(help_text="Thalassemia (0–3)")

    # ✅ change this field from number to text
    result = models.CharField(max_length=20, null=True, blank=True)
    probability = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.result} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"

