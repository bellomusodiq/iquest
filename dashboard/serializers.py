from rest_framework import serializers
from .models import (
    Dashboard, Announcement, UpcommingEvent,
    PhaseContent, UserDashboard, TrainingContent,
    Material
)


class AnnouncementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Announcement
        fields = '__all__'


class UpcommingEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = UpcommingEvent
        fields = '__all__'


class PhaseContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhaseContent
        fields = '__all__'


class DashboardSerializer(serializers.ModelSerializer):
    announcements = serializers.SerializerMethodField()
    upcomming_events = serializers.SerializerMethodField()

    class Meta:
        model = Dashboard
        fields = '__all__'

    def get_announcements(self, obj):
        announcements = []
        for announcement in Announcement.objects.all():
            announcements.append(AnnouncementSerializer(announcement).data)
        return announcements

    def get_upcomming_events(self, obj):
        upcomming_events = []
        for u in UpcommingEvent.objects.all():
            upcomming_events.append(UpcommingEventSerializer(u).data)
        return upcomming_events


class UserDashboardSerializer(serializers.ModelSerializer):
    phase1_progress_percentage = serializers.SerializerMethodField()
    phase2_progress_percentage = serializers.SerializerMethodField()
    phase3_progress_percentage = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()

    class Meta:
        model = UserDashboard
        fields = '__all__'

    def get_username(self, obj):
        return obj.user.username

    def get_phase1_progress_percentage(self, obj):
        phase_count = PhaseContent.objects.filter(phase='phase 1').count()
        try:
            return obj.phase1_progress / phase_count
        except ZeroDivisionError:
            return 0

    def get_phase2_progress_percentage(self, obj):
        phase_count = PhaseContent.objects.filter(phase='phase 2').count()
        try:
            return obj.phase2_progress / phase_count
        except ZeroDivisionError:
            return 0

    def get_phase3_progress_percentage(self, obj):
        phase_count = PhaseContent.objects.filter(phase='phase 3').count()
        try:
            return obj.phase3_progress / phase_count
        except ZeroDivisionError:
            return 0


class TrainingSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrainingContent
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material
        fields = '__all__'
