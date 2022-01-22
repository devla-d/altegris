from django.shortcuts import render





def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')



def pricing(request):
    return render(request, 'pricing.html')


def services(request):
    return render(request, 'services.html')


def support(request):
    return render(request, 'support.html')
