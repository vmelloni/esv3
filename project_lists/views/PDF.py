from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View, CreateView
from django.utils import timezone
from project_lists.models import *
from .render import Render
from decimal import *


class Pdf(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "project_lists/PDF.html"
    model = Component
    fields = '__all__'

    def get(self, request, **kwargs):
        project_id = self.kwargs.get('pk')
        today = today = timezone.now()
        metodo = self.kwargs.get('met')
        components = Component.objects.filter(list_id=self.kwargs.get('pk'))
        estimate_mtv = ProjectList.objects.get(id=self.kwargs.get('pk')).estimate_mtv
        estimate_mtvm = ProjectList.objects.get(id=self.kwargs.get('pk')).estimate_mtvm
        estimate_pcu = ProjectList.objects.get(id=self.kwargs.get('pk')).estimate_pcu
        tot_envFactors = 0
        tot_techFact = 0
        if EnvFactors.objects.filter(idProject=project_id).exists():
            envFactors = EnvFactors.objects.get(idProject=self.kwargs.get('pk'))
            tot_envFactors = (
                    (envFactors.familiarityWithTheProject * Decimal('1.5')) + (
                    envFactors.applicationExperience * Decimal('0.5')) +
                    envFactors.objectOrientedProgrammingExperience +
                    + (envFactors.leadAnalystCapability * Decimal('0.5')) + envFactors.motivation + (
                            envFactors.stableRequirements * 2)
                    - envFactors.partTimeStaff - envFactors.difficultProgrammingLanguage)
            tot_envFactors = Decimal('1.4') - (Decimal('0.03') * Decimal(tot_envFactors))
        if TechFactors.objects.filter(idProject=project_id).exists():
            techFactors = TechFactors.objects.get(idProject=self.kwargs.get('pk'))
            tot_techFact = (
                                   (techFactors.distributedSystem * 2) + techFactors.complexInternalProcessing
                                   + (techFactors.crossPlatformSupport * 2) + techFactors.customSecurity
                                   + techFactors.dependenceThirdPartyCode + (techFactors.easyToChange / 2) +
                                   techFactors.endUserEfficency + techFactors.highlyConcurrent + techFactors.installationEasiness
                                   + techFactors.responseTime + techFactors.reusableCode +
                                   (techFactors.usability / 2) + techFactors.userTraining) / 100
            tot_techFact = tot_techFact + Decimal('0.6')
        tot_PCU = 0
        for component in components:
            tot_PCU = tot_PCU + component.weightCU + component.actorsAmount
        project_name = ProjectList.objects.get(id=self.kwargs.get('pk')).name
        params = {
            'components': components,
            'project': project_name,
            'today': today,
            'estimate_mtv': estimate_mtv,
            'estimate_mtvm': estimate_mtvm,
            'estimate_pcu': estimate_pcu,
            'tot_envFactors': tot_envFactors,
            'tot_techFact': tot_techFact,
            'tot_PCU': tot_PCU,
            'metodo': metodo,
            'request': request
        }
        return Render.render('project_lists/PDF.html', params)
