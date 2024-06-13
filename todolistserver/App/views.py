import json
from rest_framework.views import APIView
from rest_framework.response import Response
from App.env import env

from .models import *


# rich
from rich import pretty
from rich.console import Console

pretty.install()
console = Console()



class TaskStatusAPI(APIView):
    def get(self, request):
        # 檢查是否有任務已經註冊過
        tasks_registered = Task.objects.exists()
        # 檢查 Task 是否是空的
        tasks_empty = not Task.objects.exists()
        # 檢索前20筆資料
        latest_tasks = Task.objects.all().order_by('-id')[:20]
        latest_serializer = TaskSerializer(latest_tasks, many=True)
        
        # 檢索所有未完成的任務，排除掉已經在前 20 筆資料中出現過的任務
        incomplete_tasks = Task.objects.filter(completed=False).exclude(id__in=[task.id for task in latest_tasks])
        incomplete_serializer = TaskSerializer(incomplete_tasks, many=True)
        
        # 合併 latest_tasks 和 incomplete_tasks 為一個列表
        all_tasks = list(latest_tasks) + list(incomplete_tasks)
        
        # 序列化合併後的任務列表
        all_tasks_serializer = TaskSerializer(all_tasks, many=True)

        return Response({
            'tasks_registered': tasks_registered,
            'tasks_empty': tasks_empty,
            "tasks": all_tasks_serializer.data,
        })


        
        