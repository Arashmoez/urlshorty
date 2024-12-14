from django.db import models
from .utils import code_generator
# Create your models here.
class MoezUrl(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=20 , blank=True , default=code_generator())
