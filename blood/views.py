from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import BloodDonationRequest
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import DeleteView
from .forms import BloodDonationRequestForm

class BloodRequestCreateView(CreateView):
    model = BloodDonationRequest
    form_class = BloodDonationRequestForm  # Use the form we just created
    template_name = 'blood/blood_request_form.html'
    success_url = reverse_lazy('blood_request_list')

    # Optionally, you can add more context or functionality to the view
    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign the current user to the request
        return super().form_valid(form)

class BloodRequestUpdateView(UpdateView):
    model = BloodDonationRequest
    form_class = BloodDonationRequestForm  # Use the form we just created
    template_name = 'blood/blood_request_form.html'
    success_url = reverse_lazy('blood_request_list')

    # Ensure user can only update if they own the request
    def get_queryset(self):
        return BloodDonationRequest.objects.filter(user=self.request.user)

class BloodRequestDeleteView(DeleteView):
    model = BloodDonationRequest
    template_name = 'blood/blood_request_confirm_delete.html'
    success_url = reverse_lazy('blood_request_list')

    # Ensure user can only delete if they own the request
    def get_queryset(self):
        return BloodDonationRequest.objects.filter(user=self.request.user)

class BloodRequestListView(ListView):
    model = BloodDonationRequest
    template_name = 'blood/blood_request_list.html'
    context_object_name = 'blood_requests'

    # Optionally, filter the list for the current user
    def get_queryset(self):
        return BloodDonationRequest.objects.all()
# Create your views here.
