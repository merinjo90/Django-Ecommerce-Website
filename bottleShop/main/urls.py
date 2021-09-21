from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name='home'),
    path('category_list',views.category_list,name='category_list'),
    path('brand_list',views.brand_list,name='brand_list'),
    path('product-list', views.product_list, name='product-list'),
    path('category_product_list/<int:cat_id>',views.category_product_list,name='category_product_list'),
    path('brand_product_list/<int:brand_id>', views.brand_product_list, name='brand_product_list')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)