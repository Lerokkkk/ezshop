
from rest_framework import serializers



class BalanceToUpSerializer(serializers.Serializer):
    amount = serializers.IntegerField(min_value=0)

    def save(self, user):
        user.balance += self.validated_data['amount']
        user.save()
        return user.balance


class CheckoutSerializer(serializers.Serializer):
    total = serializers.IntegerField(min_value=0)
