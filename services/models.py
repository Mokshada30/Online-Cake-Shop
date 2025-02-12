from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact table"


# product model
class Product(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200 ,help_text="Relative path to the image within 'static/img/'")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.title


# Payment Model
class Payment(models.Model):
    # product_name = models.CharField(max_length=100)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    card_number = models.CharField(max_length=16)
    card_holder = models.CharField(max_length=100)
    expiration_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return self.product.title