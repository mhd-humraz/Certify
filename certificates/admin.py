from django.contrib import admin
from .models import Event, CertificateTemplate, Participant, Certificate


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'event_date', 'organizer', 'certificate_type', 'created_at']
    list_filter = ['certificate_type']
    search_fields = ['event_name', 'organizer']


@admin.register(CertificateTemplate)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ['template_name', 'is_active', 'created_at']
    list_filter = ['is_active']


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'college', 'course', 'event']
    list_filter = ['event']
    search_fields = ['name', 'email']


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['certificate_id', 'participant', 'event', 'issue_date', 'email_sent']
    list_filter = ['email_sent', 'event']
    search_fields = ['certificate_id', 'participant__name']
