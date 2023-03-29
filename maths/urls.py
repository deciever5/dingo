from django.urls import path
from .views import math, add, sub, mul, div,maths_list, math_details,results_list

app_name="maths"
urlpatterns = [
   path('', math),
   path('add/<int:a>/<int:b>', add),
   path('sub/<int:a>/<int:b>', sub),
   path('mul/<int:a>/<int:b>', mul),
   path('div/<int:a>/<int:b>', div),
   path('histories/', maths_list, name="list"),
   path('histories/<int:id>', math_details, name="details"),
   path('results/', results_list, name="results"),
]