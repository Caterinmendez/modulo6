from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def index(request):
    return render(request,"creaciones_multicolor/index.html",{})

def mostrar_usuarios(request):
    lista_usuarios = CustomUser.objects.all()
    return render(request, "creaciones_multicolor/usuarios.html",{"lista_usuarios": lista_usuarios})