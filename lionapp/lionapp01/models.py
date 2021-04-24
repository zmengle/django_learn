from django.db import models

# Create your models here.


class Logs(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    info = models.CharField(
        max_length=64
    )
    created_at = models.DateTimeField(
        auto_now=True
    )  

