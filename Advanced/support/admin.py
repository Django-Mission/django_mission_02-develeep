from django.contrib import admin
from .models import Inquiry
from .models import Answer

# Register your models here.
admin.site.register(Inquiry)
admin.site.register(Answer)
