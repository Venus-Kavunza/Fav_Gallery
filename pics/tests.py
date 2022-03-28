from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Pics, Location, Category

# Testing the save method


class LocationTestClass(TestCase):

    # set up method

    def setUp(self):
        self.Venus = Location(location_name='Venus')
        self.Venus.save_location_name()


    def tearDown(self):
        Location.objects.all().delete()
 
    def test_instance(self):
        self.assertTrue(isinstance(self.Venus, Location))

    def test_save_method(self):
        self.Venus.save_location_name()
        Locations = Location.objects.all()
        print(Locations)
        self.assertTrue(len(Locations)==1)

    def test_update_location(self):
        new_location.update_location(self.location.id,new_location_name)
        updated_location = Location.objects.filter(location_name='')
        self.assertTrue(len(updated_location) > 0)


    def test_delete_method(self):
        self.Kasarani.delete_location_name()
        Locations = Location.objects.all()
        print(Locations)
        self.assertTrue(len(Locations)==0)
        

    

class PhotosTestClass(TestCase):
    def setUp(self):
        self. new_location = Location(location_name = 'Nakuru')
        self. new_location.save()

        self. new_category = Category(category_name = 'Nature')
        self. new_category.save()

        self. new_car = Pics(name = 'Benz', photo_description = 'Nice photo', photo_location = self.new_location, photo_category = self.new_category, photo = 'image.jpeg' )
        self. new_car.save()

    def tearDown(self):
        Pics.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()


    def test_instance(self):
        self.assertTrue(isinstance(self.new_building, Pics))

    def test_save_car(self):
        self.new_building.save_photo()
        photo = Pics.objects.all()
      
        
    def test_delete_car(self):
        self.new_building.save_photo()
        self.new_building.delete_photo()
       

class CategoryTestClass(TestCase):
    def setUp(self):
        self.Tour= Category(category_building ='Tour')
        self.Tour.save_building_name()


    def tearDown(self):
        Category.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.Tour, Category))

    def test_save_category(self):
        self.test_category = Category(category_name = 'Business')
        self.test_category.save_category_name()


    def test_delete_category(self):
        self.test_category = Category(category_name = 'Business')
        self.test_category.save_category_name()
        self.test_category.delete_category_name()