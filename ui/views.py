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
    context = {
        "name": "Breaking Bad",
        "poster_path": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOcWkpWG_NRrU2M8-WB8EbEcJk7smhdrY1eO0ttKXm0bo2ooOEWxk3zBSbsFrSgSJh2OEKOQ",
        "overview": "Walter White, a chemistry teacher, discovers that he has cancer and decides to get into the meth-making business to repay his medical debts. His priorities begin to change when he partners with Jesse.",
        "seasons": [1, 2, 3, 4, 5],
    }
    return render(
        request=request, template_name="ui/tvshow/details.djhtml", context=context
    )
