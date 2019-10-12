from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render_to_response
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DetailView
from django.views.generic.edit import DeleteView, FormMixin, FormView
from project_lists.models import Component, ProjectList
from project_lists.forms import ComponentForm


# Create your views here.


class RePCUDetailsView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = ComponentForm
    template_name = "project_lists/repcu_details.html"
    success_message = "Component has been created."

    def get_success_url(self):
        return reverse('project_lists:repcu_details', kwargs={'pk': self.kwargs.get("pk")})

    def form_valid(self, form):
        item_name = form.cleaned_data['name']
        list = ProjectList.objects.filter(id=self.kwargs.get('pk')).first()
        if Component.objects.filter(name=item_name, list=list).exists():
            form._errors[' An Component with that name already exists'] = ''
            return super(MTVDetailsView, self).form_invalid(form)
        form.instance.list = list
        return super(RePCUDetailsView, self).form_valid(form)

    def render_to_response(self, context, **response_kwargs):
        context['Component'] = Component.objects.filter(list=self.kwargs.get('pk'))
        context['object'] = ProjectList.objects.filter(id=self.kwargs.get('pk')).first()
        return super(RePCUDetailsView, self).render_to_response(context, **response_kwargs)

