from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render_to_response, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from django.views.generic.edit import DeleteView
from project_lists.models import ProjectList, Component, UseCase
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from project_lists.models import ProjectList, Component, TechFactors


# Create your views here.


class UseCaseDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = UseCase
    template_name = "project_lists/use_case_delete.html"
    success_message = "El caso de uso  ha sido eliminado exitosamente."

    def get_success_url(self):
        list_id = self.kwargs.get('comp')
        return reverse('project_lists:cu', kwargs={'pk': list_id})

    def get_context_data(self, **kwargs):
        context = super(UseCaseDelete, self).get_context_data(**kwargs)
        context['component'] = Component.objects.filter(id=self.kwargs.get('comp'))
        context['component_id'] = self.kwargs.get('comp')
        context['use_case_id'] = self.kwargs.get('pk')
        context['use_case_name'] = UseCase.objects.get(id=self.kwargs.get('pk')).name

        return context


def del_uc(request, **kwargs):
    # get use case
    component_id = request.POST.get("component_id")
    component = Component.objects.get(id=component_id)
    use_case_id= request.POST.get("use_case_id")
    use_case_transactions = UseCase.objects.get(id=use_case_id).weightCU
    # update Component weight based on deleted use case
    component.weightCU = component.weightCU - int(use_case_transactions)
    component.save()

    use_case = UseCase.objects.get(id=use_case_id)
    use_case.delete()

    url = "/repcu/" + str(component_id) + "/cu/"
    return redirect(url)
