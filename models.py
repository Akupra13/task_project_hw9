from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'task_manager_category'
        verbose_name = 'Category'
class Task(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    status = models.CharField(
        max_length=20, choices=[('New', 'New'), ('In progress', 'In progress'),
                                ('Pending', 'Pending'), ('Blocked', 'Blocked'), ('Done', 'Done')]
    )
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'task_manager_task'
        ordering = ['-created_at']
        verbose_name = 'Task'
class SubTask(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20, choices=[('New', 'New'), ('In progress', 'In progress'),
                                ('Pending', 'Pending'), ('Blocked', 'Blocked'), ('Done', 'Done')]
    )
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'task_manager_subtask'
        ordering = ['-created_at']
        verbose_name = 'SubTask'
