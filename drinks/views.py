from django.http.response import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect, render

@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    
    if request.method == 'GET':
        drinks = Drink.objects.all()
        return render(request, 'all.html', {'drinks': drinks})

# fromat je zbog jsona i zbog toga sto je u urls.py format_suffix_patterns

@api_view(['GET'])
def add_drink(request, format=None):
    if request.method == 'GET':
        return render(request, 'add.html', {})

@api_view(['POST'])
def placeDrink(request, format=None):
    if request.method == 'POST':
        drinkData = request.data
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'add.html', {'drinks': drinkData})
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
def updateTemplate(request, format=None):
    if request.method == 'GET':
        drink: Drink.objects.get(pk=id)
        return render(request, 'update.html', {'drinks': drink})

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None): 
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response({'message': 'The drink does not exist'}, status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return render(request, 'hello.html', {'drinks': drink})

    elif request.method == 'DELETE':
        drink.delete()
        return Response({'message': 'Drink was deleted successfully!'}, status.HTTP_204_NO_CONTENT)