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


class RePCUDetailsView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Component
    form_class = ComponentForm
    template_name = "project_lists/repcu_details.html"
    success_url = reverse_lazy('project_lists:repcu_details')
    success_message = ""

    def get_success_url(self):
        project_id = self.kwargs.get("pk")
        return reverse('project_lists:repcu_details', kwargs={'pk': project_id })

    def get_context_data(self, **kwargs):
        context = super(RePCUDetailsView, self).get_context_data(**kwargs)
        project_id = self.kwargs.get('pk')
        context['project'] = ProjectList.objects.get(id=project_id)
        context['project_name'] = ProjectList.objects.get(id=self.kwargs.get('pk')).name
        components = Component.objects.filter(list_id=project_id)
        context['components'] = components
        time = ProjectList.objects.get(id=project_id).time
        if time is 1:
            context['project_time'] = "Días"
        if time is 2:
            context['project_time'] = "Horas"
        if time is 3:
            context['project_time'] = "Minutos"
        return context
    
    def render_to_response(self, context, **response_kwargs):
        project_id = self.kwargs.get('pk')
        context['project'] = ProjectList.objects.get(id=project_id)
        components = Component.objects.filter(list_id=project_id)
        context['components'] = components
        return super(RePCUDetailsView, self).render_to_response(context, **response_kwargs)

