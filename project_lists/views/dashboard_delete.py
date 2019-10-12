from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render_to_response
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import DeleteView
from project_lists.models import ProjectList
from project_lists.forms import ProjectDeleteForm


# Create your views here.


class ProjectDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Deletion of a project."""
    model = ProjectList
    form_class = ProjectDeleteForm
    template_name = "project_lists/dashboard_delete.html"
    success_url = reverse_lazy("project_lists:dashboard")
    success_message = "El proyecto ha sido eliminado."

    def get_context_data(self, **kwargs):
        context = super(ProjectDelete, self).get_context_data(**kwargs)
        context['project'] = self.kwargs.get('pk')
        context['project_name'] = ProjectList.objects.get(id=self.kwargs.get('pk')).name
        return context

    def form_valid(self, form):
        ProjectList.objects.get(id=self.kwargs.get('pk')).delete()
        return super(ProjectDelete, self).form_valid(form)
