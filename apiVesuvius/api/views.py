from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/reservation-list/',
        'Detail View': '/reservation-detail/<int:id>',
        'Create': '/reservation-create/',
        'Update': '/reservation-update/<int:id>',
        'Delete': '/reservation-delete/<int:id>',
    }

    return Response(api_urls);


@api_view(['GET'])
def showAllReservations(request):
    reservation = Reservation.objects.all()
    serializer = ReservationSerializer(reservation, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def viewReservation(request, pk):
    reservation = Reservation.objects.get(id=pk)
    serializer = ReservationSerializer(reservation, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createReservation(request):
    serializer = ReservationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateReservation(request, pk):
    reservation = Reservation.objects.get(id=pk)
    serializer = ReservationSerializer(instance=reservation, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteReservation(request, pk):
    reservation = Reservation.objects.get(id=pk)
    reservation.delete()

    return Response('Reservation Deleted Successfully')


@api_view(['GET'])
def showAllLocations(request):
    location = Location.objects.all()
    serializer = LocationSerializer(location, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def viewLocation(request, pk):
    location = Location.objects.get(id=pk)
    serializer = LocationSerializer(location, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createLocation(request):
    serializer = LocationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateLocation(request, pk):
    location = Location.objects.get(id=pk)
    serializer = LocationSerializer(instance=location, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteLocation(request, pk):
    location = Location.objects.get(id=pk)
    location.delete()

    return Response('Location Deleted Successfully')


@api_view(['GET'])
def showAllCustomers(request):
    customers = Customers.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def viewCustomers(request, pk):
    customers = Customers.objects.get(id=pk)
    serializer = CustomerSerializer(customers, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createCustomers(request):
    serializer = CustomerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateCustomers(request, pk):
    customers = Customers.objects.get(id=pk)
    serializer = CustomerSerializer(instance=customers, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteCustomers(request, pk):
    customers = Customers.objects.get(id=pk)
    customers.delete()

    return Response('Customer Deleted Successfully')


@api_view(['GET'])
def showAllTables(request):
    tables = Tables.objects.all()
    serializer = TablesSerializer(tables, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def viewTables(request, pk):
    tables = Tables.objects.get(id=pk)
    serializer = TablesSerializer(tables, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createTables(request):
    serializer = TablesSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateTables(request, pk):
    tables = Tables.objects.get(id=pk)
    serializer = TablesSerializer(instance=tables, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteTables(request, pk):
    tables = Tables.objects.get(id=pk)
    tables.delete()

    return Response('Tables Deleted Successfully')


@api_view(['GET'])
def showAllIngredients(request):
    ingredients = Ingredients.objects.all()
    serializer = IngredientsSerializer(ingredients, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def viewIngredients(request, pk):
    ingredients = Ingredients.objects.get(id=pk)
    serializer = IngredientsSerializer(ingredients, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createIngredients(request):
    serializer = IngredientsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateIngredients(request, pk):
    ingredients = Ingredients.objects.get(id=pk)
    serializer = IngredientsSerializer(instance=ingredients, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteIngredients(request, pk):
    ingredients = Ingredients.objects.get(id=pk)
    ingredients.delete()

    return Response('Ingredients Deleted Successfully')


@api_view(['GET'])
def showAllCategory(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def viewCategory(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createCategory(request):
    serializer = CategorySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateCategory(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(instance=category, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteCategory(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()

    return Response('Category Deleted Successfully')


@api_view(['GET'])
def showAllMenuItems(request):
    menuItems = MenuItems.objects.all()
    serializer = MenuItemsSerializer(menuItems, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def viewMenuItems(request, pk):
    menuItems = MenuItems.objects.get(id=pk)
    serializer = MenuItemsSerializer(menuItems, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createMenuItems(request):
    serializer = MenuItemsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateMenuItems(request, pk):
    menuItems = MenuItems.objects.get(id=pk)
    serializer = MenuItemsSerializer(instance=menuItems, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteMenuItems(request, pk):
    menuItems = MenuItems.objects.get(id=pk)
    menuItems.delete()

    return Response('MenuItems Deleted Successfully')


@api_view(['GET'])
def showAllItemassembly(request):
    itemassembly = Itemassembly.objects.all()
    serializer = ItemAssemblySerializer(itemassembly, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def viewItemassembly(request, pk):
    itemassembly = Itemassembly.objects.get(id=pk)
    serializer = ItemAssemblySerializer(itemassembly, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createItemassembly(request):
    serializer = ItemAssemblySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateItemassembly(request, pk):
    itemassembly = Itemassembly.objects.get(id=pk)
    serializer = ItemAssemblySerializer(instance=itemassembly, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteItemassembly(request, pk):
    itemassembly = Itemassembly.objects.get(id=pk)
    itemassembly.delete()

    return Response('Itemassembly Deleted Successfully')



@api_view(['GET'])
def showAllOrderItems(request):
    orderItems = OrderItems.objects.all()
    serializer = OrderItemsSerializer(orderItems, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def viewOrderItems(request, pk):
    orderItems = OrderItems.objects.get(id=pk)
    serializer = OrderItemsSerializer(orderItems, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createOrderItems(request):
    serializer = OrderItemsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateOrderItems(request, pk):
    orderItems = OrderItems.objects.get(id=pk)
    serializer = OrderItemsSerializer(instance=orderItems, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteOrderItems(request, pk):
    orderItems = OrderItems.objects.get(id=pk)
    orderItems.delete()

    return Response('OrderItems Deleted Successfully')




@api_view(['GET'])
def showAllOrder(request):
    order = Order.objects.all()
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def viewOrder(request, pk):
    order = Order.objects.get(id=pk)
    serializer = OrderSerializer(order, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createOrder(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    serializer = OrderSerializer(instance=order, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()

    return Response('Order Deleted Successfully')


@api_view(['GET'])
def showAllEmployee(request):
    employee = Employee.objects.all()
    serializer = EmployeeSerializer(employee, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewEmployee(request, pk):
    employee = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createEmployee(request):
    serializer = EmployeeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateEmployee(request, pk):
    employee = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(instance=employee, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteEmployee(request, pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()

    return Response('Order Deleted Successfully')