import uuid

from django.db import models

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

FOOD_TYPE = (
    ('F', 'Fruit'),
    ('V', 'Vegetable'),
    ('U', 'Unknown'),
)


class Company(models.Model):
    index = models.BigAutoField(primary_key=True)
    guid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=100)


class Tag(models.Model):
    name = models.CharField(primary_key=True, max_length=100)


class Food(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    food_type = models.CharField(max_length=1, default='U', choices=FOOD_TYPE)


class People(models.Model):
    index = models.BigAutoField(primary_key=True)
    guid = models.UUIDField(default=uuid.uuid4)
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    favourite_food = models.ManyToManyField(Food)
    friends = models.JSONField(blank=True, null=True)
    has_died = models.BooleanField(default=None, blank=True, null=True)
    balance = models.DecimalField(max_digits=6, decimal_places=2, default=None, blank=True, null=True)
    picture = models.CharField(max_length=100, default=None, blank=True, null=True)
    age = models.IntegerField(default=None, blank=True, null=True)
    eye_color = models.CharField(max_length=100, default=None, blank=True, null=True)
    name = models.CharField(max_length=100, default=None, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(default=None, blank=True, null=True)
    phone = models.CharField(max_length=100, default=None, blank=True, null=True)
    address = models.CharField(max_length=100, default=None, blank=True, null=True)
    about = models.TextField(default=None, blank=True, null=True)
    registered = models.DateTimeField(default=None, blank=True, null=True)

    @property
    def favourite_fruits(self):
        return self.favourite_food.filter(food_type='F').values('name')

    @property
    def favourite_vegetables(self):
        return self.favourite_food.filter(food_type='V').values('name')

    @property
    def favourite_fruit_vegetables(self):
        query_fruits = self.favourite_fruits
        query_vegetables = self.favourite_vegetables

        fruits, vegetables = [], []

        for fruit in query_fruits:
            fruits.append(fruit['name'])

        for vegetable in query_vegetables:
            vegetables.append(vegetable['name'])

        return fruits, vegetables

    def friends_in_common(self, guid, eye_color, has_died):
        second_person = People.objects.get(guid=guid)
        first_friends = self.friends
        second_friends = second_person.friends

        list_first_friends, list_second_friends = [], []
        for value in first_friends:
            list_first_friends.append(value['index'])
        for value in second_friends:
            list_second_friends.append(value['index'])

        common_friends = list(set(list_first_friends) &
                              set(list_second_friends))

        queryset = People.objects.filter(index__in=common_friends, eye_color=eye_color, has_died=has_died).values(
            'index', 'name', 'age', 'address', 'phone', 'eye_color', 'has_died')

        return second_person, list(queryset)
