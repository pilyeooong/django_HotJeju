from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns =[
    path('', places_in_category , name='All_places'),
    path('<slug:category_slug>/', places_in_category, name='places_in_category'),
    path('<int:id>/<places_slug>/', places_detail , name='places_detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)