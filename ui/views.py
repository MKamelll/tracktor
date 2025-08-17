from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return login(request)
    return dashboard(request)


def signup(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="ui/auth/signup.djhtml")


def login(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="ui/auth/login.djhtml")


def dashboard(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="ui/dashboard/home.djhtml")


def tvshow(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="ui/tvshow/details.djhtml")
