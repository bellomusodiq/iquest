from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer
import stripe
from decouple import config
# Create your views here.


stripe.api_key = config('STRIPE_SECRET')
YOUR_DOMAIN = 'http://localhost:3000/checkout'


class UserCreateView(APIView):

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        user = User.objects.filter(pk=pk).first()
        if not user:
            return Response({'message': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserCreateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'user created successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None):
        user = User.objects.filter(pk=pk).first()
        if not user:
            return Response({'message': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(UserCreateSerializer(user).data)


class CreateStripeSession(APIView):

    def post(self, request):

        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'unit_amount': 2000,
                            'product_data': {
                                'name': 'Stubborn Attachments',
                                'images': ['https://i.imgur.com/EHyR2nP.png'],
                            },
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=YOUR_DOMAIN + '?success=true',
                cancel_url=YOUR_DOMAIN + '?canceled=true',
            )
            return Response({'id': checkout_session.id})
        except Exception as e:
            print(str(e))
            return Response(dict(error=str(e)), 403)


def jwt_response_payload_handler(token, user=None, request=None):
    return dict(token=token, userid=user.id)
