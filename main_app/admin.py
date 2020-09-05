from django.contrib import admin

from .models import Dog, Feeding, Toy, Photo

# Register your models here.

admin.site.register(Dog)
admin.site.register(Feeding)
admin.site.register(Toy)
admin.site.register(Photo)