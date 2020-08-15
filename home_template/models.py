from django.db import models

# Create your models here.


class Home(models.Model):
    heading1 = models.CharField(max_length=400)
    text1 = models.TextField()
    image1 = models.ImageField(upload_to='home/images')

    about_heading = models.CharField(max_length=400)
    about_text = models.TextField()
    about_poster = models.ImageField(upload_to='home/images')
    about_video = models.FileField(upload_to='home/videos')

    our_way_heading = models.CharField(max_length=400)
    forex_text = models.TextField()
    crypto_text = models.TextField()

    learning_heading = models.CharField(max_length=400)
    learning_text = models.TextField()
    learning_poster = models.ImageField(upload_to='home/images')
    learning_video = models.FileField(upload_to='home/videos')

    learning_item1 = models.CharField(max_length=400)
    learning_item2 = models.CharField(max_length=400)
    learning_item3 = models.CharField(max_length=400)
    learning_item4 = models.CharField(max_length=400)

    testimonial_heading = models.CharField(max_length=400)
    testimonial_text = models.TextField()
    testimonial_image1 = models.ImageField(upload_to='home/images')
    testimonial_image2 = models.ImageField(upload_to='home/images')
    testimonial_image3 = models.ImageField(upload_to='home/images')
    
    facebook_url = models.URLField()
    twitter_url = models.URLField()
    instagram_url = models.URLField()


class Testimonial(models.Model):
    heading = models.CharField(max_length=400)
    poster1 = models.ImageField(upload_to='testimonial/images')
    poster2 = models.ImageField(upload_to='testimonial/images')
    poster3 = models.ImageField(upload_to='testimonial/images')
    video1 = models.FileField(upload_to='testimonial/videos')
    video2 = models.FileField(upload_to='testimonial/videos')
    video3 = models.FileField(upload_to='testimonial/videos')
    pips_in_profit = models.IntegerField(default=0)
    accuracy = models.IntegerField(default=0)
    trades_per_week = models.CharField(max_length=20)


class Pioneer(models.Model):
    heading = models.CharField(max_length=400)
    schedule_text = models.TextField()


class Leader(models.Model):
    pioneer = models.ForeignKey(Pioneer, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='pioneers/images')
    description = models.CharField(max_length=400)


class SuccessStory(models.Model):
    pioneer = models.ForeignKey(Pioneer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pioneers/images')


class GetStarted(models.Model):
    heading = models.CharField(max_length=400)
    how_to_start = models.TextField()
    webinar_image = models.ImageField(upload_to='get_started/images')
    get_started_text = models.TextField()


class CallTime(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        get_latest_by = ['-pk']

    def __str__(self):
        return self.title


class ScheduleCall(models.Model):
    email = models.EmailField(max_length=400)
    phone_no = models.CharField(max_length=20)
    call_time = models.ForeignKey(CallTime, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.phone_no + ' ' + self.call_time
