from django.db import models

# Create your models here.
class TagModel(models.Model):
   Name = models.CharField(max_length=100)
   def __str__(self):
       return self.Name
class NewModel(models.Model):
   Title = models.CharField(max_length=200)
   Text = models.TextField()
   Tags = models.ManyToManyField(TagModel)
   Source = models.URLField(max_length=200)
   def __str__(self):
       return self.Title
