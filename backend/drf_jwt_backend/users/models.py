from django.db import models
# from client.models import Client


class Users(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email= models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    # type =models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

