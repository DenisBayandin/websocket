from django.urls import path
from .views import note_view


urlpatterns = [
    path('note-example/', note_view, name='note'),
]
