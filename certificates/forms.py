from django import forms
from .models import Event, CertificateTemplate, Participant


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_date', 'organizer', 'certificate_type', 'description']
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'event_name': forms.TextInput(attrs={'class': 'form-control'}),
            'organizer': forms.TextInput(attrs={'class': 'form-control'}),
            'certificate_type': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class TemplateForm(forms.ModelForm):
    class Meta:
        model = CertificateTemplate
        fields = [
            'template_name', 'template_file',
            'name_x', 'name_y', 'name_font_size', 'name_color',
            'event_x', 'event_y', 'event_font_size',
            'date_x', 'date_y', 'date_font_size',
            'cert_id_x', 'cert_id_y', 'cert_id_font_size',
            'qr_x', 'qr_y', 'qr_size',
        ]
        widgets = {
            'template_name': forms.TextInput(attrs={'class': 'form-control'}),
            'template_file': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'name_x': forms.NumberInput(attrs={'class': 'form-control'}),
            'name_y': forms.NumberInput(attrs={'class': 'form-control'}),
            'name_font_size': forms.NumberInput(attrs={'class': 'form-control'}),
            'name_color': forms.TextInput(attrs={'type': 'color', 'class': 'form-control form-control-color'}),
            'event_x': forms.NumberInput(attrs={'class': 'form-control'}),
            'event_y': forms.NumberInput(attrs={'class': 'form-control'}),
            'event_font_size': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_x': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_y': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_font_size': forms.NumberInput(attrs={'class': 'form-control'}),
            'cert_id_x': forms.NumberInput(attrs={'class': 'form-control'}),
            'cert_id_y': forms.NumberInput(attrs={'class': 'form-control'}),
            'cert_id_font_size': forms.NumberInput(attrs={'class': 'form-control'}),
            'qr_x': forms.NumberInput(attrs={'class': 'form-control'}),
            'qr_y': forms.NumberInput(attrs={'class': 'form-control'}),
            'qr_size': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'college', 'course']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'college': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField(
        label='Upload Excel / CSV File',
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': '.xlsx,.csv'})
    )


class BulkGenerateForm(forms.Form):
    event = forms.ModelChoiceField(
        queryset=Event.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Select Event'
    )
    template = forms.ModelChoiceField(
        queryset=CertificateTemplate.objects.filter(is_active=True),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Select Template'
    )
    base_url = forms.CharField(
        initial='http://localhost:8000',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Base URL (for QR verification links)',
        required=False
    )
