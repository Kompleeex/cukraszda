from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
from django.db.models import Q
from .models import *
from .forms import *


def index(request):
    edessegek = Edesseg.objects.all()
    context = {
        "edessegek" : edessegek 
    }
    return render(request, "index.html", context = context)


def feltolt(request):
    edessegek = Edesseg.objects.all()
    form = EdessegForm(request.POST or None)
    if(request.method == "POST"):
        if(form.is_valid()):
            form.save()
            return redirect(index)
    else:
        form = EdessegForm()
    context = {
        "form" : form,
        "edessegek" : edessegek
    }
    return render (request, "feltolt.html", context = context)


def modosit(request, id):
    edesseg = get_object_or_404(Edesseg, pk = id)
    form = EdessegForm(request.POST or None, instance = edesseg)
    if(request.method == "POST"):
        if(form.is_valid()):
            form.save()
            return redirect(index)
    context = {
        "form" : form,
    }
    return render (request, "feltolt.html", context = context)

def torol(request, id):
    edesseg = get_object_or_404(Edesseg, pk = id)
    edesseg.delete()

    return redirect(index)
