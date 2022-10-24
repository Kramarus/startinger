from django.shortcuts import render

# Create your views here.
def render_home(request):
    return render(request, 'landing/home.html', {"navbar": "home"})

def render_services(request):
    return render(request, 'landing/services.html', {"navbar": "services"})

def render_about(request):
    return render(request, 'landing/about.html', {"navbar": "about"})

def render_contact(request):
    return render(request, 'landing/contact.html', {"navbar": "contact"})

def render_quote(request):
    return render(request, 'landing/quote.html')