from django.shortcuts import render, redirect
from . import data_fun
from .models import StoryCost, Player
from .logic import model_fun
from .forms import StoryCostForm, PlayerForm


# Create your views here.
def index(request):
    data = data_fun.load_data()
    player = Player.objects.all()
    me = Player.objects.get(id=1)  # или по username и т.д.

    total = round((
             int(me.orundum)
             + int(me.originium) * 180
             + int(me.tickets) * 600
            ) / 600, 2)

    content = {'data': data, 'player': player, 'total': total}
    return render(request, 'main/index.html', content)


def create_model_data(request):
    data = StoryCost.objects.all()
    # model_fun.update()
    model_fun.create()
    # model_fun.delete_all()
    # model_fun.delete()
    return render(request, 'main/model_test.html', {'data': data})


def edit_stories(request):
    stories = StoryCost.objects.all()

    if request.method == 'POST':
        instance = StoryCost.objects.get(pk=request.POST.get('id'))
        form = StoryCostForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('f')  # замените на ваш URL

    # передаём формы вместе с объектами
    form_list = [(item, StoryCostForm(instance=item)) for item in stories]
    return render(request, 'main/forms_for_model.html', {'form_list': form_list, 'data': stories})


def edit_player(request):
    player = Player.objects.all()

    if request.method == 'POST':
        instance = Player.objects.get(pk=request.POST.get('id'))
        form = PlayerForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('index')

    form_list = [(item, PlayerForm(instance=item)) for item in player]
    return render(request, 'main/player_form.html', {'form_list': form_list, 'player': player})