from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import request
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from project_lists.forms import EstimateForm
from project_lists.models import Estimate, ProjectList


class EstimationOptionsView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    Model = Estimate
    form_class = EstimateForm
    template_name = "project_lists/estimate_window.html"
    success_url = reverse_lazy("project_lists:dashboard")
    success_message = "Tipo de Estimación seleccionada"

    def get_success_url(self):
        project = self.kwargs.get('project')
        return reverse('project_lists:edit_project_components', kwargs={'pk': project})

    def render_to_response(self, context, **response_kwargs):
        context['project_id'] = ProjectList.objects.filter(owner=self.request.user)
        context['owner'] = self.request.user
        return super(EstimationOptionsView, self).render_to_response(context, **response_kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(EstimationOptionsView, self).get_context_data(**kwargs)
        context['project_id'] = self.kwargs.get('project')
        context['project_name'] = ProjectList.objects.get(id=self.kwargs.get('project')).name
        return context

    def form_valid(self, form):
        method = form.cleaned_data['type_estimate']
        project_id = self.kwargs.get('project')
        if method is '1':
            url = "/mtv/" + str(project_id)
            return redirect(url)
        elif method is '2':
            url = "/mtv_m/" + str(project_id)
            return redirect(url)
        elif method is '3':
            url = "/repcu/" + str(project_id)
            return redirect(url)
        return super(EstimationOptionsView, self).form_valid(form)




