from django.urls import path

from .views import (DashBoardView, ProjectUpdate, ProjectDelete,
                    DetailsView, ActivityUpdate, ActivityDelete)

app_name = "project_lists"
urlpatterns = [
    path('dashboard/list_update/<int:pk>/', ProjectUpdate.as_view(), name='update_list'),
    path('dashboard/list_delete/<int:pk>/', ProjectDelete.as_view(), name='delete_list'),
    path('dashboard', DashBoardView.as_view(), name='dashboard'),
    path('details/<int:pk>/', DetailsView.as_view(), name='details'),
    path('details/<int:pk>/update/', ActivityUpdate.as_view(), name='update_activity'),
    path('details/<int:pk>/delete/', ActivityDelete.as_view(), name='delete_activity'),
   ]
