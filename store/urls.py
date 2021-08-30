from django.contrib.auth import logout
from django.urls import path
from . import views

urlpatterns = [
    path('signUp/', views.signUpPage, name="signUp" ),
    path('login/', views.logInPage, name="login" ),
    path('logout', views.logoutUser, name="logout"),

    path('', views.store, name="store"),
    
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('cart/update_item/', views.updateItem, name="update_item"),
    path('checkout/process_order', views.processOrder, name="process_order"),
    path('<slug:product_slug>', views.product_detail, name="product_details"),

]