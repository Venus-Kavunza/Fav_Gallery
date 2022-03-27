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


class Location(models.Model):
    name = models.CharField(max_length=100)
    
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    @classmethod
    def all_locations(cls):
        locations = Location.objects.all()
        return locations

    @classmethod   
    def update_location(cls, id, name):
        cls.objects.filter(id=id).update(name=name)

    def __str__(self):
        return self.name
