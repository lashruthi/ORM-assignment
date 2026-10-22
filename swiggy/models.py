from django.db import models

class FoodItem(models.Model):
    item_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    cuisine_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.FloatField()
    is_available = models.BooleanField(default=True)

    def _str_(self):
        return self.name