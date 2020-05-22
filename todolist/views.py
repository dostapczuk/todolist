from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from todolist.models import TodoItem

# Create your views here.
from todolist.serializers import TodoItemSerializer


@api_view(['GET', 'POST'])
def todo_list(request, format=None):

    if request.method == 'GET':
        todo_items = TodoItem.objects.all()
        serializer = TodoItemSerializer(todo_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        data["author_ip"] = ip
        print(ip)
        serializer = TodoItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def todo_detail(request, pk, format=None):

    try:
        todo_item = TodoItem.objects.get(pk=pk)
    except TodoItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodoItemSerializer(todo_item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        todo_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
