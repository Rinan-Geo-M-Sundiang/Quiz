from django.contrib import admin
from .models import BloodDonationRequest


class BloodDonationRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'request_type', 'blood_type', 'region', 'province', 'created_at')
    search_fields = ('user__username', 'blood_type', 'region', 'province')
    list_filter = ('blood_type', 'request_type', 'region', 'province')

    # Adding a custom action to the admin
    actions = ['mark_as_resolved']

    def mark_as_resolved(self, request, queryset):
        queryset.update(request_type='resolved')  # Custom bulk update action
        self.message_user(request, "Selected requests have been marked as resolved.")

    mark_as_resolved.short_description = "Mark selected requests as resolved"


admin.site.register(BloodDonationRequest, BloodDonationRequestAdmin)
