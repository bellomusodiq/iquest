from django.contrib import admin
from .models import (
    Home, Testimonial, SuccessStory, Pioneer, Leader,
    ScheduleCall, GetStarted, CallTime
)
# Register your models here.


admin.site.register(Home)
admin.site.register(Testimonial)
admin.site.register(SuccessStory)
admin.site.register(Pioneer)
admin.site.register(Leader)
admin.site.register(ScheduleCall)
admin.site.register(GetStarted)
admin.site.register(CallTime)
