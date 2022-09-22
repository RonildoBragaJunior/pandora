from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.http.response import HttpResponseBadRequest

from pandora.models import Company, People
from pandora.services.welcome import WelcomeService


def welcome(request):
    '''
    Loads and provides information about all citizens in Pandora as per given json files.
        Returns:
                json (json object): An HTTP response class that consumes data to be serialized to JSON
        Raises:
            HttpResponseBadRequest: If there is any problem with the json files provided
    '''
    try:
        WelcomeService().load_pandora_citzens()
        data={
            'pandora_companies': Company.objects.all().count(),
            'pandora_citizens': People.objects.all().count()
        }
        return JsonResponse(data)
    except:
        return HttpResponseBadRequest('Bad request', status=400)

def list_companies(request):
    '''
    List all companies in padora.
    '''
    queryset = Company.objects.values()
    data = {
        "qtd_companies": queryset.count(),
        "companies": list(queryset)
    }
    return JsonResponse(data)

def company_employees(request, guid_company):
    '''
    Finds company employees given a determined company index.
        Parameters:
                guid_company (str): A UUID (Universal Unique Identifier)
        Returns:
                json (json object): An HTTP response class that consumes data to be serialized to JSON
        Raises:
            HttpResponseBadRequest: If the company index does not exists
    '''
    try:
        company = Company.objects.get(guid=guid_company)
        data = {
            'company_index': company.index,
            'company_name': company.name,
            'company_employees': list(company.employees.values('index', 'name', 'age', 'address', 'phone'))
        }
        return JsonResponse(data)
    except ObjectDoesNotExist:
        return HttpResponseBadRequest('Bad request', status=404)


def friends_in_common(request, guid_first_person, guid_second_person):
    '''
    Finds friends in common given the index of 2 people.
        Parameters:
                guid_first_person (str): A UUID (Universal Unique Identifier)
                guid_second_person (str): A UUID (Universal Unique Identifier)
        Returns:
                json (json object): An HTTP response class that consumes data to be serialized to JSON
        Raises:
            HttpResponseBadRequest: If one of the person index does not exists
    '''
    try:
        first_person = People.objects.get(guid=guid_first_person)
        second_person, common_friends = first_person.friends_in_common(
            guid=guid_second_person, eye_color='brown', has_died=False)
        data = {
            'first_person': {
                'name': first_person.name,
                'age': first_person.age,
                'address': first_person.address,
                'phone': first_person.phone

            },
            'second_person': {
                'name': second_person.name,
                'age': second_person.age,
                'address': second_person.address,
                'phone': second_person.phone

            },
            'common_friends': common_friends
        }
        return JsonResponse(data)
    except ObjectDoesNotExist:
        return HttpResponseBadRequest('Bad request', status=404)


def favourite_fruit_vegetables(request, guid_person):
    '''
    Finds favourite food given the index of 1 person.
        Parameters:
                guid_person (str): A UUID (Universal Unique Identifier)
        Returns:
                json (json object): An HTTP response class that consumes data to be serialized to JSON
        Raises:
            HttpResponseBadRequest: If the person index does not exists
    '''
    try:
        people = People.objects.get(guid=guid_person)
        fruits, vegetables = people.favourite_fruit_vegetables
        data = {
            'username': people.name,
            'age': people.age,
            'fruits': fruits,
            'vegetables': vegetables
        }
        return JsonResponse(data)
    except ObjectDoesNotExist:
        return HttpResponseBadRequest('Bad request', status=404)
