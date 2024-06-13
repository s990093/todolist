from App.models import Task, TaskSerializer


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rich import print

# mdoels
from src.Bertchinese.predictionModel import PredictionModel
from App import env

model = PredictionModel(json_file_path="data.json", model_path="classifier.pt", env=env)

class TaskCreateAPIView(APIView):
    def post(self, request, format=None):
        try:
            # ai
            predicted_category, prediction_score = model.predict(request.data['text'])
            request.data['type'] = predicted_category


            serializer = TaskSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
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