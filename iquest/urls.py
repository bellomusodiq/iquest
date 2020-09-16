"""iquest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from home_template.views import (
    HomeView, TestimonialView, PioneerView,
    GetStartedView, ScheduleCallViewSet,
    CallTimeViewSet
)

from accounts.views import UserCreateView, CreateStripeSession

from dashboard.views import DashboardView, UserDashboardView, PhaseView, TrainingView, \
    MaterialViewSet
from django.views.generic.base import TemplateView

router = DefaultRouter()

router.register('schedule-call', ScheduleCallViewSet, 'schedule-call')
router.register('call-time', CallTimeViewSet, 'call-time')
router.register('materials', MaterialViewSet, 'materials')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/home/', HomeView.as_view()),
    path('api/testimonial/', TestimonialView.as_view()),
    path('api/pioneer/', PioneerView.as_view()),
    path('api/get-started/', GetStartedView.as_view()),
    path('api/dashboard/', DashboardView.as_view()),
    path('api/user-dashboard/', UserDashboardView.as_view()),
    path('api/trainings/', TrainingView.as_view()),
    path('api/phase/<int:phase>/', PhaseView.as_view()),
    path('api/user-create/', UserCreateView.as_view()),
    path('api/user-create/<int:pk>/', UserCreateView.as_view()),
    path('api/login/', obtain_jwt_token),
    path('create-session/', CreateStripeSession.as_view())
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
