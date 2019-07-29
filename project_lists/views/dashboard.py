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
    success_message = "Project has been created."

    def render_to_response(self, context, **response_kwargs):
        context['project_lists'] = ProjectList.objects.filter(owner=self.request.user)
        return super(DashBoardView, self).render_to_response(context, **response_kwargs)

    def form_valid(self, form):
        list_name = form.cleaned_data['name']
        owner = self.request.user
        if ProjectList.objects.filter(name=list_name, owner=owner).exists():
            form._errors['Project already exists'] = ''
            return super(DashBoardView, self).form_invalid(form)
        form.instance.owner = owner
        return super(DashBoardView, self).form_valid(form)


class ProjectUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ProjectList
    form_class = ProjectListForm
    template_name = "project_lists/edit_list_form.html"
    success_url = reverse_lazy("project_lists:dashboard")
    success_message = "Update was successful."

    def form_valid(self, form):
        list_name = form.cleaned_data['name']
        owner = self.request.user
        list = ProjectList.objects.filter(name=list_name, owner=owner)
        if list.exists() and list.first().id != self.kwargs.get('pk'):
            form._errors[' A Project with that name already exists'] = ''
            context = {"form": form}
            context['project_lists'] = ProjectList.objects.filter(owner=owner)
            return render_to_response("project_lists/dashboard.html", context=context)
        return super(ProjectUpdate, self).form_valid(form)


class ProjectDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Deletion of a project."""
    model = ProjectList
    template_name = "project_lists/delete_list_form.html"
    success_url = reverse_lazy("project_lists:dashboard")
    success_message = "Delete was successful."

    def get_context_data(self, **kwargs):
        context = super(ProjectDelete, self).get_context_data(**kwargs)
        context['messages'] = list(self.success_message)
        return context
