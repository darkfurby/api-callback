from django.urls import path
from api.views import receive_url

urlpatterns = [
    path('callme/', receive_url, name='receive_url'),
    path('callme', receive_url, name='receive_url'),
]
