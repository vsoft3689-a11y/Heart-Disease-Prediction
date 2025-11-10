from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from .forms import PredictionForm
from .models import Prediction
import joblib, os
import numpy as np
from django.conf import settings
import pandas as pd


# ------------------ HOME PAGE ------------------
def home_page(request):
    return render(request, "home.html")


def about_view(request):
    return render(request, 'about.html')


# ------------------ USER REGISTRATION ------------------
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Account created successfully! Please log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


# ------------------ FORGOT PASSWORD (No Email Needed) ------------------
def forgot_password_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password != confirm_password:
            messages.error(request, "⚠️ Passwords do not match.")
        else:
            try:
                user = User.objects.get(username=username)
                user.set_password(new_password)
                user.save()
                messages.success(request, "✅ Password updated successfully! Please log in.")
                return redirect('login')
            except User.DoesNotExist:
                messages.error(request, "❌ Username not found.")

    return render(request, 'registration/forgot_password.html')


# ------------------ CHANGE PASSWORD (For Logged-in Users) ------------------
@login_required
def change_password_view(request):
    if request.method == "POST":
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if not request.user.check_password(current_password):
            messages.error(request, "❌ Current password is incorrect.")
        elif new_password != confirm_password:
            messages.error(request, "⚠️ New passwords do not match.")
        else:
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, "✅ Password changed successfully!")
            return redirect('dashboard')

    return render(request, 'change_password.html')


# ------------------ MODEL LOADING ------------------
MODEL_PATH = os.path.join(settings.BASE_DIR, 'ml_models', 'heart_pipeline_v6.joblib')
model = joblib.load(MODEL_PATH)


# ------------------ PREDICTION VIEW ------------------
@login_required
def predict_view(request):
    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            prediction = form.save(commit=False)
            prediction.user = request.user

            data = {
                'age': prediction.age,
                'sex': prediction.sex,
                'cp': prediction.cp,
                'trestbps': prediction.trestbps,
                'chol': prediction.chol,
                'fbs': prediction.fbs,
                'restecg': prediction.restecg,
                'thalach': prediction.thalach,
                'exang': prediction.exang,
                'oldpeak': prediction.oldpeak,
                'slope': prediction.slope,
                'ca': prediction.ca,
                'thal': prediction.thal
            }

            try:
                trained_features = model.feature_names_in_
            except AttributeError:
                trained_features = list(data.keys())

            df = pd.DataFrame([[data[f] for f in trained_features]], columns=trained_features)

            pred_class = model.predict(df)[0]
            pred_proba = model.predict_proba(df)[0][1]

            prediction.result = "High Risk" if pred_class == 1 else "Low Risk"
            prediction.probability = round(float(pred_proba), 2)
            prediction.save()

            return render(request, "result.html", {"prediction": prediction})
    else:
        form = PredictionForm()

    return render(request, "predict.html", {"form": form})


# ------------------ DASHBOARD VIEW ------------------
@login_required
def dashboard_view(request):
    predictions = Prediction.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "dashboard.html", {"predictions": predictions})
