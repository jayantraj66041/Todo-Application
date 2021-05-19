from django.urls import path
from .views import TodoDetails, TodoList
urlpatterns = [
    path('', TodoList.as_view()),
    path('<int:id>', TodoDetails.as_view()),
]