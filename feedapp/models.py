from django.db import models

# Create your models here.
class FeedbackData(models.Model):
    Name=models.CharField(max_length=100)
    Rating=models.IntegerField()
    Date=models.DateTimeField(max_length=100)
    Feedback=models.CharField(max_length=100)