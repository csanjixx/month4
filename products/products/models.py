from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название продукта")
    description = models.TextField(verbose_name="Описание продукта")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.IntegerField(default=0, verbose_name="Количество на складе")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="Категория")

    def __str__(self):
        return f"{self.title} ({self.category.name})"

    class Review(models.Model):
        product = models.ForeignKey('Product', on_delete=models.CASCADE)
        user_name = models.CharField(max_length=255)
        comment = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"{self.user_name} - {self.product.name} - {self.created_at}"
