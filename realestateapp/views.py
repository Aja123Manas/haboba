from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def agents(request):
    return render(request, 'agent-single.html')


def grid(request):
    return render(request, 'agents-grid.html')

def blog(request):
    return render(request, 'blog-grid.html')

def single(request):
    return render(request, 'blog-single.html')

def contact(request):
    return render(request, 'contact.html')

def property(request):
    return render(request, 'property-grid.html')
def properties(request):
    return render(request, 'property-single.html')

