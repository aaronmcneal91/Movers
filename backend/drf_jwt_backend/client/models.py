from django.db import models


class Client(models.Model):
    type =models.CharField(max_length = 10)

    def __str__(self):
        return self.type

    