from django.shortcuts import render
from django.http import JsonResponse
from .models import TaskList, Task
# Create your views here.

def lists(request):
    all_lists = TaskList.objects.all()
    json_lists = [c.to_json() for c in all_lists]
    return JsonResponse(json_lists, safe=False)

def task_list_under(request,pk):
    try:
        li = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    json_li = li.to_json()
    return JsonResponse(json_li)

def list_tasks(request,pk):
    try:
        list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    tasks = list.task_set.all()
    json_tasks = [t.to_json() for t in tasks]
    return JsonResponse(json_tasks,safe=False)