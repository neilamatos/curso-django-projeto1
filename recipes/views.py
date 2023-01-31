from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Neila Matos'
    })


def contato(request):
    return render(request, 'temp.html')


def sobre(request):
    return HttpResponse('SOBRE 1')
