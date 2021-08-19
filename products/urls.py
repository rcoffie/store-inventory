from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('',views.home,name="home"),
    path('product_detail/<int:id>/',views.product_detail,name='product_detail'),
    path('issue_item/<str:pk>/',views.issue_item,name="issue_item"),
    path('add_to_stock/<str:pk>/',views.add_to_stock,name="add_to_stock"),
    path('receipt/', views.receipt, name = "receipt"),
    path('all_sales/', views.all_sales, name = 'all_sales'),
    path('receipt_detail/<int:id>/',views.receipt_detail,name="receipt_detail")
    
]
