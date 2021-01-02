from django.urls import path
import pages.views

urlpatterns=[
    path("pagina/<str:slug>", pages.views.page, name="page")
]