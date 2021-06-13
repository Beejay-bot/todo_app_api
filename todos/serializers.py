from django.db.models import fields
from rest_framework import serializers
from .models import TodoTable


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoTable
        fields = ['content']