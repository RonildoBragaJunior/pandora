from django.test import Client, TestCase
from django.urls import resolve, reverse

from pandora.models import Company, People
from pandora.services.welcome import WelcomeService


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.uuid = 'f9a8a024-3a74-11ed-a261-0242ac120002'

    @classmethod
    def setUpTestData(cls):
        WelcomeService().load_pandora_citzens()

    def test_company_employees_status_200(self):
        guid = Company.objects.first().guid
        response = self.client.get(reverse('company_employees', args=[guid]))
        self.assertEqual(response.status_code, 200)

    def test_company_employees_status_404(self):
        response = self.client.get(
            reverse('company_employees', args=[self.uuid]))
        self.assertEqual(response.status_code, 404)

    def test_people_friends_in_common_200(self):
        response = self.client.get(
            reverse('people_friends_in_common', args=[People.objects.first().guid, People.objects.last().guid]))
        self.assertEqual(response.status_code, 200)

    def test_people_friends_in_common_404(self):
        response = self.client.get(
            reverse('people_friends_in_common', args=[self.uuid, self.uuid]))
        self.assertEqual(response.status_code, 404)

    def test_people_favourite_fruit_vegetables_200(self):
        response = self.client.get(
            reverse('people_favourite_fruit_vegetables', args=[People.objects.first().guid]))
        self.assertEqual(response.status_code, 200)

    def test_people_favourite_fruit_vegetables_404(self):
        response = self.client.get(
            reverse('people_favourite_fruit_vegetables', args=[self.uuid]))
        self.assertEqual(response.status_code, 404)
    

    # def test_people_friends_in_common_1(self):
    #     response = self.client.get(
    #         reverse('people_friends_in_common', args=[0, 1]))
    #     self.assertJSONEqual(
    #         str(response.content, encoding='utf8'),
    #         {"first_person": {"name": "Carmella Lambert", "age": 61, "address": "628 Sumner Place, Sperryville, American Samoa, 9819", "phone": "+1 (910) 567-3630"}, "second_person": {"name": "Decker Mckenzie", "age": 60, "address": "492 Stockton Street, Lawrence, Guam, 4854", "phone": "+1 (893) 587-3311"}, "common_friends": [
    #             {"index": 4, "name": "Mindy Beasley", "age": 62, "address": "628 Brevoort Place, Bellamy, Kansas, 2696", "phone": "+1 (862) 503-2197", "eye_color": "brown", "has_died": False}]}
    #     )

    # def test_people_favourite_fruit_vegetables(self):
    #     response = self.client.get(
    #         reverse('people_favourite_fruit_vegetables', args=[1]))
    #     self.assertJSONEqual(
    #         str(response.content, encoding='utf8'),
    #         {"username": "Decker Mckenzie", "age": 60, "fruits": [
    #             "cucumber"], "vegetables": ["carrot", "celery"]}
    #     )
