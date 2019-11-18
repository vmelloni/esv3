from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render_to_response, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import DeleteView
from project_lists.models import ProjectList
from project_lists.forms import UpdateProjectListForm
from django.shortcuts import redirect
from django.contrib import messages


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
        context['project_time'] = ProjectList.objects.get(id=self.kwargs.get('pk')).time
        context['project_name'] = ProjectList.objects.get(id=self.kwargs.get('pk')).name
        return context
  
def editProject(request, **kwargs):
    list_name = request.POST.get("project_name")
    time = request.POST.get("time")
    project_id = kwargs.get('pk')
    if ProjectList.objects.filter(name=request.POST.get('project_name')).exists() and ProjectList.objects.filter(
            owner=request.user.id).exists():
        messages.error(request, 'Error, proyecto ya existente.')
    else:
        project = ProjectList.objects.get(id=project_id)
        project.name=list_name
        project.time = time
        project.save()
        messages.success(request, 'Proyecto modificado correctamente.')

    url = "/dashboard"
    return redirect(url)