from django.contrib import admin
from services.models import Contact
from services.models import Product
from services.models import Payment



# Register your models here.
admin.site.site_header="The Cake Fairy | Admin"

class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','email','number','subject','added_on','is_approved']
admin.site.register(Contact,ContactAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','title','image_url','price','rating']    
admin.site.register(Product,ProductAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display=['id','product_name','price','card_number','card_holder','expiration_date','cvv']    
admin.site.register(Payment,PaymentAdmin)


