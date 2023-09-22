from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=20)


class Product(models.Model):
    title = models.CharField(max_length=20)
    users = models.ManyToManyField(Users, through='Access')


class Access(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    access_status = models.BooleanField()
    owner_status = models.BooleanField()



class Lesson(models.Model):
    title = models.CharField(max_length=20)
    url = models.URLField()
    duration = models.IntegerField()
    viewing_status = models.BooleanField()
    viewing_time = models.IntegerField()
    last_viewing_date = models.DateField()
    products = models.ManyToManyField(Product)