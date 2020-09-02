from django.contrib import admin

from .models import Dog, Feeding, Toy

# Register your models here.

admin.site.register(Dog)
admin.site.register(Feeding)
admin.site.register(Toy)