from django.db import models

# Create your models here.
class article(models.Model):
    title=models.CharField(max_length=100)
    image=models.URLField(null=True,blank=True)
    url=models.TextField()

    def __str__(self):
        return self.title