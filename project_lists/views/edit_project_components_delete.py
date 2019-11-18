from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render_to_response
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import DeleteView
from project_lists.models import ProjectList, Component, UseCase, Actors
from project_lists.forms import ProjectListForm, ComponentForm


# Create your views here.


class ComponentDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Deletion of a Component."""
    model = Component
    template_name = "project_lists/edit_project_components_delete.html"
    success_message = "El componente se ha sido eliminado."

    def get_success_url(self):
        list_id = Component.objects.filter(id=self.kwargs.get('pk')).first().list.id
        return reverse('project_lists:edit_project_components', kwargs={'pk': list_id})

    def get_context_data(self, **kwargs):
        context = super(ComponentDelete, self).get_context_data(**kwargs)
        context['component_id'] = self.kwargs.get('pk')
        context['component_name'] = Component.objects.get(id=self.kwargs.get('pk')).name
        return context

    def form_valid(self, form):
        component_id = self.kwargs.get('pk')
        use_cases = UseCase.objects.filter(idComponent=component_id)
        for use_case in use_cases:
            use_case.delete()
        actors = Actors.objects.filter(idComponent=component_id)
        for actor in actors:
            actor.delete()
        Component.objects.get(id=self.kwargs.get('pk')).delete()
        return super(ComponentDelete, self).form_valid(form)