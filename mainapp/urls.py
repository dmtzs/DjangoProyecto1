from django.urls import path
import mainapp.views

urlpatterns= [
    path("", mainapp.views.index, name="index"),
    path("Inicio/", mainapp.views.index, name="inicio")
]