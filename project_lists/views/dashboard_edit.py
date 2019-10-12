from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render_to_response
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import DeleteView
from project_lists.models import ProjectList
from project_lists.forms import UpdateProjectListForm


# Create your views here.


class ProjectUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ProjectList
    form_class = UpdateProjectListForm
    template_name = "project_lists/dashboard_edit.html"
    success_url = reverse_lazy("project_lists:dashboard")
    success_message = "El proyecto ha sido editado exitosamente."

    def get_context_data(self, **kwargs):
        context = super(ProjectUpdate, self).get_context_data(**kwargs)
        context['project_id'] = self.kwargs.get('pk')
        return context
 
    def form_valid(self, form):
        list_name = form.cleaned_data['name']
        project = ProjectList.objects.get(id=self.kwargs.get('pk'))
        project.name = list_name
        project.save()
        return super(ProjectUpdate, self).form_valid(form)

