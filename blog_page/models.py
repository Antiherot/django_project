from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def save(self, *arg,**kwargs):
        if not self.name.startswith('#'):
            self.name = f'#{self.name}'
        super(Category,self).save(*arg,**kwargs)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)
    mood = models.PositiveIntegerField(null=False,blank=False,default=9)

    def __str__(self):
        return self.title
    
class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.quote
 
    