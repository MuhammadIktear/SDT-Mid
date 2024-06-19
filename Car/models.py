from django.db import models
from django.contrib.auth.models import User
class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,unique=True,null=True,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        app_label = 'Car'

class Car(models.Model):
    image = models.ImageField(upload_to='Car/media/uploads/',blank=True,null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return self.name
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    
class Comment(models.Model):
    post = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"
        
    
    

