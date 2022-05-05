from django.db import models

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.pizza_name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        return f"{self.topping_name[:50]}..."

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    comment_name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment_name[:50]}..."