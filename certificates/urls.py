from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Events
    path('events/', views.event_list, name='event_list'),
    path('events/create/', views.event_create, name='event_create'),
    path('events/<int:pk>/', views.event_detail, name='event_detail'),
    path('events/<int:pk>/edit/', views.event_edit, name='event_edit'),
    path('events/<int:pk>/delete/', views.event_delete, name='event_delete'),

    # Participants
    path('events/<int:event_pk>/participants/', views.participant_list, name='participant_list'),
    path('events/<int:event_pk>/participants/upload/', views.upload_participants, name='upload_participants'),
    path('participants/<int:pk>/delete/', views.participant_delete, name='participant_delete'),

    # Templates
    path('templates/', views.template_list, name='template_list'),
    path('templates/create/', views.template_create, name='template_create'),
    path('templates/<int:pk>/delete/', views.template_delete, name='template_delete'),

    # Certificates
    path('generate/', views.generate_bulk, name='generate_bulk'),
    path('certificates/<int:pk>/download/', views.certificate_download, name='certificate_download'),
    path('events/<int:event_pk>/download-zip/', views.download_zip, name='download_zip'),

    # Email
    path('certificates/<int:cert_pk>/send-email/', views.send_certificate_email, name='send_certificate_email'),
    path('events/<int:event_pk>/send-bulk-email/', views.send_bulk_email, name='send_bulk_email'),

    # Verification (public)
    path('certificate/verify/<str:certificate_id>/', views.verify_certificate, name='verify_certificate'),
    path('verify/', views.verify_search, name='verify_search'),

    # Reports
    path('reports/', views.reports, name='reports'),
]
