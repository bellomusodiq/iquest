from django.shortcuts import render
from .models import (
    Home, Testimonial, Pioneer, GetStarted,
    ScheduleCall, CallTime
)
from .serializers import (
    HomeSerializer, TestimonialSerializer, PioneerSerializer,
    GetStartedSerializer, ScheduleCallSerializer, CallTimeSerializer
)
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class HomeView(APIView):

    def get(self, request):
        home_obj = Home.objects.first()
        if home_obj:
            return Response(HomeSerializer(home_obj).data, status=status.HTTP_200_OK)
        return Response({'message': 'home object not set'}, status=status.HTTP_404_NOT_FOUND)


class TestimonialView(APIView):

    def get(self, request):
        testimonial_obj = Testimonial.objects.first()
        home_obj = Home.objects.first()
        if testimonial_obj:
            res = TestimonialSerializer(testimonial_obj).data
            res = {**res, 'facebook_url': home_obj.facebook_url,
                   'instagram_url': home_obj.instagram_url,
                   'twitter_url': home_obj.twitter_url}
            return Response(res, status=status.HTTP_200_OK)
        return Response({'message': 'home object not set'}, status=status.HTTP_404_NOT_FOUND)


class PioneerView(APIView):

    def get(self, request):
        pioneer_obj = Pioneer.objects.first()
        home_obj = Home.objects.first()
        if pioneer_obj:
            res = PioneerSerializer(pioneer_obj).data
            res = {**res, 'facebook_url': home_obj.facebook_url,
                   'instagram_url': home_obj.instagram_url,
                   'twitter_url': home_obj.twitter_url}
            return Response(res, status=status.HTTP_200_OK)
        return Response({'message': 'home object not set'}, status=status.HTTP_404_NOT_FOUND)


class GetStartedView(APIView):

    def get(self, request):
        pioneer_obj = GetStarted.objects.first()
        home_obj = Home.objects.first()
        if pioneer_obj:
            res = GetStartedSerializer(pioneer_obj).data
            res = {**res, 'facebook_url': home_obj.facebook_url,
                   'instagram_url': home_obj.instagram_url,
                   'twitter_url': home_obj.twitter_url}
            return Response(res, status=status.HTTP_200_OK)
        return Response({'message': 'home object not set'}, status=status.HTTP_404_NOT_FOUND)


class ScheduleCallViewSet(ModelViewSet):
    queryset = ScheduleCall.objects.all()
    serializer_class = ScheduleCallSerializer


class CallTimeViewSet(ModelViewSet):
    queryset = CallTime.objects.all()
    serializer_class = CallTimeSerializer
