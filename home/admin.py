from django.contrib import admin
from .models import *

# Register your models here.

urlpatterns = [
    admin.site.register(receipe)
]
