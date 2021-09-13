from django.db import models

# Create your models here.

#category
class Category(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="cat_img/")

    def __str__(self):
        return self.title

#brand
class Brand(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="brand_img/")

    def __str__(self):
        return self.title

#Color
class Color(models.Model):
    title=models.CharField(max_length=100)
    color_cod=models.CharField(max_length=100)

    def __str__(self):
        return self.title

#Size
class Size(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title