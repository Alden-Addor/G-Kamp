from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.sessions.backends.db import SessionStore
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
    
    # Over rides and adds on session key into the users saved information at the time of signup.
    def save(self, commit=True):
        user = super().save(commit=False)
        user_session = SessionStore()
        user_session.create()
        user.session_key = user_session.session_key
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')