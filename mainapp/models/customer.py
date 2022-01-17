import email
from pyexpat import model
from django.db import models
from django.utils.translation import gettext_lazy as gt_l
from common.models import BaseModel


class Customer(BaseModel):
    """
    Customer model
    """
    name = models.CharField(
        gt_l('Name'),
        max_length=200,
        blank=False,
        null=False
    )
    email = models.EmailField(
        gt_l('Email'),
        blank=False,
        null=False
    )
