from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from project_lists.models import EnvFactors, Actors, Component, ProjectList
from django.shortcuts import redirect


class ActorsAdd(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "project_lists/actors.html"
    model = Actors
    success_message = "Actores ingresados correctamente"
    fields = '__all__'

    def get_success_url(self):
        list = self.kwargs.get('pk')
        return reverse('project_lists:repcu_details', kwargs={'pk': list})

    def get_context_data(self, **kwargs):
        context = super(ActorsAdd, self).get_context_data(**kwargs)
        context['component'] = self.kwargs.get('pk')
        context['project'] = Component.objects.get(id=self.kwargs.get('pk')).list_id
        context['component_name'] = Component.objects.get(id=self.kwargs.get('pk')).name
        project_id = Component.objects.get(id=self.kwargs.get('pk')).list_id
        project = ProjectList.objects.get(id=project_id)
        context['project_name'] = project.name
        
        if Actors.objects.filter(idComponent=self.kwargs.get('pk')).exists():
            context['actors'] = Actors.objects.get(idComponent=self.kwargs.get('pk'))
        else:
            actors = Actors(
                simple=0,
                average=0,
                complex=0,
                critical=0,)
            context['actors'] = actors
        return context


def editActors(request, **kwargs):
    component_id = request.POST.get('component')
    simple = request.POST.get('simple')
    average = request.POST.get('average')
    complex = request.POST.get('complex')
    critical = request.POST.get('critical')
    idComponent = Component.objects.get(id=component_id)
    if Actors.objects.filter(idComponent=component_id).exists():
        actors = Actors.objects.get(idComponent=component_id)
        actors.simple = simple
        actors.average = average
        actors.complex = complex
        actors.critical = critical
        actors.idComponent = idComponent
    else:
        actors = Actors(
            simple=simple,
            average=average,
            complex=complex,
            critical=critical,
            idComponent=idComponent
        )
    actors.save()
    component = Component.objects.get(id=component_id)
    # update Component weight based on created use case
    component.actorsAmount = int(actors.simple) + (int(actors.average) * 2) + (int(actors.complex) * 3) + (
            int(actors.critical) * 4)
    component.save()
    url = "/repcu/" + str(component_id) + "/actors/"
    return redirect(url)
