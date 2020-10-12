from django.contrib.auth.models import User
from rest_framework import serializers
from .models import PlanItem, Plan, UserPlan, PlanEmail


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=200)
    password = serializers.CharField(max_length=100)

    def validate_username(self, value):
        if value == 'bell':
            raise serializers.ValidationError('play')
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        # username availability check
        user = User.objects.filter(username=username).first()
        if user:
            raise serializers.ValidationError({'username': 'user with this username already exists'})
        user = User.objects.filter(email=email).first()
        if user:
            raise serializers.ValidationError({'email': 'user with this email already exists'})
        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
        return user

    def validate(self, attrs):
        # raise serializers.ValidationError('user with this username already exists')
        return attrs

    def update(self, instance, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        user = User.objects.filter(username=username).first()
        if user and (user.pk != instance.pk):
            raise serializers.ValidationError({'username': 'user with this username already exists'})
        user = User.objects.filter(email=email).first()
        if user and (user.pk != instance.pk):
            raise serializers.ValidationError({'email': 'user with this email already exists'})
        if validated_data.get('password'):
            instance.set_password(validated_data['password'])
        instance.save()

        return instance


class PlanSerializer(serializers.ModelSerializer):

    plan_items = serializers.SerializerMethodField()

    class Meta:
        fields = '__all__'
        model = Plan

    def get_plan_items(self, obj):
        items = []
        for item in obj.planitem_set.all():
            items.append(PlanItemSerializer(item).data)
        return items


class PlanItemSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = PlanItem


class UserPlanSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = UserPlan


class PlanEmailSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = PlanEmail
