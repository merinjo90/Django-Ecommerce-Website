from django.shortcuts import render
from .models import Banner, Category, Brand, Product, ProductAttribute


# Create your views here.

#Home Page
def home(request):
    banners=Banner.objects.all().order_by('-id')
    data=Product.objects.filter(is_featured=True).order_by('-id')
    return render(request,'index.html',{'data':data,'banners':banners})

#Category
def category_list(request):
    data=Category.objects.all().order_by('-id')
    return render(request,'category_list.html',{'data':data})

#Brand
def brand_list(request):
    data=Brand.objects.all().order_by('-id')
    return render(request,'brand_list.html',{'data':data})

#Product List
def product_list(request):
    data=Product.objects.all().order_by('-id')
    cats=Product.objects.distinct().values('category__title','category_id')
    colors=ProductAttribute.objects.distinct().values('color__title','color_id','color__color_cod')
    sizes = ProductAttribute.objects.distinct().values('size__title','size_id')
    brands=Product.objects.distinct().values('brand__title','brand_id')
    return render(request,'product_list.html',
        {
            'data':data,
            'cats':cats,
            'brands':brands,
            'colors':colors,
            'sizes':sizes,
        })

#Product list According to category
def category_product_list(request,cat_id):
    category=Category.objects.get(id= cat_id)
    data=Product.objects.filter(category=category)
    cats = Product.objects.distinct().values('category__title', 'category_id')
    colors = ProductAttribute.objects.distinct().values('color__title', 'color_id', 'color__color_cod')
    sizes = ProductAttribute.objects.distinct().values('size__title', 'size_id')
    brands = Product.objects.distinct().values('brand__title', 'brand_id')
    return render(request,'category_product_list.html',
            {
                'data':data,
                'cats': cats,
                'brands': brands,
                'colors': colors,
                'sizes': sizes,
            })


#Product list According to Brand
def brand_product_list(request,brand_id):
    brand=Brand.objects.get(id= brand_id)
    data=Product.objects.filter(brand=brand)
    cats = Product.objects.distinct().values('category__title', 'category_id')
    colors = ProductAttribute.objects.distinct().values('color__title', 'color_id', 'color__color_cod')
    sizes = ProductAttribute.objects.distinct().values('size__title', 'size_id')
    brands = Product.objects.distinct().values('brand__title', 'brand_id')
    return render(request,'category_product_list.html',
            {
                'data':data,
                'cats': cats,
                'brands': brands,
                'colors': colors,
                'sizes': sizes,
            })
