from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render_to_response
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DetailView
# from django.views.generic.edit import DeleteView, FormMixin, FormView
from project_lists.models import Component, ProjectList
from django.shortcuts import redirect

# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render


class MTVDetailsView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Component
    template_name = "project_lists/mtv_details_view.html"
    success_url = reverse_lazy('project_lists:mtv_details_view')
    success_message = "Exito!."
    fields = '__all__'

    def get_success_url(self):
        project = self.kwargs.get('pk')
        return reverse('project_lists:mtv_details_view', kwargs={'pk': project})

    def get_context_data(self, **kwargs):
        context = super(MTVDetailsView, self).get_context_data(**kwargs)
        project_id = self.kwargs.get('pk')
        context['project'] = ProjectList.objects.filter(id=project_id).first()
        components = Component.objects.filter(list_id=self.kwargs.get('pk'))
        context['components'] = components
        context['project_name'] = ProjectList.objects.get(id=project_id).name
        time = ProjectList.objects.get(id=project_id).time
        if time is 1:
            context['project_time'] = "Días"
        if time is 2:
            context['project_time'] = "Horas"
        if time is 3:
            context['project_time'] = "Minutos"
        return context

    def render_to_response(self, context, **response_kwargs):
        context['component'] = Component.objects.filter(list=self.kwargs.get('pk'))
        context['object'] = ProjectList.objects.filter(id=self.kwargs.get('pk')).first()
        return super(MTVDetailsView, self).render_to_response(context, **response_kwargs)


class MTVDetailsEditView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Component
    template_name = "project_lists/mtv_details_edit.html"
    success_url = reverse_lazy('project_lists:mtv_details_edit')
    # success_message = ""
    fields = '__all__'

    def get_success_url(self):
        project = self.kwargs.get('pk')
        return reverse('project_lists:mtv_details_edit', kwargs={'pk': project})

    def get_context_data(self, **kwargs):
        context = super(MTVDetailsEditView, self).get_context_data(**kwargs)
        project_id = self.kwargs.get('pk')
        context['project'] = ProjectList.objects.filter(id=project_id).first()
        components = Component.objects.filter(list_id=self.kwargs.get('pk'))
        context['components'] = components
        context['project_name'] = ProjectList.objects.get(id=project_id).name
        time = ProjectList.objects.get(id=project_id).time
        if time is 1:
            context['project_time'] = "Días"
        if time is 2:
            context['project_time'] = "Horas"
        if time is 3:
            context['project_time'] = "Minutos"
        return context

    def render_to_response(self, context, **response_kwargs):
        context['component'] = Component.objects.filter(list=self.kwargs.get('pk'))
        context['object'] = ProjectList.objects.filter(id=self.kwargs.get('pk')).first()
        return super(MTVDetailsEditView, self).render_to_response(context, **response_kwargs)


def editMTV(request, **kwargs):
    components_id = request.POST.getlist("id")
    components_optimist = request.POST.getlist("optimist")
    components_pessimist = request.POST.getlist("pessimist")
    components_average = request.POST.getlist("average")
    project_id = kwargs.get('pk')
    for c in components_id:
        optimist_value = components_optimist.pop(0)
        pessimist_value = components_pessimist.pop(0)
        average_value = components_average.pop(0)
        component = Component.objects.get(id=c)
        component.optimist = optimist_value
        component.pessimist = pessimist_value
        component.average = average_value
        component.save()

    url = "/mtv/" + str(project_id) + "/estimate"
    return redirect(url)
