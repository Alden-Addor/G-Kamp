from django.urls import path
from . import views

app_name = 'g_kamp_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('campground/<int:facilityID>/<int:index>', views.campground, name='campground'),
    path('getsessiondata/', views.getSessionData, name='getsessiondata'),
    path('save/', views.savedCampground, name='saved'),
    path('profile/', views.profile, name='profile'),
    path('pro_search/<int:facilityID>/', views.pro_search, name='pro_search'),
    path('campsites/<int:facilityID>/', views.campsites, name='campsites')
]