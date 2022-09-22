from django.test import Client, TestCase
from django.urls import resolve, reverse

from pandora.models import Company, People
from pandora.services.welcome import WelcomeService


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    @classmethod
    def setUpTestData(cls):
        WelcomeService().load_pandora_citzens()

    def test_company_employees_status_200(self):
        response = self.client.get(reverse('company_employees', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_company_employees_status_404(self):
        response = self.client.get(
            reverse('company_employees', args=[1000000000]))
        self.assertEqual(response.status_code, 404)

    def test_people_friends_in_common_200(self):
        response = self.client.get(
            reverse('people_friends_in_common', args=[1, 2]))
        self.assertEqual(response.status_code, 200)

    def test_people_friends_in_common_404(self):
        response = self.client.get(
            reverse('people_friends_in_common', args=[1000000000, 1]))
        self.assertEqual(response.status_code, 404)

    def test_people_favourite_fruit_vegetables_200(self):
        response = self.client.get(
            reverse('people_favourite_fruit_vegetables', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_people_favourite_fruit_vegetables_404(self):
        response = self.client.get(
            reverse('people_favourite_fruit_vegetables', args=[1000000000]))
        self.assertEqual(response.status_code, 404)

    def test_company_employees(self):
        response = self.client.get(reverse('company_employees', args=[1]))
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {"company_index": 1, "company_name": "PERMADYNE", "company_employees": [{"index": 289, "name": "Frost Foley", "age": 22, "address": "824 Clark Street, Utting, New Mexico, 3994", "phone": "+1 (987) 436-3916"}, {"index": 580, "name": "Luna Rodgers", "age": 56, "address": "430 Frank Court, Camino, American Samoa, 2134", "phone": "+1 (889) 544-3275"}, {"index": 670, "name": "Boyer Raymond", "age": 20, "address": "326 Times Placez, Cumminsville, Montana, 2703", "phone": "+1 (867) 458-3241"}, {"index": 714, "name": "Solomon Cooke", "age": 51, "address": "340 Granite Street, Cazadero, Colorado, 1597", "phone": "+1 (844) 460-3877"}, {
                "index": 828, "name": "Walter Avery", "age": 35, "address": "797 Vandervoort Place, Wheaton, Kentucky, 1051", "phone": "+1 (992) 532-3748"}, {"index": 928, "name": "Hester Malone", "age": 38, "address": "928 Seaview Court, Jacksonburg, American Samoa, 4161", "phone": "+1 (847) 435-3662"}, {"index": 985, "name": "Arlene Erickson", "age": 46, "address": "821 Coventry Road, Manchester, New Mexico, 2751", "phone": "+1 (878) 521-3781"}]}
        )

    def test_people_friends_in_common_1(self):
        response = self.client.get(
            reverse('people_friends_in_common', args=[0, 1]))
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {"first_person": {"name": "Carmella Lambert", "age": 61, "address": "628 Sumner Place, Sperryville, American Samoa, 9819", "phone": "+1 (910) 567-3630"}, "second_person": {"name": "Decker Mckenzie", "age": 60, "address": "492 Stockton Street, Lawrence, Guam, 4854", "phone": "+1 (893) 587-3311"}, "common_friends": [
                {"index": 4, "name": "Mindy Beasley", "age": 62, "address": "628 Brevoort Place, Bellamy, Kansas, 2696", "phone": "+1 (862) 503-2197", "eye_color": "brown", "has_died": False}]}
        )

    def test_people_favourite_fruit_vegetables(self):
        response = self.client.get(
            reverse('people_favourite_fruit_vegetables', args=[1]))
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {"username": "Decker Mckenzie", "age": 60, "fruits": [
                "cucumber"], "vegetables": ["carrot", "celery"]}
        )
