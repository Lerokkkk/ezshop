from django.core.exceptions import ValidationError
from django.db import transaction

from shop_cart.models import ShopCart


def process_checkout(user, total):
    if user.balance < total:

        raise ValidationError(message='Недостаточно средств на балансе')

    with transaction.atomic():
        user.balance -= total
        user.save()

        ShopCart.objects.filter(user=user).delete()



