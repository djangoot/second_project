from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def timeinfo(request):
    date=datetime.datetime.now()
    msg='<h1>Hello friends Good Evening!!!</h1></hr><hr>'
    msg=msg+'<h1>Now server time is:'+str(date)+'</h1>'
    return HttpResponse(msg)
