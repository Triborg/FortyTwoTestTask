from django.db import models


# Create your models here.
class Persons(models.Model):
    name = models.CharField(max_length=21, unique=True)
    last_name = models.CharField(max_length=21)
    date_birth = models.DateField()
    bio = models.TextField(verbose_name='biography')

    def __str__(self):
        return "{0} {1}".format(self.name, self.last_name)


class PersonsContacts(models.Model):
    name = models.ForeignKey(Persons)
    email = models.EmailField(unique=True, verbose_name='email')
    jabber_JID = models.EmailField(unique=True)
    skype = models.CharField(max_length=21)
    twitter = models.CharField(max_length=21)
    tel = models.CharField(max_length=21)
