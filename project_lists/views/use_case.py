from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render_to_response
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import DeleteView
from project_lists.models import ProjectList, Component, UseCase


# Create your views here.


class CUView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'project_lists/use_case.html'
    model = UseCase
    success_message = "Caso de Uso agregado correctamente."
    fields = '__all__'

    def get_success_url(self):
        component = self.kwargs.get('pk')
        return reverse('project_lists:repcu_details', kwargs={'pk': component})

    def render_to_response(self, context, **response_kwargs):
        component_id = self.kwargs.get('pk')
        context['component_id'] = component_id
        context['component'] = Component.objects.get(id=component_id)
        context['project'] = Component.objects.get(id=component_id).list_id
        context['use_case_lists'] = UseCase.objects.filter(idComponent=component_id)
        return super(CUView, self).render_to_response(context, **response_kwargs)

