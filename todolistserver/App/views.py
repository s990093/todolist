import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *

from src.get_obs import classify_task, get_embeddings


# rich
from rich import pretty
from rich import print,print_json
from rich.console import Console

pretty.install()
console = Console()
import torch
from transformers import BertTokenizer
from sklearn.preprocessing import LabelEncoder

with open('App/data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Load the saved model and label encoder
classifier = torch.load('App/classifier.pt')
label_encoder = LabelEncoder()
data['category_encoded'] = label_encoder.fit_transform(data['category'])


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
            "tasks": latest_serializer.data,
            "tasks": all_tasks_serializer.data
        })


class TaskCreateAPIView(APIView):
    def post(self, request, format=None):
        try:    
            # ai
            predicted_category, prediction_score= classify_task(request.data['text'], classifier, label_encoder)
            request.data['type'] = predicted_category
            
            print(request.data, f"prediction_score - > {prediction_score}")

            serializer = TaskSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        try:
            # 檢索前20筆資料
            latest_tasks = Task.objects.all().order_by('-id')[:20]
            latest_serializer = TaskSerializer(latest_tasks, many=True)
            
            # 檢索所有未完成的任務，排除掉已經在前 20 筆資料中出現過的任務
            incomplete_tasks = Task.objects.filter(completed=False).exclude(id__in=[task.id for task in latest_tasks])
            incomplete_serializer = TaskSerializer(incomplete_tasks, many=True)

            return Response({
                "latest_tasks": latest_serializer.data,
                "incomplete_tasks": incomplete_serializer.data
            })
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        try:
            # 取得要更新的任務的 ID
            task_id = request.data.get('id')
            
            # 找到對應 ID 的任務
            task = Task.objects.get(pk=task_id)
            
            # 更新任務完成狀態
            task.completed = True
            
            # 儲存更新後的任務
            task.save()
            
            # 序列化更新後的任務
            serializer = TaskSerializer(task)
            
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        
class TaskClassifier(APIView):
    def post(self, request, format=None):
        task = request.data.get('task', '')
        if not task:
            return Response({'error': 'No task provided'}, status=status.HTTP_400_BAD_REQUEST)

    
        

        predicted_category = classify_task(task, classifier, label_encoder)
        
        print(f'Task: {task}, Predicted Category: {predicted_category}')

        return Response({'predicted_category': predicted_category}, status=status.HTTP_200_OK)