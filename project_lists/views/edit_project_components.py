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


class ComponentsView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'project_lists/edit_project_components.html'
    form_class = ComponentForm
    success_url =  reverse_lazy('project_lists:edit_project_components')
    success_message = "Componente agregado correctamente."

    def get_success_url(self):
        list = self.kwargs.get('pk')
        return reverse('project_lists:edit_project_components', kwargs={'pk': list})

    def get_context_data(self, **kwargs):
        context = super(ComponentsView, self).get_context_data(**kwargs)
        context['project_id'] = self.kwargs.get('pk')
        context['components'] = Component.objects.filter(list_id=self.kwargs.get('pk'))
        return context

    def form_valid(self, form):
        list_name = form.cleaned_data['name']
        if Component.objects.filter(name=list_name).exists() and Component.objects.filter(list_id=self.kwargs.get('pk')).exists() :
            form._errors['Component already exists'] = ''
            return super(ComponentsView, self).form_invalid(form)
        form.list_id = list
        return super(ComponentsView, self).form_valid(form)


