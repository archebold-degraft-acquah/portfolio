from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save


class User(AbstractUser):
    profile_picture = models.ImageField(upload_to="images/profile/", blank=True, null=True)
    bio = models.TextField()


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="images/projects/", blank=True, null=True)
    project_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SocialMediaHandle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    network_name = models.CharField(max_length=255)
    network_url = models.URLField()

    def __str__(self):
        return self.network_name


class Reply(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    to_user = models.ForeignKey(Contact, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.subject



@receiver(post_save, sender=Reply)
def send_email(sender, instance, created, **kwargs):
    if created:
        send_mail(instance.subject, instance.message, instance.from_user.email, [instance.to_user.email])
