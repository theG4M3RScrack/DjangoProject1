from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import ToDoItem, Persona


class AllToDos(ListView):
    model = ToDoItem
    template_name = "todo/index.html"

def index(request):
    personas = Persona.objects.all()

    return render(request, 'todo/index.html', {
        'persona': Persona
    })
def index(request):
    return render(request, 'todo/index.html')
def about(request):
    return render(request, "todo/about.html")
def portfolio(request):
    return render(request, "todo/portfolio.html")
def contact(request):
    return render(request, "todo/contact.html")

def anotherclass(request):
    return render(request,"todo/anotherclass.html")
