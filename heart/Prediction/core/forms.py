from django import forms
from .models import Prediction

# 🔹 Define choices before the class
SEX_CHOICES = [
    (1, 'Male'),
    (0, 'Female'),
]

CP_CHOICES = [
    (0, 'Typical Angina'),
    (1, 'Atypical Angina'),
    (2, 'Non-anginal Pain'),
    (3, 'Asymptomatic'),
]

FBS_CHOICES = [
    (1, 'True (≥120 mg/dl)'),
    (0, 'False'),
]

RESTECG_CHOICES = [
    (0, 'Normal'),
    (1, 'ST-T Wave Abnormality'),
    (2, 'Left Ventricular Hypertrophy'),
]

EXANG_CHOICES = [
    (1, 'Yes'),
    (0, 'No'),
]

SLOPE_CHOICES = [
    (0, 'Upsloping'),
    (1, 'Flat'),
    (2, 'Downsloping'),
]

CA_CHOICES = [(i, str(i)) for i in range(5)]  # 0–4
THAL_CHOICES = [
    (0, 'Normal'),
    (1, 'Fixed Defect'),
    (2, 'Reversible Defect'),
    (3, 'Unknown'),
]


class PredictionForm(forms.ModelForm):
    class Meta:
        model = Prediction
        fields = [
            'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
            'exang', 'oldpeak', 'slope', 'ca', 'thal'
        ]

        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'sex': forms.Select(choices=SEX_CHOICES, attrs={'class': 'form-control'}),
            'cp': forms.Select(choices=CP_CHOICES, attrs={'class': 'form-control'}),
            'trestbps': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Resting BP'}),
            'chol': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cholesterol'}),
            'fbs': forms.Select(choices=FBS_CHOICES, attrs={'class': 'form-control'}),
            'restecg': forms.Select(choices=RESTECG_CHOICES, attrs={'class': 'form-control'}),
            'thalach': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Max Heart Rate'}),
            'exang': forms.Select(choices=EXANG_CHOICES, attrs={'class': 'form-control'}),
            'oldpeak': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ST Depression'}),
            'slope': forms.Select(choices=SLOPE_CHOICES, attrs={'class': 'form-control'}),
            'ca': forms.Select(choices=CA_CHOICES, attrs={'class': 'form-control'}),
            'thal': forms.Select(choices=THAL_CHOICES, attrs={'class': 'form-control'}),
        }
