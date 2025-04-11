from django.shortcuts import render
from . import data_fun
from .models import StoryCost
from .logic import model_fun


# Create your views here.
def index(request):
    data = data_fun.load_data()
    content = {'data': data}
    return render(request, 'main/index.html', content)


def create_model_data(request):
    data = StoryCost.objects.all()
    model_fun.update()
    # model_fun.create()
    # model_fun.delete_all()
    # model_fun.delete()
    return render(request, 'main/model_test.html', {'data': data})
