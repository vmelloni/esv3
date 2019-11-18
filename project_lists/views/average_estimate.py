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


class AverageView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'project_lists/average.html'
    model = UseCase
    
    fields = '__all__'

    def get_success_url(self):
        project_id = self.kwargs.get('pk')
        return reverse('project_lists:dashboard', kwargs={'pk': project_id})

    def render_to_response(self, context, **response_kwargs):
        project_id = self.kwargs.get('pk')
        context['project'] = ProjectList.objects.get(id=project_id)
        context['project_name'] = ProjectList.objects.get(id=project_id).name
        context['modo'] = self.kwargs.get('mod')
        project = ProjectList.objects.get(id=project_id)
        prom = (project.estimate_mtv + project.estimate_mtvm + project.estimate_pcu) / 3
        prom = round(prom, 2)
        context['average'] = prom
        return super(AverageView, self).render_to_response(context, **response_kwargs)

