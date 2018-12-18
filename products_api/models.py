from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30, blank= False)
    created_date = models.DateTimeField()


class DialogFlowRequest(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, blank=False)
    content = models.TextField()
