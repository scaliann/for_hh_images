from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=255)
    file_path = models.ImageField(upload_to='images/')
    upload_date = models.DateTimeField(auto_now_add=True)
    resolution = models.CharField(max_length=50)
    size = models.IntegerField()

    def __str__(self):
        return self.name