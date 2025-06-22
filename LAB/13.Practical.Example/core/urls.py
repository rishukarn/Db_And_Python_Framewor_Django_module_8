from django.urls import path
from core.views import index,register,forgot,activate_account,seller_dashboard,customer_dashboard,change_password,password_reset_confirm
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',index,name='Home'),
    path('re/',register,name='singup'),
    path('fg/',forgot,name='forgot'),
    path('activate/<uidb64>/<str:token>/', activate_account,name='activate'),
    path('password_reset_confirm/<uidb64>/<str:token>/', password_reset_confirm,name='password_reset_confirm'),
    path('seller/',seller_dashboard,name='seller_dashboard'),
    path('customer/',customer_dashboard,name='customer_dashboard'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('change/',change_password,name='change_password')
    
]