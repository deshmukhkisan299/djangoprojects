from django.contrib import admin
from django.urls import path
from women import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", views.womenhome),
    path("form/", views.women_form),
    path("data/", views.womendata),
    path("update/<id>/", views.women_update),
    path("delete/<id>/", views.women_delete),
]
