from django.db import models

# Create your models here.

class Pic(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    name = models.CharField(max_length=200)
    upload_date = models.DateTimeField(auto_now_add=True)
     
    

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
