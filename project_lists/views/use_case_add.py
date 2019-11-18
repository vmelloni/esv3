from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from project_lists.models import UseCase, Component, ProjectList
from project_lists.forms import UseCaseAddForm
from django.urls import reverse
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse

# Create your views here.


class CUAdd(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'project_lists/use_case_add.html'
    form_class = UseCaseAddForm
    success_url = reverse_lazy('project_lists:cu')
    success_message = "Caso de Uso agregado correctamente."

    def get_success_url(self):
        component = self.kwargs.get('pk')
        return reverse('project_lists:cu', kwargs={'pk': component})

    def get_context_data(self, **kwargs):
        context = super(CUAdd, self).get_context_data(**kwargs)
        context['component'] = self.kwargs.get('pk')
        component = Component.objects.get(id=self.kwargs.get('pk'))
        context['component_name'] = component.name
        project_id = component.list_id
        project = ProjectList.objects.get(id=project_id)
        context['project_name'] = project.name
        return context


def AddUC(request, **kwargs):
    # create use case
    use_case_name = request.POST.get("useCaseName")
    use_case_transactions = request.POST.get("cantTransactions")
    component_id = request.POST.get("idComponent")
    component = Component.objects.get(id=component_id)
    use_case = UseCase(name=use_case_name, idComponent=component, weightCU=use_case_transactions)
    use_case.save()

    # update Component weight based on created use case
    component.weightCU = component.weightCU + int(use_case_transactions)
    component.save()

    url = "/repcu/" + str(component_id) + "/cu/"
    return redirect(url)
