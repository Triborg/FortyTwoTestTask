from django.contrib import admin
from apps.hello.models import Persons, PersonsContacts
admin.autodiscover()


class PersonsAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'date_birth', 'bio')


class PersonsContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'jabber_JID', 'skype', 'tel')


admin.site.register(Persons, PersonsAdmin)
admin.site.register(PersonsContacts, PersonsContactsAdmin)
