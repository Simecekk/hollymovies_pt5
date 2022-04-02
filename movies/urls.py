from django.urls import path
from movies.views import homepage

urlpatterns = [
    path('', homepage),
]
