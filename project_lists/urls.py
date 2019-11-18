from django.urls import path
from project_lists.views.PDF import Pdf
from project_lists.views.help import Help
from project_lists.views.use_case import CUView
from project_lists.views.use_case_add import CUAdd
from . import views
from .views import (DashBoardView, DashBoardAdd, ProjectUpdate, ProjectDelete,
                    ComponentUpdate, ComponentDelete, ComponentsView, ComponentAdd,
                    EstimationOptionsView, MTVEstimate, MTVDetailsView,
                    MTVMDetailsView, MTVMEstimate, RePCUDetailsView, RePCUEstimate, editMTV, editMTVM,
                    MTVDetailsEditView, MTVMDetailsEditView, TechFactorsAdd, EnvFactorsAdd, ActorsAdd, AddUC,
                    UseCaseDelete, AverageView, DuplicateView, duplicateAllData, editProject)

app_name = "project_lists"
urlpatterns = [

    # ABM DE PROYECTOS y estimacion
    path('dashboard/list_update/<int:pk>/', ProjectUpdate.as_view(), name='update_list'),
    path('dashboard/list_update/<int:pk>/project/edit', views.editProject, name='test'),
    path('dashboard/list_delete/<int:pk>/', ProjectDelete.as_view(), name='delete_list'),
    path('dashboard/<int:pk>/dashboard_add/', DashBoardAdd.as_view(), name='dashboard_add'),
    path('dashboard/project_delete/<int:pk>/', ProjectDelete.as_view(), name='dashboard_delete'),
    path('dashboard/', DashBoardView.as_view(), name='dashboard'),
    path('estimate/<int:project>/', EstimationOptionsView.as_view(), name='estimate'),
    path('dashboard/<int:pk>/<int:mod>/average_estimate/', AverageView.as_view(), name='average_estimate'),
    path('dashboard/<int:pk>/duplicate/', DuplicateView.as_view(), name='duplicate'),
    path('dashboard/<int:pk>/duplicate/duplicateAllData/', views.duplicateAllData, name='duplicateAllData'),


    # ABM DE COMPONENTES
    path('edit_project_components/<int:project>/<int:pk>/edit', ComponentUpdate.as_view(), name='components_edit'),
    path('edit_project_components/<int:pk>/add', ComponentAdd.as_view(), name='add_components'),
    path('edit_project_components/<int:project>/<int:pk>/delete', ComponentDelete.as_view(), name='component_delete'),
    path('edit_project_components/<int:pk>/components/', ComponentsView.as_view(), name='edit_project_components'),


    # METODOS DE ESTIMACION

    # MTV
    path('mtv/<int:pk>/mtv/editMTV/', views.editMTV, name='mtv_edit'),
    path('mtv/<int:pk>/view/', MTVDetailsView.as_view(), name='mtv_details'),
    path('mtv/<int:pk>/edit', MTVDetailsEditView.as_view(), name='mtv_details_edit'),
    path('mtv/<int:pk>/estimate', MTVEstimate.as_view(), name='mtv_estimate'),

    # MTV_M
    path('mtv_m/<int:pk>/mtvm/editMTVM/', views.editMTVM, name='mtvm_edit'),
    path('mtv_m/<int:pk>/view/', MTVMDetailsView.as_view(), name='mtvm_details'),
    path('mtv_m/<int:pk>/edit', MTVMDetailsEditView.as_view(), name='mtvm_details_edit'),
    path('mtv_m/<int:pk>/estimate', MTVMEstimate.as_view(), name='mtvm_estimate'),

    # REPCU
    path('repcu/<int:pk>/', RePCUDetailsView.as_view(), name='repcu_details'),
    path('repcu/<int:pk>/estimate', RePCUEstimate.as_view(), name='repcu_estimate'),

    # REPCU - FACT. TECNICOS
    path('repcu/<int:pk>/techfactors/', TechFactorsAdd.as_view(), name='techfactors'),
    path('repcu/<int:pk>/techfactors/editTF/', views.editTechFactors, name='techfactors_edit'),

    # REPCU - FACT. AMBIENTALES
    path('repcu/<int:pk>/envfactors/editEF/', views.editEnvFactors, name='envfactors_edit'),
    path('repcu/<int:pk>/envfactors/', EnvFactorsAdd.as_view(), name='envfactors'),

    # REPCU - ACTORES
    path('repcu/<int:pk>/actors/', ActorsAdd.as_view(), name='actors'),
    path('repcu/<int:pk>/actors/editAC/', views.editActors, name='actors_edit'),

    # REPCU - CASO DE USO
    path('repcu/<int:pk>/cuadd/', CUAdd.as_view(), name='use_case_add'),
    path('repcu/<int:pk>/cu/', CUView.as_view(), name='cu'),
    path('repcu/<int:pk>/cuadd/repcu/ucAdd', views.AddUC, name='add'),
    path('repcu/<int:comp>/<int:pk>/ucDel/', UseCaseDelete.as_view(), name='use_case_del'),
    path('repcu/<int:comp>/<int:pk>/ucDel/delete/', views.del_uc, name='use_case_delete_function'),


    # DOWNLOAD
    path('pdf/<int:met>/<int:pk>', Pdf.as_view(), name='pdf_MTV'),
    path('pdf/<int:met>/<int:pk>', Pdf.as_view(), name='pdf_MTVM'),
    path('pdf/<int:met>/<int:pk>', Pdf.as_view(), name='pdf_PCU'),

    path('help/', Help.as_view(), name='help'),

]
