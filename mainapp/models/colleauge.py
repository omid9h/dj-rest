from django.db import models
from django.utils.translation import gettext_lazy as gt_l
from common.models import BaseModel


class ColleagueStatus(models.TextChoices):
    """
    Django enumeration for choices of Colleague model status
    """
    ACTIVE = 'ACTIVE', gt_l('Active')
    INACTIVE = 'INACTIVE', gt_l('Inactive')


class ColleagueStatusReason(models.TextChoices):
    """
    Django enumeration for choices of ColleagueStatusHistory model reason
    """
    END_CONTRACT = 'END_CONTRACT', gt_l('Contract has ended')
    TERMINATE_BY_COLLEAGUE = 'TERMINATE_BY_COLLEAGUE', gt_l('Contract has been terminated by colleague')
    TERMINATE_BY_COMPANY = 'TERMINATE_BY_COMPANY', gt_l('Contract has been terminated by company')


class Colleague(BaseModel):
    """
    Colleague model
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
    status = models.CharField(
        gt_l('Status'),
        choices=ColleagueStatus.choices,
        default=ColleagueStatus.ACTIVE,
        max_length=10,
        blank=False,
        null=False
    )

    def __str__(self):
        return f'{self.name} - {self.email}'


class ColleagueStatusHistory(BaseModel):
    """
    Colleague status history model
    """
    colleague = models.ForeignKey(
        Colleague,
        on_delete=models.CASCADE,
        related_name='status_history',
        blank=False,
        null=False
    )
    status = models.CharField(
        gt_l('Status'),
        choices=ColleagueStatus.choices,
        default=ColleagueStatus.ACTIVE,
        max_length=10,
        blank=False,
        null=False
    )
    reason = models.CharField(
        gt_l('Reason'),
        choices=ColleagueStatusReason.choices,
        max_length=50,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.colleague} - {self.status}'


class ColleagueCustomerMap(BaseModel):
    """
    Colleague-Customer mapping model
    """
    colleague = models.ForeignKey(
        Colleague,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    customer = models.ForeignKey(
        'Customer',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    colleague_status = models.CharField(
        gt_l('Colleague Status'),
        choices=ColleagueStatus.choices,
        default=ColleagueStatus.ACTIVE,
        max_length=10,
        blank=False,
        null=False
    )
