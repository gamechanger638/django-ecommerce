from django.db import models

# Create your models here.
 

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Product Name")
    description = models.TextField(verbose_name="Product Description", null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    image1 = models.ImageField(upload_to='products/', verbose_name="Image 1", blank=True, null=True)
    image2 = models.ImageField(upload_to='products/', verbose_name="Image 2", blank=True, null=True)
    image3 = models.ImageField(upload_to='products/', verbose_name="Image 3", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"