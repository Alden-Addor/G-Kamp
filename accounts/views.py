from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sessions.backends.db import SessionStore

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

'''
Created a override to Django's base login.
This allows the user's session data to be restored everytime they login.
Restores session data even if Cookies has been cleared.
'''
def session_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            # session = SessionStore(session_key = user.session_key)
            # request.session = session
            return HttpResponseRedirect(reverse_lazy('home'))
        else:
            return HttpResponseRedirect(reverse_lazy('signup'))
    else:
        return render(request, 'registration/login.html')