from django.db import models

class Record(models.Model):
    create_at = models.DateTimeField(auto_now_add = True) #create_at = model.DateTimeField(auto_now_add = True)
    first_name = models.CharField(max_length = 15)
    last_name = models.CharField(max_length = 10)
    email = models.EmailField()
    phone = models.CharField(max_length = 10)