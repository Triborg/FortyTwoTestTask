from django.test import TestCase
from apps.hello.models import Persons, PersonsContacts
from django.core.urlresolvers import reverse
from django.test.client import Client
#from django.contrib.contenttypes.models import ContentType
# test model
class TestModel(TestCase):
    """ Tests for the Persons and PersonsContacts detail view """
    def setUp(self):
        self.person = Persons.objects.create(
            name="Vycheslav",
            last_name="Oreshko",
            date_birth="1980-07-14",
            bio="I was born on 14.07.1980 in Navoiy, Uzbekistan. ", )

        self.contacts = PersonsContacts.objects.create(
            name=self.person,
            email="ardlion108@gmail.com",
            jabber_JID="triborg@jabber.ua",
            skype="oreshko_slava",
            tel="(098)-784-23-81"
        )
        self.client = Client()
        #self.person_type = ContentType.objects.get(app_label="apps.hello", model="persons")

    def test_model(self):
        self.assertTrue(isinstance(self.person, Persons))
        self.assertTrue(isinstance(self.contacts, PersonsContacts))

    def test_view(self):
        url = reverse("apps.hello.views.home")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')

    def test_admin(self):
        resp = self.client.get(reverse('admin:persons_persons_add'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['persons'].pk, 1)
        self.assertEqual(resp.context['persons'].last_name, 'Oreshko')

        # Ensure that non-existent persons throw a 404.
        resp_no_one = self.client.get('/hello/2/')
        self.assertEqual(resp_no_one.status_code, 404)

    def tearDown(self):
        self.client.logout()


if __name__ == "__main__":
    TestCase.main()
