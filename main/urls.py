from django.urls import path 
from .views import *

urlpatterns = [
    path("new/", New.as_view()),
]