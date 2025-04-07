from django.db import models

class Record(models.Model):
    create_at = models.DateTimeField(auto_now_add = True) #create_at = model.DateTimeField(auto_now_add = True)
    first_name = model.CharField()
    last_name = model.CharField()
    email = model.EmailField()
    phone = model.CharField()