from django.contrib import admin
from .models import PrimaryTable,SecondTable,ThirdTable,FourthTable
# Register your models here.
admin.site.register(PrimaryTable)
admin.site.register(SecondTable)
admin.site.register(ThirdTable)