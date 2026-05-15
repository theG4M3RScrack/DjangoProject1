from django.urls import path
from . import views

urlpatterns = [
    path("", views.AllToDos.as_view(), name="index"),
    path("sobre", views.about, name="about"),
    path("portafolio", views.portfolio, name="portfolio"),
    path("contactos", views.contact, name="contact"),

    path("anotherclass", views.anotherclass, name="anotherclass")

]