from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import ProjectList, Component, Estimate, TechFactors, EnvFactors, Actors, UseCase


class ProjectListForm(ModelForm):
    class Meta:
        model = ProjectList

        fields = ("name", "owner", "time")
        labels = {
            "name": _("Nombre del proyecto"),
            "time": _("Unidad de tiempo")
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nombre",
                "autocomplete": "random_name",
            }),
            "time": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Unidad de tiempo",
                "autocomplete": "random_name",
            }),
            "owner": forms.TextInput(attrs={
                "placeholder": "owner id ",
                "autocomplete": "random_name",
                "input_type": 'hidden',
            }),

        }


class UpdateProjectListForm(ModelForm):
    class Meta:
        model = ProjectList
        fields = ("name",)
        labels = {
            "name": _("Nombre del proyecto")
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nombre",
                "autocomplete": "random_name",
            }),
            "list": forms.TextInput(attrs={
                "placeholder": "list id ",
                "autocomplete": "random_name",
                "input_type": 'hidden',
            }),
        }


class ComponentForm(ModelForm):
    class Meta:
        model = Component
        fields = ("name", "list",)
        labels = {
            "name": _("Componente"),
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control testclass",
                "placeholder": "Nombre del componente",
                "autocomplete": "random_name",
            }),
            "list": forms.TextInput(attrs={
                "autocomplete": "random_name",
                "input_type": 'hidden',
            }),
        }


class ComponentUpdateForm(ModelForm):
    class Meta:
        model = Component
        fields = ("name", "id")
        labels = {
            "name": _("Component"),
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Componente",
                "autocomplete": "random_name",
            }),
            "id": forms.TextInput(attrs={
                "placeholder": "id",
                "autocomplete": "random_name",
                "input_type": 'hidden',
            }),
        }


class ProjectDeleteForm(ModelForm):
    class Meta:
        model = ProjectList
        fields = ("id",)
        labels = {
            "name": _("Project Name")
        }
        widgets = {
            "id": forms.TextInput(attrs={
                "autocomplete": "random_name",
                "input_type": 'hidden',
            }),
        }


class EstimateForm(ModelForm):
    ESTIMATE_CHOICES = [
        ('1', 'MTV'),
        ('2', 'MTVM'),
        ('3', 'RePCU'),
    ]

    class Meta:
        model = Estimate
        fields = ("type_estimate",)

    labels = {
        "type_estimate": _("Component"),
    }

    widgets = {
        'estimate': forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple,
                                              choices=ESTIMATE_CHOICES, )
    }


class ActorsForm(ModelForm):
    class Meta:
        model = Actors
        fields = ("simple", "average", "complex", "critical",)
        labels = {
            "name": _("Actors"),
        }
        widgets = {
            "simple": forms.TextInput(attrs={
                "class": "form-control testclass",
                "placeholder": "simple",
                "autocomplete": "random_name",
            }),
            "average": forms.TextInput(attrs={
                "class": "form-control testclass",
                "placeholder": "promedio",
                "autocomplete": "random_name",
            }),
            "complex": forms.TextInput(attrs={
                "class": "form-control testclass",
                "placeholder": "complejo",
                "autocomplete": "random_name",
            }),
            "critical": forms.TextInput(attrs={
                "class": "form-control testclass",
                "placeholder": "crítico",
                "autocomplete": "random_name",
            }),
        }


class TechFactorsForm(ModelForm):
    class Meta:
        model = TechFactors
        fields = ("distributedSystem", "responseTime", "endUserEfficency", "complexInternalProcessing",
                  "reusableCode", "installationEasiness", "usability", "crossPlatformSupport",
                  "easyToChange", "highlyConcurrent", "customSecurity", "dependenceThirdPartyCode",
                  "userTraining",)
        labels = {
            "name": _("TechFactors"),
        }
        widgets = {
            "distributedSystem": forms.TextInput(attrs={
                "class": "form-control testclass",
                "autocomplete": "random_name",
            }),
            "responseTime": forms.TextInput(attrs={
                "class": "form-control testclass",
                "autocomplete": "random_name",
            }),
            "endUserEfficency": forms.TextInput(attrs={
                "class": "form-control testclass",
                "autocomplete": "random_name",
            }),
            "complexInternalProcessing": forms.TextInput(attrs={
                "class": "form-control testclass",
                "autocomplete": "random_name",
            }),
            "reusableCode": forms.TextInput(attrs={
                "class": "form-control testclass",
                "autocomplete": "random_name",
            }),
            "installationEasiness": forms.TextInput(attrs={
                "class": "form-control testclass",
                "autocomplete": "random_name",
            }),
            "usability": forms.TextInput(attrs={
                "class": "form-control testclass",
                "autocomplete": "random_name",
            }),
            "crossPlatformSupport": forms.TextInput(attrs={
                "class": "form-control testclass",
                "autocomplete": "random_name",
            }),
            "easyToChange": forms.TextInput(attrs={
                "class": "form-control testclass",
                "autocomplete": "random_name",
            }),
            "highlyConcurrent": forms.TextInput(attrs={
                "class": "form-control testclass",
                "autocomplete": "random_name",
            }),
            "customSecurity": forms.TextInput(attrs={
                "class": "form-control testclass",
                "autocomplete": "random_name",
            }),
            "dependenceThirdPartyCode": forms.TextInput(attrs={
                "class": "form-control testclass",
                "autocomplete": "random_name",
            }),
            "userTraining": forms.TextInput(attrs={
                "class": "form-control testclass",
                "autocomplete": "random_name",
            }),
        }


class EnvFactorsForm(ModelForm):
    class Meta:
        model = EnvFactors
        fields = ("familiarityWithTheProject", "applicationExperience", "objectOrientedProgrammingExperience",
                  "leadAnalystCapability", "motivation", "stableRequirements", "partTimeStaff",
                  "difficultProgrammingLanguage",)
        labels = {
            "name": _("EnvFactors"),
        }
        widgets = {
            "familiarityWithTheProject": forms.TextInput(attrs={
                "class": "form-control testclass",
                "autocomplete": "random_name",
            }),
            "applicationExperience": forms.TextInput(attrs={
                "class": "form-control testclass",
                "autocomplete": "random_name",
            }),
            "objectOrientedProgrammingExperience": forms.TextInput(attrs={
                "class": "form-control testclass",
                "autocomplete": "random_name",
            }),
            "leadAnalystCapability": forms.TextInput(attrs={
                "class": "form-control testclass",
                "autocomplete": "random_name",
            }),
            "motivation": forms.TextInput(attrs={
                "class": "form-control testclass",
                "autocomplete": "random_name",
            }),
            "stableRequirements": forms.TextInput(attrs={
                "class": "form-control testclass",
                "autocomplete": "random_name",
            }),
            "partTimeStaff": forms.TextInput(attrs={
                "class": "form-control testclass",
                "autocomplete": "random_name",
            }),
            "difficultProgrammingLanguage": forms.TextInput(attrs={
                "class": "form-control testclass",
                "autocomplete": "random_name",
            }),
        }


class UseCaseAddForm(ModelForm):
    class Meta:
        model = UseCase
        fields = ("name", "idComponent",)
        labels = {
            "name": _("UseCase"),
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Nombre de Caso de Uso",
                "autocomplete": "random_name",
            }),
            "idComponent": forms.TextInput(attrs={
                "input_type": 'hidden',
            }),
        }
