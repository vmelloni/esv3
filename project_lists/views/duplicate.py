from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render_to_response, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import DeleteView
from project_lists.models import ProjectList, Component, UseCase, TechFactors, EnvFactors, Actors
from project_lists.forms import ProjectListForm, ComponentForm
from django.template import Context
from django.contrib import messages


# Create your views here.


class DuplicateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'project_lists/duplicate.html'
    form_class = ProjectListForm

    success_message = "Proyecto duplicado correctamente."

    def get_success_url(self):
        list = self.kwargs.get('pk')
        return reverse('project_lists:dashboard', kwargs={'pk': list})

    def render_to_response(self, context, **response_kwargs):
        context['project_lists'] = ProjectList.objects.filter(owner=self.request.user)
        context['project_id'] = self.kwargs.get('pk')
        context['project_name'] = ProjectList.objects.get(id=self.kwargs.get('pk')).name
        context['owner'] = self.request.user
        return super(DuplicateView, self).render_to_response(context, **response_kwargs)

    def get_context_data(self, **kwargs):
        context = super(DuplicateView, self).get_context_data(**kwargs)
        context['project_id'] = self.kwargs.get('pk')
        return context


def componentDuplicate(components_old_project, new_project):
    for component in components_old_project:
        new_component = Component(
            name=component.name,
            list=new_project,
            optimist=component.optimist,
            average=component.average,
            pessimist=component.pessimist,
            riskValue=component.riskValue,
            actorsAmount=component.actorsAmount,
            weightCU=component.weightCU,
        )
        new_component.save()
        if UseCase.objects.filter(idComponent=component).exists():
            use_cases = UseCase.objects.filter(idComponent=component)
            for use_case in use_cases:
                new_use_case = UseCase(idComponent=new_component, name=use_case.name, weightCU=use_case.weightCU)
                new_use_case.save()
        if Actors.objects.filter(idComponent=component).exists():
            actors = Actors.objects.filter(idComponent=component)
            for actor in actors:
                new_actor = Actors(idComponent=new_component, simple=actor.simple, average=actor.average,
                                   complex=actor.complex, critical=actor.critical)
                new_actor.save()


def techFactorsDuplicate(tech_factors_old_project, new_project):
    tech_factors_old_project = tech_factors_old_project.first()
    techFactors = TechFactors(
        distributedSystem=tech_factors_old_project.distributedSystem,
        complexInternalProcessing=tech_factors_old_project.complexInternalProcessing,
        crossPlatformSupport=tech_factors_old_project.crossPlatformSupport,
        customSecurity=tech_factors_old_project.customSecurity,
        dependenceThirdPartyCode=tech_factors_old_project.dependenceThirdPartyCode,
        easyToChange=tech_factors_old_project.easyToChange,
        endUserEfficency=tech_factors_old_project.endUserEfficency,
        highlyConcurrent=tech_factors_old_project.highlyConcurrent,
        installationEasiness=tech_factors_old_project.installationEasiness,
        responseTime=tech_factors_old_project.responseTime,
        reusableCode=tech_factors_old_project.reusableCode,
        usability=tech_factors_old_project.usability,
        userTraining=tech_factors_old_project.userTraining,
        idProject=new_project
    )
    techFactors.save()


def envFactorsDuplicate(env_factors_old_project, new_project):
    env_factors_old_project = env_factors_old_project.first()
    envFactors = EnvFactors(
        familiarityWithTheProject=env_factors_old_project.familiarityWithTheProject,
        applicationExperience=env_factors_old_project.applicationExperience,
        objectOrientedProgrammingExperience=env_factors_old_project.objectOrientedProgrammingExperience,
        leadAnalystCapability=env_factors_old_project.leadAnalystCapability,
        motivation=env_factors_old_project.motivation,
        stableRequirements=env_factors_old_project.stableRequirements,
        partTimeStaff=env_factors_old_project.partTimeStaff,
        difficultProgrammingLanguage=env_factors_old_project.difficultProgrammingLanguage,
        idProject=new_project
    )
    envFactors.save()


def duplicateAllData(request, **kwargs):
    old_project_id = request.POST.get('project_id')
    context = Context()
    if ProjectList.objects.filter(name=request.POST.get('name')).exists() and ProjectList.objects.filter(
            owner=request.user.id).exists():
        messages.error(request, 'Error, proyecto ya existente.')
    else:
        old_project = ProjectList.objects.get(id=old_project_id)
        old_project_mtv = old_project.estimate_mtv
        old_project_mtvm = old_project.estimate_mtvm
        old_project_pcu = old_project.estimate_pcu
        new_project_name = request.POST.get('name')
        new_project = ProjectList(name=new_project_name, owner=old_project.owner, estimate_mtv=old_project_mtv,
                                  estimate_mtvm=old_project_mtvm, estimate_pcu=old_project_pcu)
        new_project.save()
        if EnvFactors.objects.filter(idProject=old_project_id).exists():
            env_factors_old_project = EnvFactors.objects.filter(idProject=old_project_id)
            envFactorsDuplicate(env_factors_old_project, new_project)
        if TechFactors.objects.filter(idProject=old_project_id).exists():
            tech_factors_old_project = TechFactors.objects.filter(idProject=old_project_id)
            techFactorsDuplicate(tech_factors_old_project, new_project)
        if Component.objects.filter(list_id=int(old_project_id)).exists():
            components_old_project = Component.objects.filter(list_id=int(old_project_id))
            componentDuplicate(components_old_project, new_project)
        messages.success(request, 'Proyecto agregado correctamente.')
    
    url = "/dashboard/"
    return redirect(url)
