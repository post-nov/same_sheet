from django.urls import path
from .views import (
    overview,
    record_view,
    cards_view,
    new_card_type_view,
    new_card_view,
    record_card_view,
    record_card_delete_view,
    calendar_year_view,

    contacts_view,
)

urlpatterns = [
    path('', overview, name='overview'),
    path('contacts/', contacts_view, name='contacts'),
    path('<int:year>/<int:month>/<int:day>/', record_view, name='record'),
    path('cards/', cards_view, name='cards'),
    path('cards/new/', new_card_type_view, name='new_card_type'),
    path('cards/<str:card_type>/new/', new_card_view, name='new_card'),
    path('<int:year>/<int:month>/<int:day>/<str:card_type_name>/<str:card_name>/',
         record_card_view,
         name='record_card'),
    path('<int:year>/<int:month>/<int:day>/<str:card_type_name>/<str:card_name>/delete/',
         record_card_delete_view,
         name='record_card_delete'),
    path('calendar/', calendar_year_view, name='calendar_year'),
    path('calendar/<int:year>/', calendar_year_view, name='calendar_year'),
]
