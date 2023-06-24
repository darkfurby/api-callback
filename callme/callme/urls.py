from django.urls import path
from api.views import receive_url

urlpatterns = [
    path('receive_url/', receive_url, name='receive_url'),
    path('receive_url', receive_url, name='receive_url'),
]
