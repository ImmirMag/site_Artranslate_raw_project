from django.db import models

class Dict(models.Model):
    word = models.TextField(default=None,max_length=15)
    translate = models.TextField(default=None,max_length=30)

class Data(models.Model):
    user = models.TextField(default='Null')
    word = models.TextField(default=None,max_length=15)
    translate = models.TextField(default=None,max_length=30)
    iteration = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    last_date = models.DateField(auto_now='True')


class User(models.Model):
    id = models.AutoField(primary_key='True')
    user_id = models.IntegerField(default=0)
    name_current_file = models.TextField(default='')
    max_inputs_number = models.IntegerField(default=0)
# Create your models here.
