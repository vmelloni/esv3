# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.messages.views import SuccessMessageMixin
# from django.http import HttpResponseForbidden
# from django.shortcuts import render_to_response
# from django.urls import reverse_lazy, reverse
# from django.utils.decorators import method_decorator
# from django.views.generic import CreateView, UpdateView, DetailView
# from django.views.generic.edit import DeleteView, FormMixin, FormView
# from project_lists.models import Component, ProjectList
# from project_lists.forms import ComponentForm


# # Create your views here.
# class MTVMEstimate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     form_class = ComponentForm
#     model = Component
#     template_name = "project_lists/mtvm_estimation.html"
#     success_url = reverse_lazy("project_lists:details_m")
#     success_message = "Estimación exitosa."

#     def get_success_url(self):
#         return reverse('project_lists:MTVM_details', kwargs={'pk': self.kwargs.get("pk")})

#     def render_to_response(self, context, **response_kwargs):
#         project_id = self.kwargs.get("pk")
#         activities = Component.objects.filter(list_id=project_id)
#         midLowRisk = 0
#         midMidRisk = 0
#         midHighRisk = 0
#         mid = 0
#         for component in activities:
#             o_value = Component.optimist
#             a_value = Component.average
#             p_value = Component.pessimist
#             risk = Component.riskValue
#             if risk == 1:
#                 midLowRisk = midLowRisk + (o_value + 4 * a_value + p_value) / 6
#             elif risk == 2:
#                 midMidRisk = midMidRisk + (o_value + 4 * a_value + p_value) / 6
#             elif risk == 3:
#                 midHighRisk = midHighRisk + (o_value + 4 * a_value + p_value) / 6

#             mid = midLowRisk + midMidRisk + midHighRisk

#         mid = round(mid, 2)
#         context['message'] = mid
#         ProjectList.objects.filter(id=project_id).update(estimate_mtv=mid)
#         return super(MTVMEstimate, self).render_to_response(context, **response_kwargs)

# class RePCUEstimate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     form_class = ComponentForm
#     model = Component
#     template_name = "project_lists/repcu_estimation.html"
#     success_url = reverse_lazy("project_lists:details")
#     success_message = "Estimación exitosa."

#     def get_success_url(self):
#         return reverse('project_lists:MTV', kwargs={'pk': self.kwargs.get("pk")})

#     def render_to_response(self, context, **response_kwargs):
#         project_id = self.kwargs.get("pk")
#         activities = Component.objects.filter(list_id=project_id)
#         mid = 0
#         for component in activities:
#             o_value = component.optimist
#             a_value = component.average
#             p_value = component.pessimist
#             mid = mid + (o_value + 4 * a_value + p_value) / 6
#         mid = round(mid, 2)
#         context['message'] = mid
#         ProjectList.objects.filter(id=project_id).update(estimate_mtv=mid)
#         return super(RePCUEstimate, self).render_to_response(context, **response_kwargs)

