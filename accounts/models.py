from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver
import string
import random


# Create your models here.


User = get_user_model()


class Plan(models.Model):
    title = models.CharField(max_length=225)
    price = models.FloatField()

    def __str__(self):
        return self.title


class PlanItem(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)

    def __str__(self):
        return self.title


class PlanEmail(models.Model):
    email = models.EmailField(max_length=400, unique=True)
    code = models.CharField(max_length=200, blank=True, null=True)
    valid = models.BooleanField(default=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    def __str__(self):
        return self.email


def generate_token():
    token = ''
    for i in range(50):
        token += random.choice(string.ascii_letters + string.digits + string.hexdigits)
    return token


def generate_code(sender, instance, *args, **kwargs):
    if not instance.code:
        instance.code = generate_token()


# pre_save.connect(generate_code, sender=PlanEmail)


class UserPlan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
