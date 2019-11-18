from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render_to_response
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DetailView
from django.views.generic.edit import DeleteView, FormMixin, FormView
from project_lists.models import Component, ProjectList, TechFactors, EnvFactors
from project_lists.forms import ComponentForm
from decimal import *


# Create your views here.
class RePCUEstimate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = ComponentForm
    model = Component
    template_name = "project_lists/repcu_estimation.html"
    success_url = reverse_lazy("project_lists:details")
    success_message = "Estimación exitosa."

    def get_success_url(self):
        return reverse('project_lists:details', kwargs={'pk': self.kwargs.get("pk")})

    def render_to_response(self, context, **response_kwargs):
        project_id = self.kwargs.get("pk")
        activities = Component.objects.filter(list_id=project_id)
        context['project_name'] = ProjectList.objects.get(id=project_id).name
        context['project_id'] = project_id
        if not TechFactors.objects.filter(idProject=project_id).exists():
            context['error'] = 'X'
            context['message'] = 'Falta ingresar los Factores Técnicos para obtener una estimación'
            return super(RePCUEstimate, self).render_to_response(context, **response_kwargs)
        techFactors = TechFactors.objects.get(idProject=project_id)

        tot_techFact = (
                          (techFactors.distributedSystem * 2) + techFactors.complexInternalProcessing
                          + (techFactors.crossPlatformSupport * 2) + techFactors.customSecurity
                          + techFactors.dependenceThirdPartyCode + (techFactors.easyToChange / 2) +
                          techFactors.endUserEfficency + techFactors.highlyConcurrent + techFactors.installationEasiness
                          + techFactors.responseTime + techFactors.reusableCode +
                          (techFactors.usability / 2) + techFactors.userTraining) / 100
        tot_techFact = tot_techFact + Decimal('0.6')
        if not EnvFactors.objects.filter(idProject=project_id).exists():
            context['error'] = 'X'
            context['message'] = 'Falta ingresar los Factores Ambientales para obtener una estimación'
            return super(RePCUEstimate, self).render_to_response(context, **response_kwargs)
        envFactors = EnvFactors.objects.get(idProject=project_id)
        tot_envFactors = (
                                 (envFactors.familiarityWithTheProject * Decimal('1.5')) + (
                                     envFactors.applicationExperience * Decimal('0.5')) +
                                 envFactors.objectOrientedProgrammingExperience +
                                 + (envFactors.leadAnalystCapability * Decimal('0.5')) + envFactors.motivation + (
                                             envFactors.stableRequirements * 2)
                                 - envFactors.partTimeStaff - envFactors.difficultProgrammingLanguage)
        tot_envFactors = Decimal('1.4') - (Decimal('0.03') * Decimal(tot_envFactors))
        tot_PCU = 0
        for component in activities:
            tot_PCU = tot_PCU + component.weightCU + component.actorsAmount
        tot_PCU = tot_PCU * tot_techFact * tot_envFactors
        tot_PCU = round(tot_PCU, 2)
        context['message'] = tot_PCU
        time = ProjectList.objects.get(id=project_id).time
        if time is 1:
            context['project_time'] = "Días"
        if time is 2:
            context['project_time'] = "Horas"
        if time is 3:
            context['project_time'] = "Minutos"
        ProjectList.objects.filter(id=project_id).update(estimate_pcu=tot_PCU)
        return super(RePCUEstimate, self).render_to_response(context, **response_kwargs)
