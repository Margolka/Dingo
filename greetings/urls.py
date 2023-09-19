from django.urls import path
from .views import greeting, greeting_name

urlpatterns = [
   path('', greeting),
   path('<name>', greeting_name),
]