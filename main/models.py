from django.db import models

# Create your models here.


class Search(models.Model):
    keyword = models.CharField(max_length=200)
    user = models.CharField(max_length=50)  #didn't use Django user model for simplicity
    time = models.DateField(auto_now_add=True)
    numberOfResult = models.IntegerField()

    def __str__(self):
        return self.keyword
