from django.contrib import admin
from django.urls import path, include
from signup import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.signup_view),
]
