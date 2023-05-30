from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "Fooldal"),
    path("feltolt/", views.feltolt, name = "feltolt"),
    path("modositas/<int:id>", views.modosit, name = "modosit"),

    path("torol/<int:id>", views.torol, name = "torol")
]
