from django import forms
from .models import BloodDonationRequest


class BloodDonationRequestForm(forms.ModelForm):
    class Meta:
        model = BloodDonationRequest
        fields = ['request_type', 'blood_type', 'region', 'province', 'municipality']

    def __init__(self, *args, **kwargs):
        super(BloodDonationRequestForm, self).__init__(*args, **kwargs)

        # If the request type is 'donating', make certain fields read-only (user profile pre-fills this)
        if self.instance and self.instance.request_type == 'donating':
            self.fields['blood_type'].widget.attrs['readonly'] = True
            self.fields['region'].widget.attrs['readonly'] = True
            self.fields['province'].widget.attrs['readonly'] = True
            self.fields['municipality'].widget.attrs['readonly'] = True

    def clean(self):
        cleaned_data = super().clean()
        request_type = cleaned_data.get("request_type")
        if request_type == 'donating' and not self.instance.user.profile.availability:
            raise forms.ValidationError("You are not available to donate blood.")
        return cleaned_data
