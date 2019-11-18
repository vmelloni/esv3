from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render_to_response, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import DeleteView
from project_lists.models import ProjectList
from project_lists.forms import ProjectListForm
from django.contrib import messages


# Create your views here.


class DashBoardAdd(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'project_lists/dashboard_add.html'
    form_class = ProjectListForm
    success_url = reverse_lazy("project_lists:dashboard")
    # success_message = "Proyecto agregado correctamente."

    def render_to_response(self, context, **response_kwargs):
        context['project_lists'] = ProjectList.objects.filter(owner=self.request.user)
        context['owner'] = self.request.user
        return super(DashBoardAdd, self).render_to_response(context, **response_kwargs)

    def form_valid(self, form):
        list_name = form.cleaned_data['name']
        time = form.cleaned_data['time']
        owner = self.request.user
        if ProjectList.objects.filter(name=list_name, owner=owner).exists():
            messages.error(self.request, 'Error, proyecto ya existente.')  
        else:
            form.instance.owner = owner
            messages.success(self.request, 'Proyecto agregado correctamente.')
            return super(DashBoardAdd, self).form_valid(form)
        url = "/dashboard/"
        return redirect(url)

    def get_context_data(self, **kwargs):
        context = super(DashBoardAdd, self).get_context_data(**kwargs)
        context['project_id'] = self.kwargs.get('pk')
        return context
