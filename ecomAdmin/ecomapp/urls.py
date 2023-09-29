from django.urls import path
from ecomapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('orders/',views.orders,name="orders"),
    path('payment/',views.payment,name="payment"),
    path('checkout/', views.checkout, name="checkout"),
    path('profile/', views.profile, name="profile"),
    path('address/', views.address, name="address"),
    # path('handlerequest/', views.handlerequest, name="HandleRequest"),
    # path("confirm_payment/<str:pk>", views.confirm_payment, name="confirm_payment"),
    # path('',views.initial_payment,name="initial_payment"),
    # path('/<str:ref>', views.verify_payment, name="verify-payment"),
]