from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    template_name = 'core/home.html'
    context = {}
    return render(request, template_name, context)
    # return HttpResponse('home')