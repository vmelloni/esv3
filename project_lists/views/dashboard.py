from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render_to_response
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import DeleteView
from project_lists.models import ProjectList
from project_lists.forms import ProjectListForm


# Create your views here.


class DashBoardView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'project_lists/dashboard.html'
    form_class = ProjectListForm
    success_url = reverse_lazy("project_lists:dashboard")
    success_message = "Proyecto agregado correctamente."

    def render_to_response(self, context, **response_kwargs):
        context['project_lists'] = ProjectList.objects.filter(owner=self.request.user)
        context['owner'] = self.request.user
        return super(DashBoardView, self).render_to_response(context, **response_kwargs)


# class ProjectDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
#     """Deletion of a project."""
#     model = ProjectList
#     template_name = "project_lists/dashboard_delete.html"
#     success_url = reverse_lazy("project_lists:dashboard")
#     success_message = "Delete was successful."

#     def get_context_data(self, **kwargs):
#         context = super(ProjectDelete, self).get_context_data(**kwargs)
#         context['messages'] = list(self.success_message)
#         return context
