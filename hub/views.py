from django.shortcuts import render

def hub(request):
    return render(request, 'hub.html')

def bedroom(request):
    return render(request, 'bedroom.html')

def bathroom(request):
    return render(request, 'bathroom.html')

def kidsroom(request):
    return render(request, 'kidsroom.html')

def kitchen(request):
    return render(request, 'kitchen.html')

def livingroom(request):
    return render(request, 'livingroom.html')

def office(request):
    return render(request, 'office.html')

def poojaroom(request):
    return render(request, 'poojaroom.html')

def tv(request):
    return render(request, 'tv.html')
