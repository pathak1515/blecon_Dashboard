from django.db import models

# Create your models here.
class beacon(models.Model):
    uuid=models.CharField(max_length=10)
    major=models.CharField(max_length=10)
    minor=models.CharField(max_length=10)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.uuid

class department(models.Model):
    name=models.CharField(max_length=30)
    # beacon_id=models.ForeignKey(beacon,on_delete=models.CASCADE)
    beacon = models.ForeignKey(beacon,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class hit(models.Model):
    dept_name=models.CharField(max_length=30)        
    hits=models.IntegerField(default=False)
    def __str__(self):
        return self.dept_name

class notification(models.Model):
    department=models.ForeignKey(department,on_delete=models.CASCADE)
    notification=models.CharField(max_length=30)
    def __str__(self):
        return self.department





