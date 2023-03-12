from django.contrib import admin
from django.urls import path
from sign_up import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("form/", views.zomato_form),
    path("api_getpost/", views.zomatoapi_cls.as_view()),
    path("updatedelete_api/<int:pk>", views.updatedelete_api.as_view()),
]
