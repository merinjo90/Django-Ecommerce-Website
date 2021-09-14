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

# Banner
class Banner(models.Model):
    img = models.CharField(max_length=200)
    alt_text = models.CharField(max_length=300)

#Product Model
class Product(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='product_img/')
    slug=models.CharField(max_length=400)
    detail=models.TextField()
    specifs=models.TextField()
    #price=models.PositiveIntegerField()
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.title

#Prduct Attribute
class ProductAttribute(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)
    price=models.PositiveIntegerField()

    def __str__(self):
        return self.product.title

