from django.urls import path
from .views import home_view,cart_view,checkout_view

urlpatterns = [
    path('', home_view,name='home_url'),
    path('cart/', cart_view,name='cart_url'),
    path('checkout/', checkout_view,name='checkout_url'),
]
