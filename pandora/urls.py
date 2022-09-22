from django.urls import path

from pandora import views

urlpatterns = [
    path('welcome', views.welcome, name='welcome'),
    path('companies/',views.list_companies, name='list_companies'),
    path('companies/<str:guid_company>/employees/',views.company_employees, name='company_employees'),
    path('people/<str:guid_first_person>/common_friends/<str:guid_second_person>/',views.friends_in_common, name='people_friends_in_common'),
    path('people/<str:guid_person>/favourite_fruit_vegetables/',views.favourite_fruit_vegetables, name='people_favourite_fruit_vegetables'),
]
