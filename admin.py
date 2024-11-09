from django.contrib import admin
from .models import Task, SubTask, Category
# Модель Task
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'deadline', 'created_at', 'get_model_name')
    search_fields = ('title', 'status')
    list_filter = ('status', 'categories')
    ordering = ('-created_at',)
    # Метод для отображения человекочитаемого имени
    def get_model_name(self, obj):
        return obj._meta.verbose_name
    get_model_name.short_description = 'Model Name'
# Модель SubTask
@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'status', 'deadline', 'created_at', 'get_model_name')
    search_fields = ('title', 'task__title')
    list_filter = ('status',)
    ordering = ('-created_at',)
    # Метод для отображения человекочитаемого имени
    def get_model_name(self, obj):
        return obj._meta.verbose_name
    get_model_name.short_description = 'Model Name'
# Модель Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_model_name')
    search_fields = ('name',)
    # Метод для человекочитаемого имени
    def get_model_name(self, obj):
        return obj._meta.verbose_name
    get_model_name.short_description = 'Model Name'
