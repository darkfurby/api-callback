from django.urls import path
from hello.views import get_output, hello, query_and_output

urlpatterns = [
    path('hello', hello, name='hello'),
    path('hello/', hello, name='hello'),
    path('output/', get_output, name='get_output'),
    path('output', get_output, name='get_output'),
    path('queryoutput/', query_and_output, name='query_and_output'),
    path('queryoutput', query_and_output, name='query_and_output'),
]
