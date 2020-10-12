from django.shortcuts import render
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import UserCreateSerializer, PlanSerializer, PlanItemSerializer, \
    UserPlanSerializer, PlanEmailSerializer
from .models import Plan, PlanItem, UserPlan, PlanEmail
import stripe
from decouple import config
from iquest.authentications import CsrfExemptSessionAuthentication
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

    permission_classes = [permissions.AllowAny]
    authentication_classes = [CsrfExemptSessionAuthentication]

    def post(self, request, pk=None):

        try:
            plan = Plan.objects.get(pk=pk)
            email = request.data.get("email")
            if not email:
                return Response({'message': 'email field is required'}, 400)
            plan_email = PlanEmail.objects.filter(email=email).first()
            if plan_email:
                return Response({'message': 'email has been registered'}, 400)
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'unit_amount': int(plan.price * 100),
                            'product_data': {
                                'name': plan.title,
                                # 'images': ['https://i.imgur.com/EHyR2nP.png'],
                            },
                        },
                        'quantity': 1,
                        'description': 'payment for iquest academy {}'.format(plan.title),
                    },
                ],
                customer_email=email,
                mode='payment',
                metadata=dict(plan_id=plan.pk),
                success_url=YOUR_DOMAIN + '?success=true',
                cancel_url=YOUR_DOMAIN + '?success=false',
            )
            print(checkout_session.id)
            return Response({'id': checkout_session.id})
        except Plan.DoesNotExist:
            return Response({'message': 'plan not found'}, 404)
        except Exception as e:
            print(str(e))
            return Response(dict(error=str(e)), 403)


class VerifyPayment(APIView):

    def post(self, request):
        session_id = request.data.get('session_id')

        if not session_id:
            return Response({'message': 'session id is required'}, 400)

        try:

            res = stripe.checkout.Session.retrieve(
                session_id
            )

            email = res['customer_email']
            plan_id = res['metadata']['plan_id']
            plan = Plan.objects.get(pk=plan_id)

            plan_email = PlanEmail.objects.create(
                email=email,
                plan=plan
            )

            return Response({"message": "purchase was successful"})
        except IntegrityError:
            return Response({'message': 'email has been registered'}, 400)
        except Plan.DoesNotExist:
            return Response({'message': 'plan does not exist'}, 400)
        except stripe.error.InvalidRequestError as error:
            return Response({'error': str(error)}, 400)


class PlanViewSet(ModelViewSet):

    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class PlanItemViewSet(ModelViewSet):

    queryset = PlanItem.objects.all()
    serializer_class = PlanItemSerializer


class UserPlanViewSet(ModelViewSet):

    queryset = UserPlan.objects.all()
    serializer_class = UserPlanSerializer


class PlanEmailViewSet(ModelViewSet):

    queryset = PlanEmail.objects.all()
    serializer_class = PlanEmailSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    return dict(token=token, userid=user.id)
