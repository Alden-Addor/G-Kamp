from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    session_key = models.CharField(max_length=200) # Saves session key to allow the session data the user has created is recallable.

    def __str__(self):
        return self.username
    
