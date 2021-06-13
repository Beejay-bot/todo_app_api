from rest_framework import generics
from .models import TodoTable
from .serializers import TodoSerializer

class Todos(generics.ListAPIView):
    queryset = TodoTable.objects.all()
    serializer_class = TodoSerializer

class  TodoDelete(generics.RetrieveDestroyAPIView):
    queryset = TodoTable.objects.all()
    serializer_class = TodoSerializer