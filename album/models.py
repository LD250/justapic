from django.db import models
from django.conf import settings

from django.contrib.auth.models import User

class UserAlbum(models.Model):
    user = models.ForeignKey(User, related_name='useralbum')
    photo = models.ImageField(upload_to=settings.UPLOAD_IMAGES_DIR)
