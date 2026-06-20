from django.db import models
from django.contrib.auth.models import User
import uuid


class Event(models.Model):
    CERTIFICATE_TYPES = [
        ('participation', 'Participation'),
        ('completion', 'Completion'),
        ('achievement', 'Achievement'),
        ('internship', 'Internship'),
        ('appreciation', 'Appreciation'),
    ]

    event_name = models.CharField(max_length=255)
    event_date = models.DateField()
    organizer = models.CharField(max_length=255)
    certificate_type = models.CharField(max_length=50, choices=CERTIFICATE_TYPES, default='participation')
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_name

    @property
    def certificate_count(self):
        return self.certificate_set.count()


class CertificateTemplate(models.Model):
    template_name = models.CharField(max_length=255)
    template_file = models.ImageField(upload_to='templates/')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    # Field positions (JSON-like stored as text, or use JSONField in Django 3.1+)
    name_x = models.IntegerField(default=400)
    name_y = models.IntegerField(default=300)
    name_font_size = models.IntegerField(default=40)
    name_color = models.CharField(max_length=20, default='#1a1a2e')

    event_x = models.IntegerField(default=400)
    event_y = models.IntegerField(default=380)
    event_font_size = models.IntegerField(default=24)

    date_x = models.IntegerField(default=400)
    date_y = models.IntegerField(default=430)
    date_font_size = models.IntegerField(default=18)

    cert_id_x = models.IntegerField(default=100)
    cert_id_y = models.IntegerField(default=520)
    cert_id_font_size = models.IntegerField(default=12)

    qr_x = models.IntegerField(default=700)
    qr_y = models.IntegerField(default=470)
    qr_size = models.IntegerField(default=80)

    def __str__(self):
        return self.template_name


class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    college = models.CharField(max_length=255, blank=True)
    course = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.event.event_name})"

    class Meta:
        unique_together = ['event', 'email']


class Certificate(models.Model):
    certificate_id = models.CharField(max_length=50, unique=True)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    template = models.ForeignKey(CertificateTemplate, on_delete=models.SET_NULL, null=True)
    pdf_file = models.FileField(upload_to='certificates/', blank=True, null=True)
    issue_date = models.DateField(auto_now_add=True)
    email_sent = models.BooleanField(default=False)
    email_sent_at = models.DateTimeField(null=True, blank=True)
    verification_status = models.CharField(max_length=20, default='valid')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.certificate_id

    @classmethod
    def generate_id(cls, year=None):
        from django.utils import timezone
        if year is None:
            year = timezone.now().year
        count = cls.objects.filter(certificate_id__startswith=f'CERT-{year}-').count() + 1
        return f'CERT-{year}-{count:04d}'
