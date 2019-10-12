from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render_to_response
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import DeleteView
from project_lists.models import Component, ProjectList
from project_lists.forms import ComponentUpdateForm

# Create your views here.


class ComponentUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'project_lists/edit_project_components_edit.html'
    form_class = ComponentUpdateForm
    success_url = reverse_lazy('project_lists:edit_project_components')
    success_message = "El componente ha sido editado exitosamente."
    model = Component

    def get_success_url(self):
        project = self.kwargs.get('project')
        return reverse('project_lists:edit_project_components', kwargs={'pk': project})
  
    def get_context_data(self, **kwargs):
        context = super(ComponentUpdate, self).get_context_data(**kwargs)
        context['component_id'] = self.kwargs.get('pk')
        context['project_id'] = self.kwargs.get('project')
        context['project_name'] = ProjectList.objects.get(id=self.kwargs.get('project')).name
        return context

    def form_valid(self, form):
        component_name = form.cleaned_data['name']
        component = Component.objects.get(id=self.kwargs.get('pk'))
        component.name = component_name
        component.save()
        return super(ComponentUpdate, self).form_valid(form)

