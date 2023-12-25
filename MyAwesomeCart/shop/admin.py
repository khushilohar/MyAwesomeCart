from django.contrib import admin

# Register your models here.
from .models import Product

admin.site.register(Product)

from .models import Contact

admin.site.register(Contact)

from .models import Orders
admin.site.register(Orders)
