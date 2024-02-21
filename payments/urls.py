from django.urls import path
from .views import GateView, PaymentView

urlpatterns = [
    path("gaeways/", GateView.as_view()),
    path("pay/", PaymentView.as_view())
]
