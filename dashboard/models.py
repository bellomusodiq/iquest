from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Dashboard(models.Model):
    notification = models.CharField(max_length=400)
    phase1_title = models.CharField(max_length=100, default='')
    phase1_sub_title = models.CharField(max_length=100, default='')
    phase1_description = models.TextField()
    phase2_title = models.CharField(max_length=100, default='')
    phase2_sub_title = models.CharField(max_length=100, default='')
    phase2_description = models.TextField()
    phase3_title = models.CharField(max_length=100, default='')
    phase3_sub_title = models.CharField(max_length=100, default='')
    phase3_description = models.TextField()


class Announcement(models.Model):
    date = models.DateField()
    content = models.CharField(max_length=400)

    def __str__(self):
        return str(self.date) + ' ' + self.content

    class Meta:
        ordering = ['-date']


class UpcommingEvent(models.Model):
    date = models.DateField()
    content = models.CharField(max_length=400)

    def __str__(self):
        return str(self.date) + ' ' + self.content

    class Meta:
        ordering = ['date']


class PhaseContent(models.Model):
    phase = models.CharField(max_length=20,
                             choices=(('phase 1', 'phase 1'), ('phase 2', 'phase 2'), ('phase 3', 'phase 3')))
    title = models.CharField(max_length=200)
    poster = models.ImageField(upload_to='images/phase')
    video = models.FileField(upload_to='videos/phase')
    time = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.phase + ' ' + str(self.pk)


class UserDashboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phase1_progress = models.PositiveIntegerField(default=0)
    phase2_progress = models.PositiveIntegerField(default=0)
    phase3_progress = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username


class TrainingContent(models.Model):
    title = models.CharField(max_length=200)
    poster = models.ImageField(upload_to='images/phase')
    video = models.FileField(upload_to='videos/phase')
    time = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Material(models.Model):
    title = models.CharField(max_length=255)
    material_type = models.CharField(max_length=20, choices=(('PNG', 'PNG'),('PDF', 'PDF'),('PPT', 'PPT')))
    file = models.FileField(upload_to='materials/files')

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.title


@receiver(post_save, sender=User)
def create_user_dashboard(sender, instance, created, *args, **kwargs):
    if created:
        UserDashboard.objects.create(user=instance)
