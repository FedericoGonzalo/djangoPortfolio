from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return render(request,"home.html")

def expe(request):
    return HttpResponse(request,"experiencias.html")

def proye(request):
    return HttpResponse(request,"proyecto.html")


def contacto(request):
    return HttpResponse(request,"contacto.html")