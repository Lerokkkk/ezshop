from django.urls import path, include
from .views import BalanceToUpView, CheckoutView

urlpatterns = [
    path('balance/', BalanceToUpView.as_view()),
    path('purchase/', CheckoutView.as_view()),
]
