from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *


class ProjectInline(admin.StackedInline):
    model = Project
    extra = 1


class SkillInline(admin.StackedInline):
    model = Skill
    extra = 1


class ContactInline(admin.StackedInline):
    model = Contact
    extra = 1


class SocialMediaHandleInline(admin.StackedInline):
    model = SocialMediaHandle
    extra = 1

class TestimonialInline(admin.StackedInline):
    model = Testimonial
    extra = 1

class ReplyInline(admin.StackedInline):
    model = Reply
    extra = 1


class UserAdmin(BaseUserAdmin):
    inlines = [ProjectInline, SkillInline, ContactInline, SocialMediaHandleInline, TestimonialInline, ReplyInline]


admin.site.register(User, UserAdmin)
