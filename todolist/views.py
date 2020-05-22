from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from todolist.models import TodoItem
from django.http import JsonResponse, HttpResponse

# Create your views here.
from todolist.serializers import TodoItemSerializer


@csrf_exempt
def todo_list(request):

    if request.method == 'GET':
        todo_items = TodoItem.objects.all()
        serializer = TodoItemSerializer(todo_items, many=True)
        return JsonResponse(serializer.data, safe=False)

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
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def todo_detail(request, pk):

    try:
        todo_item = TodoItem.objects.get(pk=pk)
    except TodoItem.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TodoItemSerializer(todo_item)
        return JsonResponse(serializer.data)

    elif request.method == 'DELETE':
        todo_item.delete()
        return HttpResponse(status=204)
