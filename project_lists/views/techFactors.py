from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from project_lists.models import ProjectList, Component, TechFactors
from project_lists.forms import TechFactorsForm
from django.shortcuts import redirect


# Create your views here.


class TechFactorsAdd(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'project_lists/techFactors.html'
    model = TechFactors
    # form_class = TechFactorsForm
    # success_url = reverse_lazy('project_lists:repcu_details')
    success_message = "Factores actualizados correctamente."
    fields = '__all__'

    def get_success_url(self):
        list = self.kwargs.get('pk')
        return reverse('project_lists:repcu_details', kwargs={'pk': list})

    def get_context_data(self, **kwargs):
        context = super(TechFactorsAdd, self).get_context_data(**kwargs)
        context['project_id'] = self.kwargs.get('pk')
        project = ProjectList.objects.get(id=self.kwargs.get('pk'))
        if TechFactors.objects.filter(idProject=project).exists():
            context['techFactors'] = TechFactors.objects.get(idProject=project)
        else:
            techFactors = TechFactors(
                distributedSystem=0,
                complexInternalProcessing=0,
                crossPlatformSupport=0,
                customSecurity=0,
                dependenceThirdPartyCode=0,
                easyToChange=0,
                endUserEfficency=0,
                highlyConcurrent=0,
                installationEasiness=0,
                responseTime=0,
                reusableCode=0,
                usability=0,
                userTraining=0,
               )
            context['techFactors'] = techFactors

        return context


def editTechFactors(request, **kwargs):
    project_id = request.POST.get('project_id')
    distributedSystem = request.POST.get('distributedSystem')
    complexInternalProcessing = request.POST.get('complexInternalProcessing')
    crossPlatformSupport = request.POST.get('crossPlatformSupport')
    customSecurity = request.POST.get('customSecurity')
    dependenceThirdPartyCode = request.POST.get('dependenceThirdPartyCode')
    easyToChange = request.POST.get('easyToChange')
    endUserEfficency = request.POST.get('endUserEfficency')
    highlyConcurrent = request.POST.get('highlyConcurrent')
    installationEasiness = request.POST.get('installationEasiness')
    responseTime = request.POST.get('responseTime')
    reusableCode = request.POST.get('reusableCode')
    usability = request.POST.get('usability')
    userTraining = request.POST.get('userTraining')
    idProject = ProjectList.objects.get(id=project_id)

    if TechFactors.objects.filter(idProject=project_id).exists():
        techFactors = TechFactors.objects.get(idProject=idProject)
        techFactors.distributedSystem = distributedSystem
        techFactors.complexInternalProcessing = complexInternalProcessing
        techFactors.crossPlatformSupport = crossPlatformSupport
        techFactors.customSecurity = customSecurity
        techFactors.dependenceThirdPartyCode = dependenceThirdPartyCode
        techFactors.easyToChange = easyToChange
        techFactors.endUserEfficency = endUserEfficency
        techFactors.highlyConcurrent = highlyConcurrent
        techFactors.installationEasiness = installationEasiness
        techFactors.responseTime = responseTime
        techFactors.reusableCode = reusableCode
        techFactors.usability = usability
        techFactors.userTraining = userTraining
        techFactors.idProject = idProject
    else:
        techFactors = TechFactors(
            distributedSystem=distributedSystem,
            complexInternalProcessing=complexInternalProcessing,
            crossPlatformSupport=crossPlatformSupport,
            customSecurity=customSecurity,
            dependenceThirdPartyCode=dependenceThirdPartyCode,
            easyToChange=easyToChange,
            endUserEfficency=endUserEfficency,
            highlyConcurrent=highlyConcurrent,
            installationEasiness=installationEasiness,
            responseTime=responseTime,
            reusableCode=reusableCode,
            usability=usability,
            userTraining=userTraining,
            idProject=idProject
        )
    techFactors.save()
    url = "/repcu/" + str(project_id) + "/techfactors/"
    return redirect(url)
