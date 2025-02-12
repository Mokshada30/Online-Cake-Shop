from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

#create your model here
class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    number = PhoneNumberField(null=False, blank=False, unique=True)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact table"