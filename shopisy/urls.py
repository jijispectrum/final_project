from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('product/', views.product, name='product'),
    path('upload/', views.upload_product, name='upload_product'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('logout/', views.user_logout, name='logout'),

   
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update-cart/<int:cart_item_id>/', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order_confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('razorpay/payment/', views.razorpay_payment, name='razorpay_payment'),
    path('receipt/', views.receipt, name='receipt'),
    path('why/', views.why, name='why'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('contact/', views.contact, name='contact'),
  

]



