from django.urls import path
from .views import BloodRequestCreateView
from .views import BloodRequestUpdateView
from .views import BloodRequestDeleteView
from .views import BloodRequestListView
urlpatterns = [
    path('request/new/', BloodRequestCreateView.as_view(), name='blood_request_create'),
    path('request/<int:pk>/edit/', BloodRequestUpdateView.as_view(), name='blood_request_update'),
    path('request/<int:pk>/delete/', BloodRequestDeleteView.as_view(), name='blood_request_delete'),
    path('requests/', BloodRequestListView.as_view(), name='blood_request_list'),
]
