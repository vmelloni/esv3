from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render_to_response
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DetailView
from django.views.generic.edit import DeleteView, FormMixin, FormView
from project_lists.models import Component, ProjectList
from project_lists.forms import ComponentForm


# Create your views here.

class MTVEstimate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = ComponentForm
    model = Component
    template_name = "project_lists/mtv_estimation.html"
    success_url = reverse_lazy("project_lists:mtv_details")
    success_message = "Estimación exitosa."

    def get_success_url(self):
        return reverse('project_lists:mtv_details', kwargs={'pk': self.kwargs.get("pk")})

    def render_to_response(self, context, **response_kwargs):
        project_id = self.kwargs.get("pk")
        activities = Component.objects.filter(list_id=project_id)
        mid = 0
        for component in activities:
            o_value = component.optimist
            a_value = component.average
            p_value = component.pessimist
            mid = mid + (o_value + 4 * a_value + p_value) / 6
        mid = round(mid, 2)
        context['message'] = mid
        context['project_id'] = project_id
        context['project_name'] = ProjectList.objects.get(id=project_id).name
        time = ProjectList.objects.get(id=project_id).time
        if time is 1:
            context['project_time'] = "Días"
        if time is 2:
            context['project_time'] = "Horas"
        if time is 3:
            context['project_time'] = "Minutos"
        ProjectList.objects.filter(id=project_id).update(estimate_mtv=mid)
        return super(MTVEstimate, self).render_to_response(context, **response_kwargs)
