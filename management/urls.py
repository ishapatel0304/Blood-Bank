# management/urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('donors/', views.donors, name='donors'),
    path('patients/', views.patients, name='patients'),
    path('hospitals/', views.hospitals, name='hospitals'),
    path('payments/', views.payments, name='payments'),
    path('admin/', views.admin_page, name='admin'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
