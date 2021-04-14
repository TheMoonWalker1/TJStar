from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')


def speaker(request):
    return render(request, 'speaker.html')


def contact(request):
    return render(request, 'contact.html')

def event(request):
    return render(request, 'event.html')