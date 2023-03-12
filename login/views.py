from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import logintable

# Create your views here.
def login_page_view(r):

    return render(r, 'registration/login.html')

# def login_page_view2(r):
#     return render(r, 'registration/login.html', {'Name':'Krishnat'})
