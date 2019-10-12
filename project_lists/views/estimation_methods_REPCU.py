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
class RePCUEstimate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = ComponentForm
    model = Component
    template_name = "project_lists/repcu_estimation.html"
    success_url = reverse_lazy("project_lists:details")
    success_message = "Estimation was successful."

    def get_success_url(self):
        return reverse('project_lists:MTV', kwargs={'pk': self.kwargs.get("pk")})

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
        ProjectList.objects.filter(id=project_id).update(estimate_mtv=mid)
        return super(RePCUEstimate, self).render_to_response(context, **response_kwargs)

