from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView
from django.utils import timezone

from project_lists.forms import ProjectListForm
from project_lists.models import *
from .render import Render
from decimal import *


class Help(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "project_lists/help.html"
    success_url = reverse_lazy("project_lists:dashboard")
    form_class = ProjectListForm

    def render_to_response(self, context, **response_kwargs):
        return super(Help, self).render_to_response(context, **response_kwargs)