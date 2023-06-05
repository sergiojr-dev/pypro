from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Olá django data 05-06-23')