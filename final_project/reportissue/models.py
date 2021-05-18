from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class ReportIssue(models.Model):
    name = models.CharField(max_length=250, verbose_name='name')
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('index')
