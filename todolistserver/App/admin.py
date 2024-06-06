from django.contrib import admin
from .models import Task, ClassifyTask, TaskCompletion, LongTermGoal


class TaskAdmin(admin.ModelAdmin):
    list_display = ('text', 'type', 'completed')  # 在列表中顯示的欄位

   
# 將自定義的 ModelAdmin 註冊到 Task 模型
admin.site.register(Task, TaskAdmin)
admin.site.register(ClassifyTask)
admin.site.register(TaskCompletion)
admin.site.register(LongTermGoal)
