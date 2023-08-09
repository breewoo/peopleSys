from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from . import forms


def HOMEPage(request):
    peopleList = models.People.objects.all()
    return render(request, './people/home.html', {'peopleList':peopleList})

def CREATEPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        position = request.POST.get('position')
        language = request.POST.getlist('language')
        salary = request.POST.get('salary')
        NEW_PEOPLE = models.People.objects.create(
                name = name,
                gender = gender,
                age = age,
                position = position,
                language = language,
                salary = salary
        )
        NEW_PEOPLE.save()
        return HttpResponseRedirect('/')
    return render(request, './people/create.html')


def EDITPage(request, id):
    peopleUnit = models.People.objects.get(id=id)
    return render(request, './people/edit.html',{'peopleUnit':peopleUnit})


def UPDATEPage(request, id):
    peopleUnit = models.People.objects.get(id=id)
    # form = forms.peopleform(request.POST, instance=peopleUnit)
    # if form.is_valid:
    #     form.save()
    #     peopleUnit = models.People.objects.all()
    #     return HttpResponseRedirect('/')
    if request.method == 'POST':
        peopleUnit.name = request.POST.get('name')
        peopleUnit.gender = request.POST.get('gender')
        peopleUnit.age = request.POST.get('age')
        peopleUnit.position = request.POST.get('position')
        peopleUnit.language = request.POST.getlist('language')
        peopleUnit.salary = request.POST.get('salary')
        peopleUnit.save()
        return HttpResponseRedirect('/')
       

def DELETEPage(request, pk):
    peopleUnit = models.People.objects.get(id=pk)
    peopleUnit.delete()
    return HttpResponseRedirect('/')
