from django.shortcuts import render
from .models import Donor, Patient, Hospital, Payment

def home(request):
    return render(request, 'management/home.html')

def donors(request):
    donors = Donor.objects.all()
    return render(request, 'management/donors.html', {'donors': donors})

def patients(request):
    patients = Patient.objects.all()
    return render(request, 'management/patients.html', {'patients': patients})

def hospitals(request):
    hospitals = Hospital.objects.all()
    return render(request, 'management/hospitals.html', {'hospitals': hospitals})

def payments(request):
    payments = Payment.objects.all()
    return render(request, 'management/payments.html', {'payments': payments})

def admin_page(request):
    return render(request, 'management/admin.html')
