from django.shortcuts import render

# Create your views here.

def index(request):
        return render(request, 'index.html')

def contact(request):
        return render(request, 'contato.html')

def layout_static(request):
        return render(request, 'layout-static.html')

def layout_sidenav(request):
        return render(request, 'layout-sidenav-light.html')