from django.db import models

# Create your models here.
class Course(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
