from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    home = loader.get_template("home.html")
    return HttpResponse(home.render())

def categories(request):
    return HttpResponse("Ini halaman categories")

def products_in_category(request):
    return HttpResponse("Ini halaman di dalam category")

def produt(request):
    return HttpResponse("ini adalah halaman product")

def checkout(request):
    return HttpResponse("ini adalah halaman checkout")

def user(request):
    return HttpResponse("ini adalah halaman user")