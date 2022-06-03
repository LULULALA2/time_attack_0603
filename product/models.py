from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = "category"
    name = models.CharField(max_length=20, null=False)


class Drink(models.Model):
    class Meta:
        db_table = "my_drink"  # 테이블 이름

    name = models.CharField(max_length=20, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

