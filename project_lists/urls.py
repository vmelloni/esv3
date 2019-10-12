from django.urls import path
from . import views
from .views import (DashBoardView, DashBoardAdd, ProjectUpdate, ProjectDelete,
                    ComponentUpdate, ComponentDelete, ComponentsView, ComponentAdd, 
                    EstimationOptionsView, MTVEstimate, MTVDetailsView,
                    MTVMDetailsView, MTVMEstimate, RePCUDetailsView, RePCUEstimate, editMTV, editMTVM)

app_name = "project_lists"
urlpatterns = [
    
    # ABM DE PROYECTOS y estimacion
    path('dashboard/list_update/<int:pk>/', ProjectUpdate.as_view(), name='update_list'),
    path('dashboard/list_delete/<int:pk>/', ProjectDelete.as_view(), name='delete_list'),
    path('dashboard/<int:pk>/dashboard_add', DashBoardAdd.as_view(), name='dashboard_add'),
    path('dashboard/project_delete/<int:pk>/', ProjectDelete.as_view(), name='dashboard_delete'),
    path('dashboard/', DashBoardView.as_view(), name='dashboard'),
    path('estimate/<int:project>/', EstimationOptionsView.as_view(), name='estimate'),

    # ABM DE COMPONENTES
    path('edit_project_components/<int:project>/<int:pk>/edit', ComponentUpdate.as_view(), name='components_edit'),
    path('edit_project_components/<int:pk>/add', ComponentAdd.as_view(), name='add_components'),
    path('edit_project_components/<int:project>/<int:pk>/delete', ComponentDelete.as_view(), name='component_delete'),
    path('edit_project_components/<int:pk>/components/', ComponentsView.as_view(), name='edit_project_components'),


    # METODOS DE ESTIMACION

    # MTV
    path('mtv/<int:pk>/mtv/editMTV/', views.editMTV , name='mtv_edit'),
    path('mtv/<int:pk>/', MTVDetailsView.as_view(), name='mtv_details'),
    path('mtv/<int:pk>/estimate', MTVEstimate.as_view(), name='mtv_estimate'),
    
    # MTV_M
    path('mtv_m/<int:pk>/mtvm/editMTVM/', views.editMTVM, name='mtvm_edit'),
    path('mtv_m/<int:pk>/', MTVMDetailsView.as_view(), name='mtvm_details'),
    path('mtv_m/<int:pk>/estimate', MTVMEstimate.as_view(), name='mtvm_estimate'),

    # REPCU
    path('repcu/<int:pk>/', RePCUDetailsView.as_view(), name='repcu_details'),
    path('repcu/<int:pk>/estimate', RePCUEstimate.as_view(), name='repcu_estimate'),
    
]
