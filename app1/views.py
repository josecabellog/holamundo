from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def hola_mundo (request):

    return render (request, 'adioschao.html')

class adios_mundo1(TemplateView):
    template_name = 'adioschao.html'
