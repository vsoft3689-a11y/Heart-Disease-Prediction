from django.contrib import admin
from .models import Prediction

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'sex', 'chol', 'trestbps', 'result', 'probability', 'created_at')
    list_filter = ('result', 'sex', 'user')
    search_fields = ('user__username', 'age', 'chol')
from django.contrib import admin

# Register your models here.
