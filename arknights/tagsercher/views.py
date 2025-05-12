from django.shortcuts import render, redirect
from django.forms import modelformset_factory, formset_factory

from .forms import AddOperatorForm, TagChouseForm
from .models import Operator


# Create your views here.
def tagsercher_view(request):
    tag = {}
    if request.method == 'POST':
        form = TagChouseForm(request.POST)
        if form.is_valid():
            tag = form.cleaned_data

    #tag = set(map(lambda item: item[0], filter(lambda item: item[1] == True, tag.items())))
    tag = {key for key, value in tag.items() if value}
    full_matches = []
    partial_matches = []

    for operator in Operator.objects.all():
        operator_tags = {t.strip() for t in operator.tag.split(',')}

        # Полное совпадение: все выбранные теги содержатся у оператора
        if tag.issubset(operator_tags):
            full_matches.append(operator)
        # Частичное совпадение: хотя бы один тег совпадает
        if tag & operator_tags:
            partial_matches.append(operator)

    form = TagChouseForm()
    context = {
        'full_matches': full_matches,
        'partial_matches': partial_matches,
        'form': form,
        'class_fields': ['guard', 'sniper', 'defender', 'medic', 'suporter', 'caster', 'specialist', 'vanguard'],
        'position_fields': ['melee', 'ranged'],
        'qualification_fields': ['starter', 'senior_operator', 'top_operator'],
        'affix_fields': ['crowd_control', 'nuker', 'healing', 'support', 'dp_recovery', 'dps', 'aoe', 'defense', 'slow',
                         'debuff', 'fast_redeploy', 'shift', 'summon', 'robot', 'elemental'],
        'rarity_fields': ['all', 'six_star', 'five_star', 'four_star', 'three_star', 'two_star', 'one_star']
    }

    return render(request, 'tagsercher/tag_index.html', context)


def add_operator_form_view(request):
    if request.method == 'POST':
        form = AddOperatorForm(request.POST)
        if form.is_valid():
            Operator.objects.create(name = form.cleaned_data['name'],
                                    tag = form.cleaned_data['tag'],
                                    rarity = form.cleaned_data['rarity'],)
            return redirect('addoperator')

    form = AddOperatorForm()

    context = {'form': form}
    return render(request, 'tagsercher/add_operator_form.html', context)


def tag_chouse(request):
    if request.method == 'POST':
        form = TagChouseForm(request.POST)
        if form.is_valid():
            redirect('tagsercher')

    form = TagChouseForm()
    print(form)
    return form


def operator_edit_view(request):
    OperatorFormSet = formset_factory(AddOperatorForm, extra=0)

    # получаем данные из модели
    operators = Operator.objects.all()
    initial_data = [{'name': op.name, 'tag': op.tag, 'rarity': op.rarity} for op in operators]

    if request.method == 'POST':
        formset = OperatorFormSet(request.POST)
        if formset.is_valid():
            for form, operator in zip(formset.cleaned_data, operators):
                operator.name = form['name']
                operator.tag = form['tag']
                operator.rarity = form['rarity']
                operator.save()
            return redirect('tagsercher')

    formset = OperatorFormSet(initial=initial_data)
    return render(request, 'tagsercher/operator_edit_form.html', {'formset': formset})
