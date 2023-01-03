from django.db import models

# Create your models here.
class Link(models.Model):
  uid = models.CharField(max_length=1000)
  link = models.URLField()

  def __str__(self):
    return self.link