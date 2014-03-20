from django.contrib import admin

from data.models import Day, Sleep, HappyLog, UnhappyLog, Exercise, FoodScore, HappyScore

# Register your models here.
admin.site.register(Day)
admin.site.register(Sleep)
admin.site.register(HappyLog)
admin.site.register(UnhappyLog)
admin.site.register(Exercise)
admin.site.register(HappyScore)
admin.site.register(FoodScore)



