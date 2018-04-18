from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'console/admin-index.html')


def user(request):
    return render(request, 'console/admin-user.html')


def help(request):
    return render(request, 'console/admin-help.html')


def gallery(request):
    return render(request, 'console/admin-gallery.html')


def table(request):
    return render(request, 'console/admin-table.html')


def form(request):
    return render(request, 'console/admin-form.html')

def upload_image(request):
    pass
