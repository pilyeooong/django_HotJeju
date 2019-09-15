from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import places_in_category,

app_name = 'main'

urlpatterns =[
    path('', places_in_category , name='All_places'),
    path('notice/' ,notice_list, name='notice_list'),
    path('notice/add/' ,add_notice, name='add_notice'),
    path('notice/<int:id>' ,notice_detail, name='notice_detail'),
    path('add/', AddPlacesView.as_view(), name='add_places'),
    path('<slug:category_slug>/', places_in_category, name='places_in_category'),
    path('<int:id>/<places_slug>/', places_detail , name='places_detail'),
    path('<int:id>/<places_slug>/delete/', delete_places , name='delete_places'),
    path('<int:id>/<places_slug>/comment/', add_comment, name='add_comment'),
    path('<int:id>/<places_slug>/comment/<int:comment_id>/', edit_comment, name='edit_comment'),
    path('<int:id>/<places_slug>/comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
