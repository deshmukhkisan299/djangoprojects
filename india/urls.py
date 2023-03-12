from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def header(r):
    return render(r, 'index.html')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("men/", include('men.urls')),
    path("women/", include('women.urls')),
    path("", header),
    path("login/", include('login.urls')),
    # path("signup/", include('signup.urls')),
    path("accounts/", include('django.contrib.auth.urls'))
]
