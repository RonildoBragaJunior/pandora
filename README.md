## Pandora Challenge
Pandora is a mysterious planet. Those types of planets can support human life, for that reason the president of the Handsome Jack decides to send some people to colonise this new planet and reduce the number of people in their own country. After 10 years, the new president wants to know how the new colony is growing, and wants some information about his citizens. Hence he hired you to build a rest API to provide the desired information.

The government from Pandora will provide you two json files (located at resource folder) which will provide information about all the citizens in Pandora (name, age, friends list, fruits and vegetables they like to eat...) and all founded companies on that planet.

Unfortunately, the systems are not that evolved yet, thus you need to clean and organise the data before use. For example, instead of providing a list of fruits and vegetables their citizens like, they are providing a list of favourite food, and you will need to split that list (please, check below the options for fruits and vegetables).

## New Features
Your API must provides these end points:
- Given a company, the API needs to return all their employees. Provide the appropriate solution if the company does not have any employees.
- Given 2 people, provide their information (Name, Age, Address, phone) and the list of their friends in common which have brown eyes and are still alive.
- Given 1 people, provide a list of fruits and vegetables they like. This endpoint must respect this interface for the output: `{"username": "Ahi", "age": "30", "fruits": ["banana", "apple"], "vegetables": ["beetroot", "lettuce"]}`

## Prerequisites
- Python 3.10.6


## Setup
1. Clone the project `https://github.com/RonildoBragaJunior/pandora.git`
2. Inside project folder, create environment follwing the command
`python3 -m venv venv`
3. Activate the environment
`source venv/bin/activate`
4. Intall the project requirements
`pip install -r requirements.txt`
5. Make migrations
`python manage.py makemigrations`
`python manage.py migrate`
5. Access the welcome endpoint to load the database
`http://127.0.0.1:8000/v1/pandora/welcome`

## API Endpoints
- `/v1/pandora/welcome` - Load json files
- `/v1/pandora/companies/` - List all companies so you see their guuid that is auto generated
- `/v1/pandora/companies/<str:guid_company>/employees/` - Company details and its employees.
- `/v1/pandora/people/<str:guid_first_person>/common_friends/<str:guid_second_person>/` - People common friends
- `/v1/pandora/people/<str:guid_person>/favourite_fruit_vegetables/` - People details including their favourite fruits and vegetables.

## API calls
- `curl "http://127.0.0.1:8000/v1/pandora/welcome"`
- `curl "http://127.0.0.1:8000/v1/pandora/companies/"`
- `curl "http://127.0.0.1:8000/v1/pandora/companies/739193e6-fe0d-4768-bf69-7f94c9438572/employees/"`
- `curl "http://127.0.0.1:8000/v1/pandora/people/5e71dc5d-61c0-4f3b-8b92-d77310c7fa43/common_friends/b057bb65-e335-450e-b6d2-d4cc859ff6cc/"`
- `curl "http://127.0.0.1:8000/v1/pandora/people/b057bb65-e335-450e-b6d2-d4cc859ff6cc/favourite_fruit_vegetables/"`

## Adding or Updating more data
- You can just change the json files in the resources folder and hit the welcome endpoint
- Duplicated items are handled appropriately, older record will be updated by the newer record if there are any changes.

## Fruits and vegetables types
- Change the resources fruits.json and vegetables.json

## Running tests
- You can run the unittest by running this command: `python manage.py test`
