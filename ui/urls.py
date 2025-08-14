from django.urls import path

from ui import views

urlpatterns = [
    path("", view=views.index, name="index"),
]
