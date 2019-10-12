from accounts.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class ProjectList(models.Model):
    """This is the model for a single project list"""
    name = models.CharField(_('list_name'), max_length=80, null=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='project_lists')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    estimate_mtv = models.DecimalField(max_digits=100, decimal_places=2, default=0.00, null=True)
    estimate_mtvm = models.DecimalField(max_digits=100, decimal_places=2, default=0.00, null=True)
    estimate_pcu = models.DecimalField(max_digits=100, decimal_places=2, default=0.00, null=True)

    # averageValue = models.DecimalField(max_digits=100, decimal_places=2, default=0.00, null=True)

    class Meta:
        ordering = ('-date_created',)


class Component(models.Model):
    """This is the model for a single Component in a project"""
    name = models.CharField(_('Component_name'), max_length=70, null=True)
    list = models.ForeignKey(
        ProjectList, on_delete=models.CASCADE)
    optimist = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
    pessimist = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
    average = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    riskValue = models.IntegerField(default=1, null=True)
    actorsAmount = models.IntegerField(default=0, null=True)

    class Meta:
        ordering = ('-createdDate',)


class UseCase(models.Model):
    """This is the model for Use Cases in a project"""
    idComponent = models.ForeignKey(
        Component, on_delete=models.CASCADE)
    name = models.CharField(_('usecase_name'), max_length=100, null=True)
    actorsAmount = models.IntegerField(default=0, null=True)


class TechFactors(models.Model):
    """This is the model for the technical factors in a project"""
    idProject = models.ForeignKey(
        ProjectList, on_delete=models.CASCADE)
    distributedSystem = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
    responseTime = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
    endUserEfficency = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
    complexInternalProcessing = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
    reusableCode = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
    installationEasiness = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
    usability = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
    crossPlatformSupport = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
    easyToChange = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
    highlyConcurrent = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
    customSecurity = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
    dependenceThirdPartyCode = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
    userTraining = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)


class EnvFactors(models.Model):
    """This is the model for the environmental factors in a project"""
    idProject = models.ForeignKey(
        ProjectList, on_delete=models.CASCADE)
    familiarityWithTheProject = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
    applicationExperience = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
    objectOrientedProgrammingExperience = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
    leadAnalystCapability = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
    motivation = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
    stableRequirements = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
    partTimeStaff = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)
    difficultProgrammingLanguage = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)


# class ComponentR(Component):
#     risk = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=True)


class Estimate(models.Model):
    ESTIMATE_CHOICES = [
        ('1', 'MTV'),
        ('2', 'MTVM'),
        ('3', 'RePCU'),
    ]
    type_estimate = models.CharField(max_length=1, choices=ESTIMATE_CHOICES)
