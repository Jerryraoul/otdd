from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
import requests
# Create your views here.


def homePage(request):
    return render(request, 'restaurant/index.html')


class UserLogin(LoginView):
    template_name = 'restaurant/Login.html'


class UserLogout(LogoutView):
    template_name = 'restaurant/Logout.html'
    next_page = 'home'


@login_required(login_url='Login')
def WeatherApi(request):
    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todos = response.json()
    return render(request, "restaurant/weatherapi.html", {"todos": todos})


@login_required(login_url='Login')
def Ipsum(request):
    url = "https://rapidapi.p.rapidapi.com/"
    querystring = {"format": "html", "words": "30", "paragraphs": "3"}
    headers = {
        'x-rapidapi-host': "alexnormand-dino-ipsum.p.rapidapi.com",
        'x-rapidapi-key': "28ee4a2d1cmsh22d5c5e7e120dbep186fffjsn5cad0e3a4596"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return render(request, "restaurant/ipsum.html",  {"text": response.text})


def Iplocation(request):
    url = "https://rapidapi.p.rapidapi.com/WebAI/WFIPLocation"
    querystring = {"lng": "en", "addr": "82.200.89.143"}
    headers = {
        'x-rapidapi-host': "ip-location3.p.rapidapi.com",
        'x-rapidapi-key': "28ee4a2d1cmsh22d5c5e7e120dbep186fffjsn5cad0e3a4596"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return render(request, "restaurant/iplocation.html",  {"text": response.text})
