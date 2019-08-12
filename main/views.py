from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.views.generic.edit import CreateView
from django.utils.text import slugify   

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
    
def add_comment(request, id, places_slug=None):
    places = get_object_or_404(Place, id=id, slug=places_slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.places = places
            comment.save()
            return render(request, 'main/detail.html', {'places':places})
    else:
        form = CommentForm()
    return render(request, 'main/add_comment.html', {'form':form})


class AddPlacesView(CreateView):
    model = Place
    fields = ['category', 'name', 'image', 'description', 'address',]
    template_name = 'main/add_places.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.slug = slugify(form.instance.name, allow_unicode=True)
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})


def notice_list(request):
    notices = Notice.objects.all().order_by('-created_date')
    return render(request,'main/notice_list.html', {'notices': notices})

def notice_detail(request, id):
    notices = get_object_or_404(Notice, id=id)
    return render(request, 'main/notice_detail.html', {'notices': notices})