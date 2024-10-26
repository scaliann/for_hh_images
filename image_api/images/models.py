from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=255)
    file_path = models.ImageField(upload_to='images/media/original')
    resized_100_path = models.ImageField(upload_to='images/media/resized_100/', blank=True, null=True)
    resized_500_path = models.ImageField(upload_to='images/media/resized_500/', blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    resolution = models.CharField(max_length=50, blank=True)
    size = models.IntegerField(blank=True)
    format = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name