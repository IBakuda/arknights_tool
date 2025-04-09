from django.shortcuts import render
from . import data_fun


# Create your views here.
def index(request):
    data = data_fun.load_data()
    content = {'data': data}
    return render(request, 'main/index.html', content)