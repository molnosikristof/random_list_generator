from __future__ import unicode_literals
import random
from .forms import NameForm
from .models import RandomList
from django.http import HttpResponseRedirect

# import Http Response from django 
from django.shortcuts import render 

# create a function 
def index_view(request): 

    lists = []
    for one_list in RandomList.objects.all():
        lists.append(one_list.list_name)
    return render(request, "index.html", {'lists': lists}) 

def mix_view(request, list_name): 

    list_content= str(RandomList.objects.get(list_name=list_name).list_content)
    random_list = random.sample(list_content.split(),len(list_content.split()))
    random_string = ' '.join(map(str, random_list))
    RandomList.objects.filter(list_name=list_name).update(list_content=random_string)

    return HttpResponseRedirect('/list/' + list_name)
    
def list_view(request, list_name): 

    return render(request, "list.html", {'list': RandomList.objects.get(list_name=list_name).list_content.split(), 'list_name': RandomList.objects.get(list_name=list_name).list_name}) 

def list_form_view(request):

    list_content = ''
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():

            list_to_save = RandomList(list_name=str(form.cleaned_data['list_name']), list_content = str(form.cleaned_data['list_content']))
            if not RandomList.objects.filter(list_name=form.cleaned_data['list_name']).exists():
                list_to_save.save()

            else:
                RandomList.objects.filter(list_name=form.cleaned_data['list_name']).update(list_content=form.cleaned_data['list_content'])
            return render(request, "list_form.html", {'form': form,'list' : form.cleaned_data['list_content'].split()})

    else:
        form = NameForm()

    return render(request, "list_form.html", {'form': form,'list' : list_content.split()})
