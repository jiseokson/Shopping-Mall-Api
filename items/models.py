from django.db import models

from rest_framework.exceptions import ValidationError

class Item(models.Model):
    item_name = models.CharField(max_length=512)
    item_price = models.IntegerField()
    stock_quantity = models.IntegerField()

    def sub_stock(self, quantity, save=True):
        if self.stock_quantity - quantity < 0:
            raise ValidationError('재고 부족으로 주문이 불가능합니다.')
        self.stock_quantity -= quantity
        if save:
            self.save()
