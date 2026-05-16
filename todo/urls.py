from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.AllToDos.as_view(), name="index"),

    path("sobre", views.about, name="about"),

    path("portafolio", views.portfolio, name="portfolio"),

    path("contactos", views.    contact, name="contact"),

    path("test", views.test, name="test")

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)