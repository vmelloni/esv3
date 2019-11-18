from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from project_lists.models import EnvFactors, ProjectList
from django.shortcuts import redirect


# Create your views here.


class EnvFactorsAdd(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'project_lists/envFactors.html'
    model = EnvFactors
    success_message = "Factores actualizados correctamente."
    fields = '__all__'

    def get_success_url(self):
        list = self.kwargs.get('pk')
        return reverse('project_lists:repcu_details', kwargs={'pk': list})

    def get_context_data(self, **kwargs):
        context = super(EnvFactorsAdd, self).get_context_data(**kwargs)
        context['project_id'] = self.kwargs.get('pk')
        project = ProjectList.objects.get(id=self.kwargs.get('pk'))
        if EnvFactors.objects.filter(idProject=project).exists():
            context['envFactors'] = EnvFactors.objects.get(idProject=project)
        else:
            envFactors = EnvFactors(
                familiarityWithTheProject=0,
                applicationExperience=0,
                objectOrientedProgrammingExperience=0,
                leadAnalystCapability=0,
                motivation=0,
                stableRequirements=0,
                partTimeStaff=0,
                difficultProgrammingLanguage=0,
            )
            context['envFactors'] = envFactors
        return context


def editEnvFactors(request, **kwargs):
    project_id = request.POST.get('project_id')
    familiarityWithTheProject = request.POST.get('familiarityWithTheProject')
    applicationExperience = request.POST.get('applicationExperience')
    objectOrientedProgrammingExperience = request.POST.get('objectOrientedProgrammingExperience')
    leadAnalystCapability = request.POST.get('leadAnalystCapability')
    motivation = request.POST.get('motivation')
    stableRequirements = request.POST.get('stableRequirements')
    partTimeStaff = request.POST.get('partTimeStaff')
    difficultProgrammingLanguage = request.POST.get('difficultProgrammingLanguage')
    idProject = ProjectList.objects.get(id=project_id)

    if EnvFactors.objects.filter(idProject=project_id).exists():
        envFactors = EnvFactors.objects.get(idProject=idProject)
        envFactors.familiarityWithTheProject = familiarityWithTheProject
        envFactors.applicationExperience = applicationExperience
        envFactors.objectOrientedProgrammingExperience = objectOrientedProgrammingExperience
        envFactors.leadAnalystCapability = leadAnalystCapability
        envFactors.motivation = motivation
        envFactors.stableRequirements = stableRequirements
        envFactors.partTimeStaff = partTimeStaff
        envFactors.difficultProgrammingLanguage = difficultProgrammingLanguage
        envFactors.idProject = idProject
    else:
        envFactors = EnvFactors(
            familiarityWithTheProject=familiarityWithTheProject,
            applicationExperience=applicationExperience,
            objectOrientedProgrammingExperience=objectOrientedProgrammingExperience,
            leadAnalystCapability=leadAnalystCapability,
            motivation=motivation,
            stableRequirements=stableRequirements,
            partTimeStaff=partTimeStaff,
            difficultProgrammingLanguage=difficultProgrammingLanguage,
            idProject=idProject
        )
    envFactors.save()
    url = "/repcu/" + str(project_id) + "/envfactors/"
    return redirect(url)
