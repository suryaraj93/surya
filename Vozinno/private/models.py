
from django.db import models

class Email(models.Model):
    mail=models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.mail



class Details(models.Model):
    email=models.ForeignKey(Email,on_delete=models.CASCADE)
    password=models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    dob =models.DateField()
    last_degree= models.CharField(max_length=120)
    profile_pic=models.ImageField(upload_to="images")

    def __str__(self):
        return self.name



