import os
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


def generate_uuid_for_file_with_dir(original_file_name: str, upload_dir: str):
    """
    generates a uuid name for given file and concats it to given dir
    Example: <upload_dir>/193f511b-6061-4b03-b136-2d5fa1b3b39b<.extension>
    """
    extension = original_file_name.split(".")[-1]
    file_name = f"{uuid.uuid4()}.{extension}"
    return os.path.join(upload_dir, file_name)


class BaseModel(models.Model):
    """
    base model for all other models
    """

    is_active = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    """
    user model explicitly implemented for future enhancements
    """

    pass
