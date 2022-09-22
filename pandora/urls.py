from django.urls import path

from pandora import views

urlpatterns = [
    path('welcome', views.welcome, name='welcome'),
    path('companies/<int:id_company>/employees/',views.company_employees, name='company_employees'),
    path('people/<int:id_first_person>/common_friends/<int:id_second_person>/',views.friends_in_common, name='people_friends_in_common'),
    path('people/<int:id_person>/favourite_fruit_vegetables/',views.favourite_fruit_vegetables, name='people_favourite_fruit_vegetables'),
]
