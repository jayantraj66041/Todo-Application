from django.shortcuts import render
from .Serializers import TodoSerializers
from .models import Todo
from rest_framework import mixins, generics
# Create your views here.

class TodoList(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class TodoDetails(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request, id)
    
    def delete(self, request, id):
        return self.destroy(request, id)
    
    def put(self, request, id):
        return self.update(request, id)
