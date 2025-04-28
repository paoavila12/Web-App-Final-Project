from django.shortcuts import render
from .models import Record

# Create your views here.

def home(request):
    records = Record.object.all()
    return render(request,"home.html", {'records': records})