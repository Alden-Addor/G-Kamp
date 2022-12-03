from django.urls import path
from . import views

app_name = 'g_kamp_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('campground/<int:facilityID>/<int:index>', views.campground, name='campground')
]