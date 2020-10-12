from django.contrib import admin
from .models import Plan, PlanItem, UserPlan, PlanEmail
# Register your models here.


admin.site.register(Plan)
admin.site.register(PlanItem)
admin.site.register(UserPlan)
admin.site.register(PlanEmail)
