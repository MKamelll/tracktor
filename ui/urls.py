from django.urls import path

from ui import views

urlpatterns = [
    path("tvshow/", view=views.tvshow, name="tvshow"),
    path("dashboard/", view=views.dashboard, name="dashboard"),
    path("login/", view=views.login, name="login"),
    path("signup/", view=views.signup, name="signup"),
    path("", view=views.index, name="index"),
]
