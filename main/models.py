from django.db import models
from django.urls import reverse
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    meta_description = models.TextField(blank=True)

    slug = models.SlugField(max_length=200, db_index=True, unique=True , allow_unicode=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
            return self.name

    def get_absolute_url(self):
            return reverse('main:places_in_category', args=[self.slug])


class Place(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='places')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    image = models.ImageField(upload_to='images/%Y/%m/%d', default='images/no_image.png')
    description = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)

    address = models.CharField(max_length=200, db_index=True, default='제주')

    available_display = models.BooleanField('Display', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        index_together = [['id', 'slug']]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:places_detail', args=[self.id, self.slug])

class Comment(models.Model):
    places = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


