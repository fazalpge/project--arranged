from django.db import models

#c:/Users/DELL/projectformit/env/Scripts/Activate

class Employee(models.Model):
    name = models.CharField(max_length=100)
    atrisk= models.IntegerField()
    notrisk= models.IntegerField()
    class Meta:
        db_table ='myapp_employee'
    
    

