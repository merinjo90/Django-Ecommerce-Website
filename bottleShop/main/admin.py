from django.contrib import admin
from .models import Banner,Category,Brand,Color,Size,Product,ProductAttribute

# Register your models here.
admin.site.register(Banner)
admin.site.register(Brand)
admin.site.register(Size)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
admin.site.register(Category,CategoryAdmin)

class ColorAdmin(admin.ModelAdmin):
    list_display = ('title','color_bg')
admin.site.register(Color,ColorAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','brand','color','size','status')
    list_editable = ('status',)
admin.site.register(Product,ProductAdmin)

#product attribute
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id','product','color','size','price')
admin.site.register(ProductAttribute,ProductAttributeAdmin)