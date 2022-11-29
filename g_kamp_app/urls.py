from django.urls import path
from . import views

app_name = 'g_kamp_app'
urlpatterns = [
    path('check/', views.check, name='check')
]