from django.shortcuts import render, get_object_or_404
from .models import *

def places_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    places = Place.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        places = places.filter(category=current_category)
    
    return render(request,'main/list.html', {'current_category': current_category, 'categories': categories, 'places': places})


def places_detail(request, id, places_slug=None):
    places = get_object_or_404(Place, id=id, slug=places_slug)
    return render(request, 'main/detail.html', {'places': places})
    