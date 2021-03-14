from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models import CASCADE

TYP = [
    (1, 'Fundacja'),
    (2, 'Organizacja pozarządowa'),
    (3, 'Zbiórka lokalna')
]


class Category(models.Model):
    name = models.CharField(max_length=200)


class Institution(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    type = models.IntegerField(choices=TYP, default=1)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=CASCADE)
    address = models.TextField()
    phone_number = models.IntegerField()
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=9)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, default=None, on_delete=CASCADE)
    is_taken = models.BooleanField(default=False)


