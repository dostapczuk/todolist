from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from todolist import views

urlpatterns = [
	path('todolist/', views.todo_list),
	path('todolist/<int:pk>/', views.todo_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
