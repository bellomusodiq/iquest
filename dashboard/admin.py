from django.contrib import admin
from .models import Dashboard, Announcement, UserDashboard, UpcommingEvent, PhaseContent, \
    TrainingContent, Material
# Register your models here.


admin.site.register(Dashboard)
admin.site.register(Announcement)
admin.site.register(UserDashboard)
admin.site.register(UpcommingEvent)
admin.site.register(PhaseContent)
admin.site.register(TrainingContent)
admin.site.register(Material)
