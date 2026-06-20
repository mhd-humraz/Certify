# CertifyPro – Smart Bulk Certificate Generation & Verification System

A full-featured Django web application for generating, managing, distributing, and verifying certificates at scale.

---

## Features

- **Bulk Certificate Generation** — Upload participant Excel/CSV, generate PDF certificates instantly
- **Custom Templates** — Upload your own certificate backgrounds (PNG/JPG), configure field positions
- **Unique Certificate IDs** — Auto-generated IDs like `CERT-2026-0001`
- **QR Code Verification** — Every certificate has a QR code linking to a public verification page
- **Email Automation** — Send certificates individually or in bulk
- **ZIP Download** — Download all certificates for an event as a single ZIP file
- **Public Verification Portal** — Anyone can verify a certificate by ID or QR scan
- **Reports & Analytics** — Daily/monthly generation counts, email delivery rates

---

## Quick Start (Local Development)

### Prerequisites
- Python 3.10+
- pip

### Steps

```bash
# 1. Clone / unzip the project
cd certifypro

# 2. Run the setup script (creates venv, installs packages, migrates DB, creates admin)
bash setup.sh

# 3. Activate the venv and start the server
source venv/bin/activate
python manage.py runserver
```

Open **http://localhost:8000**

**Default credentials:** `admin` / `admin123`

---

## Docker Deployment

```bash
docker-compose up --build
```

Then visit **http://localhost**

---

## Usage Guide

### 1. Create an Event
Go to **Events → New Event** and fill in the details.

### 2. Add Participants
- **Manual:** Events → View → Participants → Add
- **Import:** Upload a CSV/Excel with columns: `name`, `email`, `college`, `course`

### 3. Upload a Template
Go to **Templates → Upload Template**. Upload a PNG/JPG certificate background and configure where name, date, QR code etc. should appear (pixel coordinates).

> **Tip:** If no template image is uploaded, CertifyPro generates a professional default background automatically.

### 4. Generate Certificates
Go to **Generate** (sidebar), select the event and template, click Generate.

### 5. Download & Email
From the **Event Detail** page:
- Download individual PDFs or a full ZIP
- Send emails one-by-one or bulk

### 6. Verify Certificates
- Visit `/verify/` (public page)
- Enter a Certificate ID like `CERT-2026-0001`
- Or scan the QR code on any printed certificate

---

## Project Structure

```
certifypro/
├── certifypro/          # Django project config
│   ├── settings.py
│   └── urls.py
├── certificates/        # Main app
│   ├── models.py        # Event, Participant, Template, Certificate
│   ├── views.py         # All views
│   ├── forms.py         # Django forms
│   ├── utils.py         # Certificate generation (Pillow + ReportLab)
│   └── urls.py
├── templates/           # HTML templates
│   ├── base.html
│   ├── registration/
│   └── certificates/
├── static/              # CSS/JS (Bootstrap CDN used)
├── media/               # Uploaded templates + generated certificates
├── sample_participants.csv
├── requirements.txt
├── setup.sh
├── Dockerfile
└── docker-compose.yml
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 4.2 |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Certificate Generation | Pillow + ReportLab |
| QR Codes | qrcode |
| Excel Parsing | openpyxl |
| Frontend | Bootstrap 5 + Bootstrap Icons |
| Deployment | Docker + Nginx + Gunicorn |

---

## Production Configuration

1. Change `SECRET_KEY` in `settings.py`
2. Set `DEBUG = False`
3. Update `ALLOWED_HOSTS`
4. Switch `EMAIL_BACKEND` to SMTP:
   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'your@email.com'
   EMAIL_HOST_PASSWORD = 'your_app_password'
   ```
5. Update database settings in `settings.py` for PostgreSQL

---

## Future Enhancements (from SRS)
- [ ] AI-powered certificate design
- [ ] Canva integration
- [ ] WhatsApp delivery
- [ ] Digital signatures
- [ ] Blockchain verification
- [ ] Certificate expiry management
- [ ] Multi-organization support
- [ ] Public API
