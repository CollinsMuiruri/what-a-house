from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=50)
    item = models.CharField(max_length=50)
    image = models.ImageField(upload_to='postedimages/')
    description = models.CharField(max_length=500)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def save_item(self):
        self.save()

    def delete_item(self):
        self.delete()

    @classmethod
    def search_by_item(cls, search_term):
        item = cls.objects.filter(name__icontains=search_term)
        return item


class LandlordProfile(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    id_number = models.IntegerField()

    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
