from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=255)
  
  class Meta:
    ordering = ('name',) # Order items alphabetically in the admin panel 
    verbose_name_plural = 'Categories' # Fixes 'Categorys' to 'Categories'
  
  def __str__ (self):
    return self.name # In order to display 'name' property of Category model, instead of hard-string 'Category object (1)' in the admin panel

class Item(models.Model):
  # 'on_delete=models.CASCADE' means, for example, if the category is deleted, the items belonging to the category will also be deleted
  category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  description = models.TextField(blank=True, null=True)
  price = models.FloatField()
  image = models.ImageField(upload_to='item_images', blank=True, null=True) # One needs 'Pillow' library in order to use ImageField
  is_sold = models.BooleanField(default=False)
  created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__ (self):
    return self.name
