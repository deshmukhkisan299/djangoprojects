from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.login_page_view),
    # path("2/", views.login_page_view2),
]
