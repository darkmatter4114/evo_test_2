import json
from datetime import datetime
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from .forms import NameForm, FullUserForm
from .models import User, FullUser


def index(request):
    form = NameForm()
    return render(request, 'main.html', {'form': form})


def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            if User.objects.filter(name=name).exists():
                messages.info(request, 'Вже бачилися {}'.format(name))
                # return HttpResponseRedirect(reverse('main'))
                form = NameForm()
            else:
                post = form.save()
                # post.save()
                messages.info(request, 'Привіт {}'.format(name))
                form = NameForm()
    else:
        form = NameForm()
    return render(request, 'main.html', {'form': form})


def get_full_name(request):
    if request.method == "POST":
        form = FullUserForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            lastName = form.cleaned_data['lastName']
            email = form.cleaned_data['email']
            if FullUser.objects.filter(name=name).exists() or FullUser.objects.filter(
                    lastName=lastName).exists() or FullUser.objects.filter(email=email).exists():
                # FullUser.last_login = datetime.now()
                messages.info(request, 'Вже бачилися {}'.format(name))
                # return HttpResponseRedirect(reverse('main'))
                form = FullUserForm()
            else:
                post = form.save()
                # post.save()
                messages.info(request, 'Привіт {}'.format(name))
                form = FullUserForm()
    else:
        form = FullUserForm()
    return render(request, 'main2.html', {'form': form})


def get_all(request):
    str = ''
    if request.method == 'GET':
        user = User.objects.all()
        for names in user:
            str += names.name + ' '
        return HttpResponse(str)


def get_all_v2(request):
    # str = ''
    if request.method == 'GET':
        data = objTOjson(FullUser)
        return JsonResponse(data, content_type='json', safe=False)


def objTOjson(model):
    z = 0
    d = []
    data = serializers.serialize('json', model.objects.all())
    struct = json.loads(data)
    while z < struct.__len__():
        d.append(json.loads(json.dumps(struct[z]['fields'])))
        z += 1
    return (d)
