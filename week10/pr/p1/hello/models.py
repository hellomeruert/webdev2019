from django.db import models

class TodoItem(models.Model):
    objects = models.Manager()
    content = models.TextField()
    
    
