# Pandora Challenge
Pandora is a mysterious planet. Those types of planets can support human life, for that reason the president of the Handsome Jack decides to send some people to colonise this new planet and reduce the number of people in their own country. After 10 years, the new president wants to know how the new colony is growing, and wants some information about his citizens. Hence he hired you to build a rest API to provide the desired information.
The government from Pandora will provide you two json files (located at resource folder) which will provide information about all the citizens in Pandora (name, age, friends list, fruits and vegetables they like to eat...) and all founded companies on that planet.
Unfortunately, the systems are not that evolved yet, thus you need to clean and organise the data before use.
For example, instead of providing a list of fruits and vegetables their citizens like, they are providing a list of favourite food, and you will need to split that list (please, check below the options for fruits and vegetables).

## New Features
Your API must provides these end points:
- Given a company, the API needs to return all their employees. Provide the appropriate solution if the company does not have any employees.
- Given 2 people, provide their information (Name, Age, Address, phone) and the list of their friends in common which have brown eyes and are still alive.
- Given 1 people, provide a list of fruits and vegetables they like. This endpoint must respect this interface for the output: `{"username": "Ahi", "age": "30", "fruits": ["banana", "apple"], "vegetables": ["beetroot", "lettuce"]}`

## Prerequisites
- Python 3.10.6


## Setup


## API Endpoints
- `/v1/pandora/welcome` - This will load the json files into the database
- `companies/<int:id_company>/employees/` - This endpoint will return a company's details and its employees.
- `people/<int:id_first_person>/common_friends/<int:id_second_person>/` - This endpoint will return the people containing details of their common friends that has brown eyes and are still alive.
- `people/<int:id_person>/favourite_fruit_vegetables/` - This endpoint will return some of the user's details including their favourite fruits and vegetables.

## Sample API calls
### Company API
```
curl "http://127.0.0.1:8000/v1/pandora/companies/1/employees/"
```
### User API
```
curl "http://127.0.0.1:8000/v1/pandora/people/0/common_friends/1/"
```
```
curl "http://127.0.0.1:8000/v1/pandora/people/1/favourite_fruit_vegetables/"
```

## Adding or Updating more data?
- You can just change the json files in the resources folder and hit the welcome endpoint
```

## Duplicated data?
Duplicated items are handled appropriately, older record will be updated by the newer record if there are any changes.

## Need new fruits and vegetables classfications?
If you need want to add more fruits or vegetables, please change the resources fruits.json and vegetables.json


## Running tests
You can run the unittest by running this command:
```
python manage.py test
```
If you have changed the json files, you need to update the tests to match the expected results
