from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import ProjectList, Activity


class ProjectListForm(ModelForm):

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
        }


class ActivityForm(ModelForm):

    class Meta:
        model = Activity
        fields = ("name", "optimist", "average", "pessimist",)
        labels = {
            "name": _("Activity"),
            "optimist": _("Optimist"),
            "average": _("Average"),
            "pessimist": _("Pessimist"),
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Activity Name",
                "autocomplete": "random_name",
            }),
            "optimist": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Optimist Value",
                "autocomplete": "random_name",
            }),
            "average": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Average Value",
                "autocomplete": "random_name",
            }),
            "pessimist": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Pessimist Value",
                "autocomplete": "random_name",
            }),
        }
