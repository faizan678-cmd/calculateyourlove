from django.db import models

class LoveCalculation(models.Model):
    your_name  = models.CharField(max_length=100)
    her_name   = models.CharField(max_length=100)
    result     = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.your_name} + {self.her_name} = {self.result}%"