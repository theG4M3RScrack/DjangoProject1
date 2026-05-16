from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import *


class AllToDos(ListView):
    model = ToDoItem
    template_name = "todo/index.html"

def index(request):
    return render(request, 'todo/index.html')
def about(request):
    return render(request, "todo/about.html")
def portfolio(request):

    proyectos = Proyectos.objects.all()

    return render(request, 'todo/portfolio.html', {
        'proyectos': proyectos
    })
def contact(request):

    personas = Personas.objects.all()

    return render(request, 'todo/contact.html', {
        'personas': personas
    })
def test(request):

    personas = Personas.objects.all()

    return render(request, 'todo/test.html', {
        'personas': personas
    })
