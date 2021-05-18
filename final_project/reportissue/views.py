from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . import models

# Create your views here.
class CreateRepport(LoginRequiredMixin, generic.CreateView):
    fields = ('name','message')
    model = models.ReportIssue
