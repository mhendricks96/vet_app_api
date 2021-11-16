from django.urls import path
from .views import PetList, PetDetail, VeterinarianList, VeterinarianDetail, ParentList, ParentDetail, VisitList, VisitDetail

urlpatterns = [
  # path('', HomeView.as_view(), name='home'),
  path('pet_list/', PetList.as_view(), name='pet_list'),
  path('pet_list/<int:pk>/', PetDetail.as_view(), name='pet_detail'),
  path('vet_list/', VeterinarianList.as_view(), name='vet_list'),
  path('vet_list/<int:pk>/', VeterinarianDetail.as_view(), name='vet_detail'),
  path('parent_list/', ParentList.as_view(), name='parent_list'),
  path('parent_list/<int:pk>/', ParentDetail.as_view(), name='parent_detail'),
  path('visit_list/', VisitList.as_view(), name='visit_list'),
  path('visit_list/<int:pk>/', VisitDetail.as_view(), name='visit_detail'),
]