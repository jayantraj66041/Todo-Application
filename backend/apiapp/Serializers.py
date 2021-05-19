from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Todo

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Todo