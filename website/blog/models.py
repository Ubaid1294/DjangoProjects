from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    public_date = models.DateTimeField()
    image = models.ImageField(upload_to="images")
    body = models.TextField()

    def summary(self):
        return self.body[:100]

    def pub_date(self):
        return self.public_date.strftime("%B %d, %Y %I:%M %p")

    def __str__(self):
        return self.title