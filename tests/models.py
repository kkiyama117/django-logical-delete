from django.db import models

# Create your models here.
from logical_delete.models import LogicalDeleteModel


class Goods(LogicalDeleteModel):
    name = models.CharField(max_length=10)
