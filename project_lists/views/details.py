from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render_to_response
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DetailView
from django.views.generic.edit import DeleteView, FormMixin, FormView
from project_lists.models import Activity, ProjectList
from project_lists.forms import ActivityForm


# Create your views here.


class DetailsView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = ActivityForm
    template_name = "project_lists/shoppinglist_detail.html"
    success_message = "Activity has been created."

    def get_success_url(self):
        return reverse('project_lists:details', kwargs={'pk': self.kwargs.get("pk")})

    def form_valid(self, form):
        item_name = form.cleaned_data['name']
        list = ProjectList.objects.filter(id=self.kwargs.get('pk')).first()
        if Activity.objects.filter(name=item_name, list=list).exists():
            form._errors[' An Activity with that name already exists'] = ''
            return super(DetailsView, self).form_invalid(form)
        form.instance.list = list
        return super(DetailsView, self).form_valid(form)

    def render_to_response(self, context, **response_kwargs):
        context['activity'] = Activity.objects.filter(list=self.kwargs.get('pk'))
        context['object'] = ProjectList.objects.filter(id=self.kwargs.get('pk')).first()
        return super(DetailsView, self).render_to_response(context, **response_kwargs)


class ActivityUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Activity
    form_class = ActivityForm
    template_name = "project_lists/edit_item_form.html"
    success_message = "Update was successful."

    def get_success_url(self):
        list_id = Activity.objects.filter(id=self.kwargs.get('pk')).first().list.id
        return reverse('shopping_lists:details', kwargs={'pk': list_id})

    def form_valid(self, form):
        item_name = form.cleaned_data['name']
        list = Activity.objects.filter(id=self.kwargs.get('pk')).first().list
        item = Activity.objects.filter(name=item_name, list=list)
        if item.exists() and item.first().id != int(self.kwargs.get('pk')):
            form._errors[' An Activity with that name already exists in this Project'] = ''
            context = {"form": form}
            context['activity'] = Activity.objects.filter(list=list)
            return render_to_response("project_lists/shoppinglist_detail.html", context=context)
        return super(ActivityUpdate, self).form_valid(form)


class ActivityDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """Deletion of a Activity."""
    model = Activity
    template_name = "project_lists/delete_item_form.html"
    success_message = "Delete was successful."

    def get_success_url(self):
        list_id = Activity.objects.filter(id=self.kwargs.get('pk')).first().list.id
        return reverse('project_lists:details', kwargs={'pk': list_id})

    def get_context_data(self, **kwargs):
        context = super(ActivityDelete, self).get_context_data(**kwargs)
        context['message'] = self.success_message
        return context