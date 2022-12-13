from django.urls import path

from .views import SignUpView, session_login

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('login/', session_login, name="login")
]