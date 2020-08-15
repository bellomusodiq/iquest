from rest_framework import serializers
from .models import (
    Home, Testimonial, Pioneer, SuccessStory, Leader,
    GetStarted, ScheduleCall, CallTime
)


class HomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Home
        fields = '__all__'


class TestimonialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Testimonial
        fields = '__all__'


class SuccessStorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SuccessStory
        fields = '__all__'


class LeaderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Leader
        fields = '__all__'


class PioneerSerializer(serializers.ModelSerializer):
    leaders = serializers.SerializerMethodField()
    success_stories = serializers.SerializerMethodField()

    class Meta:
        model = Pioneer
        fields = '__all__'

    def get_leaders(self, obj):
        leaders = []
        for leader in obj.leader_set.all():
            leaders.append(LeaderSerializer(leader).data)
        return leaders

    def get_success_stories(self, obj):
        success_stories = []
        for success_story in obj.successstory_set.all():
            success_stories.append(SuccessStorySerializer(success_story).data)
        return success_stories


class GetStartedSerializer(serializers.ModelSerializer):

    class Meta:
        model = GetStarted
        fields = '__all__'


class CallTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CallTime
        fields = '__all__'


class ScheduleCallSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScheduleCall
        fields = '__all__'
