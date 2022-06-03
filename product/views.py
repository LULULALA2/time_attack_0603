from django.shortcuts import render
from .models import Category, Drink

# Create your views here.
def category_view(request, category):
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == 'POST':
        drink = Drink.objects.filter(category=category)
        return render(request, 'home.html', {'drink':drink})