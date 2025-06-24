from django.shortcuts import render, redirect
from .models import Parroquia, Barrio
from .forms import ParroquiaForm, BarrioForm
# Create your views here.
def parroquias_y_barrios(request):
    parroquias = Parroquia.objects.prefetch_related('barrio_set').all()
    return render(request, 'ordenamiento/parroquias_y_barrios.html', {'parroquias': parroquias})

def lista_barrios(request):
    barrios = Barrio.objects.select_related('parroquia').all()
    return render(request, 'ordenamiento/lista_barrios.html', {'barrios': barrios})

def crear_parroquia(request):
    if request.method == 'POST':
        form = ParroquiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parroquias_y_barrios')
    else:
        form = ParroquiaForm()
    return render(request, 'ordenamiento/crear_parroquia.html', {'form': form})

def crear_barrio(request):
    if request.method == 'POST':
        form = BarrioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_barrios')
    else:
        form = BarrioForm()
    return render(request, 'ordenamiento/crear_barrio.html', {'form': form})

def index(request):
    parroquias = Parroquia.objects.all()
    barrios = Barrio.objects.all()
    return render(request, 'index.html', {
        'parroquias': parroquias,
        'barrios': barrios
    })
