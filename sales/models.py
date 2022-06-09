from django.conf import settings
from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='pics', null=True)
    price = models.IntegerField()
    size = models.CharField(max_length=50, null=True)
    brand = models.CharField(max_length=100, null=True)
    dis = models.BooleanField(default=False)
    category = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    description = models.CharField(max_length=4000, null=True, blank=True)
    is_active = models.BooleanField(default=True)

# class OrderItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.name
#
# class Order(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     items = models.ManyToManyField(OrderItem)
#     start_date = models.DateTimeField(auto_now_add=True)
#     ordered_date = models.DateTimeField()
#     ordered = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.user.username

class Comment(models.Model):
    product = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE)
    commenter_name = models.CharField(max_length=200)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.product.name, self.commenter_name)