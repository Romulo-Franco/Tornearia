from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("ola mundo, meu aplicativo servico esta funcionando!")