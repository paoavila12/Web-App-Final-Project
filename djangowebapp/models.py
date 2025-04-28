from django.db import models

class Record(models.Model):
    create_at = models.DateTimeField(auto_now_add = True) #create_at = model.DateTimeField(auto_now_add = True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    role = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 14)

    def __str__(self):
        return(f"{self.first_name}{self.last_name}")