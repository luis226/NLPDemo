from django.urls import path
from .views import *



app_name = 'email_filter'
urlpatterns = [
    path('', Index.as_view(), name='index'),
]