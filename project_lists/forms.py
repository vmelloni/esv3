from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import ProjectList, Component, Estimate


class ProjectListForm(ModelForm):
    class Meta:
        model = ProjectList
        fields = ("name", "owner")
        labels = {
            "name": _("Project List Name")
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Project Name",
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
            "name": _("Project List Name")
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Project Name",
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
            "name": _("Component"),
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control testclass",
                "placeholder": "Component Name",
                "autocomplete": "random_name",
            }),
            "list": forms.TextInput(attrs={
                "placeholder": "list id ",
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
                "placeholder": "Component Name",
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
                    "placeholder": "project id ",
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
                                              choices=ESTIMATE_CHOICES, )}


