from django.http import HttpResponse
from django.shortcuts import render

from demoapp.models import Team


def home(request):
   obj=Team.objects.all()
   return render(request,"index.html",{'result':obj})
