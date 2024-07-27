from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

from .models import MenuItem

menu = [{'title': "О сайте", 'url_name': 'about'}]

# Create your views here.
def index(request):
    menu = MenuItem

    data = {
        'title': 'Главная страница',
        'menu': 'menu'
    }
    return render(request, 'menu/draw_menu.html', context=data)

def about(request):
    return render(request, 'base.html', {'title': 'О сайте', 'menu': menu})
