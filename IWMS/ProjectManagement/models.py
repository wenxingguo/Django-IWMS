from django.db import models

# Create your models here.

class Station(models.Model):
    #工位
    name = models.CharField(max_length=50, null = False, unique=True, help_text='工位名称')
    description = models.TextField(max_length=200, blank= True, null= True, help_text='工位描述')
    def __str__(self):
        return self.name

class Current(models.Model):
    Station = models.ForeignKey(Station, on_delete=models.CASCADE, null=False, blank=False)
    date_time = models.DecimalField(max_digits= 10, decimal_places=0)
    value = models.FloatField()

class Voltage(models.Model):
    Station = models.ForeignKey(Station, on_delete=models.CASCADE, null = False, blank=False)
    date_time = models.DecimalField(max_digits= 10, decimal_places=0)
    value = models.FloatField()

class Sound(models.Model):
    Station = models.ForeignKey(Station, on_delete=models.CASCADE, null=False, blank=False)
    date_time = models.DecimalField(max_digits= 10, decimal_places=0)
    value = models.FloatField()

class PoolImg(models.Model):
    Station = models.ForeignKey(Station, on_delete=models.CASCADE, null=False, blank = False)
    date_time = models.DecimalField(max_digits= 10, decimal_places=0)
    value = models.TextField() #base64数据
