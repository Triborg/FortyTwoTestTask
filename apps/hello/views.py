from django.shortcuts import render
from apps.hello.models import Persons, PersonsContacts


def home(request):
    person_list = Persons.objects.all()
    contacts_list = PersonsContacts.objects.all()
    return render(request, 'home.html', locals())
