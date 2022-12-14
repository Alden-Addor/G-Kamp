from django.db import models

class Saved(models.Model):
    user = models.ForeignKey('accounts.CustomUser', related_name="saved", on_delete=models.CASCADE)
    saved_date = models.DateTimeField(auto_now_add=True)
    campground = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.campground

    class Meta:
        ordering = ['-saved_date']
    