from django.contrib import admin
from core.models import Contact, Destination, State, Slider,News,Dataset
# Register your models here.


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'img', 'desc', 'price')


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'img')
    
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','day', 'month','title','news_pic','news_desc')
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email','subject','message','date')

@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = ('id','SUBDIVISION','YEAR','JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC','ANNUAL',"Jan_Feb","Mar_May","Jun_Sep","Oct_Dec")
