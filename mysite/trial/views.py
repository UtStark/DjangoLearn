from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the trials index.")


def home(request):
    return HttpResponse(" You're at the home.")