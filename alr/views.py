from django.shortcuts import render
from store.models import Product, ReviewRating

def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('-created_date')

    # get the reviews
    reviews = ReviewRating.objects.filter(product_id=products)

    context = {
        'products':products,'reviews':reviews
    }   
    return render(request, 'home.html',context)