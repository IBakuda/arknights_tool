from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from .models import StoryCost, Player
from .logic import model_fun
from .forms import StoryCostForm, PlayerForm
from rest_framework import generics

from .serialaizers import StoryCostSerialaizer


# Create your views here.
def index(request):
    data = StoryCost.objects.all().order_by('id', 'story_type')
    model_fun.chapter_clear(data)
    player = Player.objects.all()
    me = Player.objects.get(id=1)  # или по username и т.д.

    total = round((
             int(me.orundum)
             + int(me.originium) * 180
             + int(me.tickets) * 600
            ) / 600, 2)

    all_originate = sum(item.total for item in data)
    normal = sum(item.normal for item in data)
    challenge = sum(item.challenge for item in data)

    last = all_originate - normal - challenge

    content = {'data': data, 'player': player, 'total': total, 'last': last}
    return render(request, 'main/index.html', content)


def create_model_data(request):
    data = StoryCost.objects.all()
    # model_fun.update()
    model_fun.create()
    # model_fun.delete_all()
    # model_fun.delete()
    return render(request, 'main/model_test.html', {'data': data})


def edit_stories(request):
    StoryCostFormSet = modelformset_factory(StoryCost, form=StoryCostForm, extra=0)

    if request.method == 'POST':
        formset = StoryCostFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('index')  # куда перекидывать после сохранения

    formset = StoryCostFormSet(queryset=StoryCost.objects.all())
    return render(request, 'main/forms_for_model.html', {'formset': formset})


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


class StoryCostAPIView(generics.ListAPIView):
    queryset = StoryCost.objects.all()
    serializer_class = StoryCostSerialaizer


