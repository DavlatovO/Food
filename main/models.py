from django.db import models

class FoodType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Food(models.Model):
    type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    recipe = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.TextField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)      
    created = models.DateField(auto_now_add=True)



    