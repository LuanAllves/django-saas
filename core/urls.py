from django.urls import path
from . import views

app_name='core'

urlpatterns = [
    path('', views.HomeView, name='homeview' ),
    path('dashboard/', views.DashBoard, name="dashboardview"),
]