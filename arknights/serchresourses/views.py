from django.shortcuts import render
from .forms import SerchResoursesForm
from .serchdata import serchoperator

# Create your views here.

def index(request):
    data = []
    if request.method == 'POST':
        form = SerchResoursesForm(request.POST)
        if form.is_valid():
            operator_name = form.cleaned_data
            data = serchoperator(operator_name['operator_name'])


    form = SerchResoursesForm()

    context = {
        'form': form,
        'data': data,
    }
    return render(request, 'serchresourses/res_home.html', context)


