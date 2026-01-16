from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("page/<slug:slug>/", views.static_page, name="static_page"),
]
