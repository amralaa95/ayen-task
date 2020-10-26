from __future__ import unicode_literals
import os
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


def user_directory_path(instance, filename):
    return f'user_{instance.user.id}/{filename}'



def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.pptx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension only pdf or pptx.')


class Document(models.Model):
    user = models.ForeignKey(User, related_name='documents', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    document = models.FileField(upload_to=user_directory_path, validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)
