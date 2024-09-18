from django.urls import path
from .views import BloodRequestCreateView, BloodRequestListView, BloodRequestUpdateView, BloodRequestDeleteView

urlpatterns = [
    path('blood_requests/', BloodRequestListView.as_view(), name='blood_request_list'),
    path('blood_request/create/', BloodRequestCreateView.as_view(), name='blood_request_create'),
    path('blood_request/<int:pk>/update/', BloodRequestUpdateView.as_view(), name='blood_request_update'),
    path('blood_request/<int:pk>/delete/', BloodRequestDeleteView.as_view(), name='blood_request_delete'),
]
