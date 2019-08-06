from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render_to_response, render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DetailView
from django.views.generic.edit import DeleteView, FormMixin, FormView
from project_lists.models import Activity, ProjectList
from project_lists.forms import ActivityForm, ProjectListForm
from django.template import RequestContext, Template


class ActivityMTV(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    print("MTV_VIEW 1 ")
    form_class = ActivityForm
    model = Activity
    template_name = "project_lists/mtv.html"
    success_url = reverse_lazy("project_lists:details")
    success_message = "Estimation was successful."

    def get_success_url(self):
        print("MTV_VIEW 2 ")
        return reverse('project_lists:MTV', kwargs={'pk': self.kwargs.get("pk")})

    def render_to_response(self, context, **response_kwargs):
        project_id = self.kwargs.get("pk")
        activities = Activity.objects.filter(list_id=project_id)
        mid = 0
        for activity in activities:
            o_value = activity.optimist
            a_value = activity.average
            p_value = activity.pessimist
            mid = mid + (o_value + 4 * a_value + p_value) / 6
        mid = round(mid, 2)
        context['message'] = mid
        ProjectList.objects.filter(id=project_id).update(estimate_mtv=mid)
        return super(ActivityMTV, self).render_to_response(context, **response_kwargs)

    #
    # def get_context_data(self, **kwargs):
    #     media = 12
    #     context = super(ActivityMTV, self).get_context_data(**kwargs)
    #     context['message'] = media
    #     print(context)
    #     return context

    # def render_to_response(self, form, context, **response_kwargs):
    #     print("MTV_VIEW 3 ")
    #     return super(ActivityMTV, self).render_to_response(context, **response_kwargs)
