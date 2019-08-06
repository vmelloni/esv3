from accounts.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class ProjectList(models.Model):
    """This is the model for a single project list"""
    name = models.CharField(_('list_name'), max_length=20, null=False)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='project_lists')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    estimate_mtv = models.DecimalField(max_digits=100, decimal_places=2, default=0.00, null=True)
    estimate_mtvm = models.DecimalField(max_digits=100, decimal_places=2, default=0.00, null=True)
    estimate_pcu = models.DecimalField(max_digits=100, decimal_places=2, default=0.00, null=True)

    class Meta:
        ordering = ('-date_created',)


class Activity(models.Model):
    """This is the model for a single activity in a project"""
    name = models.CharField(_('activity_name'), max_length=70, null=False)
    # optimist = models.DecimalField(_('purchase_price(KES'), max_digits=7, decimal_places=2, default=0.00)
    optimist = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=False)
    pessimist = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=False)
    average = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=False)
    # quantity = models.DecimalField(_('item_quantity'), max_digits=7, decimal_places=2, default=0.00)
    list = models.ForeignKey(
        ProjectList, on_delete=models.CASCADE, related_name='activity')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_created',)
