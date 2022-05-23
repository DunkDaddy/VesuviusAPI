

from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),

    path('reservation-list/', views.showAllReservations, name='reservation-list'),
    path('location-list/', views.showAllLocations, name='location-list'),
    path('customer-list/', views.showAllCustomers, name='customer-list'),
    path('tables-list/', views.showAllTables, name='tables-list'),
    path('ingredients-list/', views.showAllIngredients, name='ingredients-list'),
    path('category-list/', views.showAllCategory, name='category-list'),
    path('menuitems-list/', views.showAllMenuItems, name='menuitems-list'),
    path('itemassembly-list/', views.showAllItemassembly, name='itemassembly-list'),
    path('orderitems-list/', views.showAllOrderItems, name='orderitems-list'),
    path('order-list/', views.showAllOrder, name='order-list'),


    path('reservation-detail/<int:pk>/', views.viewReservation, name='reservation-detail'),
    path('location-detail/<int:pk>/', views.viewLocation, name='location-detail'),
    path('customer-detail/<int:pk>/', views.viewCustomers, name='customer-detail'),
    path('tables-detail/<int:pk>/', views.viewTables, name='tables-detail'),
    path('ingredients-detail/<int:pk>/', views.viewIngredients, name='ingredients-detail'),
    path('category-detail/<int:pk>/', views.viewCategory, name='category-detail'),
    path('menuitems-detail/<int:pk>/', views.viewMenuItems, name='menuitems-detail'),
    path('itemassembly-detail/<int:pk>/', views.viewItemassembly, name='itemassembly-detail'),
    path('orderitems-detail/<int:pk>/', views.viewOrderItems, name='orderitems-detail'),
    path('order-detail/<int:pk>/', views.viewOrder, name='order-detail'),


    path('reservation-create/', views.createReservation, name='reservation-create'),
    path('location-create/', views.createLocation, name='location-create'),
    path('customer-create/', views.createCustomers, name='customer-create'),
    path('tables-create/', views.createTables, name='tables-create'),
    path('ingredients-create/', views.createIngredients, name='ingredients-create'),
    path('category-create/', views.createCategory, name='category-create'),
    path('menuitems-create/', views.createMenuItems, name='menuitems-create'),
    path('itemassembly-create/', views.createItemassembly, name='itemassembly-create'),
    path('orderitems-create/', views.createOrderItems, name='orderitems-create'),
    path('order-create/', views.createOrder, name='order-create'),


    path('reservation-update/<int:pk>/', views.updateReservation, name='reservation-update'),
    path('location-update/<int:pk>/', views.updateLocation, name='location-update'),
    path('customer-update/<int:pk>/', views.updateCustomers, name='customer-update'),
    path('tables-update/<int:pk>/', views.updateTables, name='tables-update'),
    path('ingredients-update/<int:pk>/', views.updateIngredients, name='ingredients-update'),
    path('category-update/<int:pk>/', views.updateCategory, name='category-update'),
    path('menuitems-update/<int:pk>/', views.updateMenuItems, name='menuitems-update'),
    path('itemassembly-update/<int:pk>/', views.updateItemassembly, name='itemassembly-update'),
    path('orderitems-update/<int:pk>/', views.updateOrderItems, name='orderitems-update'),
    path('order-update/<int:pk>/', views.updateOrder, name='order-update'),


    path('reservation-delete/<int:pk>/', views.deleteReservation, name='reservation-delete'),
    path('location-delete/<int:pk>/', views.deleteLocation, name='location-delete'),
    path('customer-delete/<int:pk>/', views.deleteCustomers, name='customer-delete'),
    path('tables-delete/<int:pk>/', views.deleteTables, name='tables-delete'),
    path('ingredients-delete/<int:pk>/', views.deleteIngredients, name='ingredients-delete'),
    path('category-delete/<int:pk>/', views.deleteCategory, name='category-delete'),
    path('menuitems-delete/<int:pk>/', views.deleteMenuItems, name='menuitems-delete'),
    path('itemassembly-delete/<int:pk>/', views.deleteItemassembly, name='itemassembly-delete'),
    path('orderitems-delete/<int:pk>/', views.deleteOrderItems, name='orderitems-delete'),
    path('order-delete/<int:pk>/', views.deleteOrder, name='order-delete'),
]
