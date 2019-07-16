from django.shortcuts import render

def place_in_category(request):
    return render(request,'main:list.html')

