from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'home.html')
def demo(request):
    return render(request,'demo.html')

def login(request):
    return render(request,'login.html')