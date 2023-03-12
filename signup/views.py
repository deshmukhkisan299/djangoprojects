from django.shortcuts import render,HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
# from .forms import signup_form
# from django.contrib.auth.hashers import make_password
#
# # Create your views here.
# def signup_view(r):
#     if r.method=="POST":
#         password = r.POST['password']
#         confirm_password = r.POST['password']
#         form = signup_form(r.POST)
#         print(form.password)
#         print(form.confirm_password)
#         if form.is_valid():
#             if password == confirm_password:
#                 abc = form.save(commit=False)
#                 # abc.set_password(abc.password)
#                 abc.password =make_password(password)
#                 abc.save()
#                 HttpResponseRedirect('')
#             else:
#                 return HttpResponse("Password Error")
#         """
#         password confirmation not working
#         """
#     return render(r, 'registration/signup.html', {'form':signup_form})
