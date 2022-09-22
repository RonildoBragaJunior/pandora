import json
import logging
from decimal import Decimal
from re import sub

from django.core.exceptions import ObjectDoesNotExist
from pandora.models import Company, Food, People, Tag


class WelcomeService:
    '''
    Service class for parsing files made available in resources folder into data models
    '''

    logger = logging.getLogger(__name__)

    def __init__(self):
        with open('resources/fruits.json', 'r') as fruits:
            self.fruits = json.load(fruits)
        with open('resources/vegetables.json', 'r') as vegetables:
            self.vegetables = json.load(vegetables)

    def __load_companies(self):
        with open('resources/companies.json', 'r') as data_file:
            data = json.load(data_file)
            for value in data:
                Company(index=value['index'], name=value['company']).save()

    def __save_tags(self, tags, people):
        for value in tags:
            tag = Tag(name=value)
            tag.save()
            people.tags.add(tag)

    def __save_food(self, foods, people):
        for value in foods:
            if value in self.fruits['list']:
                food = Food(name=value, food_type='F')
            elif value in self.vegetables['list']:
                food = Food(name=value, food_type='V')
            else:
                food = Food(name=value, food_type='U')

            food.save()
            people.favourite_food.add(food)

    def __load_people(self):
        with open('resources/people.json', 'r') as data_file:
            data = json.load(data_file)
            for value in data:

                try:
                    my_company = Company.objects.get(index=value['company_id'])

                    people = People(index=value['index'], company=my_company, guid=value['guid'], has_died=value['has_died'],
                                    balance=Decimal(sub(r'[^\d.]', '', value['balance'])), picture=value['picture'], age=value['age'],
                                    eye_color=value['eyeColor'], name=value['name'], gender=value['gender'], email=value['email'],
                                    phone=value['phone'], address=value['address'], about=value['about'], registered=value['registered'],
                                    friends=value['friends'])
                    people.save()
                    self.__save_tags(value['tags'], people)
                    self.__save_food(value['favouriteFood'], people)
                except ObjectDoesNotExist:
                    self.logger.warning(
                        'The company with index %s does not exist therefore this person %s will not be saved', value['company_id'], value['index'])
                    continue

    def load_pandora_citzens(self):
        self.__load_companies()
        self.__load_people()
