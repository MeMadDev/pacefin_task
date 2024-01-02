from django.db import models

 
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    status = models.BooleanField()
    
 
   