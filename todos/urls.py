from django.urls import path
from .views import *


urlpatterns = [
        path('', Todos.as_view(), name='Todo'),
        path('<int:pk>/', TodoDelete.as_view(), name="todoDetail")
]
