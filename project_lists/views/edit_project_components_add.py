from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render_to_response
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import DeleteView
from project_lists.models import ProjectList, Component
from project_lists.forms import ProjectListForm, ComponentForm


# Create your views here.


class ComponentAdd(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'project_lists/edit_project_components_add.html'
    form_class = ComponentForm
    success_url = reverse_lazy('project_lists:edit_project_components')
    success_message = "Componente agregado correctamente."

    def get_success_url(self):
        list = self.kwargs.get('pk')
        return reverse('project_lists:edit_project_components', kwargs={'pk': list})

    def get_context_data(self, **kwargs):
        context = super(ComponentAdd, self).get_context_data(**kwargs)
        context['project_id'] = self.kwargs.get('pk')
        context['components'] = Component.objects.filter(list_id=self.kwargs.get('pk'))
        context['project_name'] = ProjectList.objects.get(id=self.kwargs.get('pk')).name
        time = ProjectList.objects.get(id=self.kwargs.get('pk')).time
        if time is 1:
            context['project_time'] = "Días"
        if time is 2:
            context['project_time'] = "Horas"
        if time is 3:
            context['project_time'] = "Minutos"
        return context
