from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("fuck off")


def login(req: HttpRequest) -> HttpResponse:
    return render(request=req, template_name="ui/auth/login.djhtml")
