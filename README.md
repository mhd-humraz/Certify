# 🎓 CertifyPro

### Smart Bulk Certificate Generation & Verification System

<p align="center">
  <img src="https://img.shields.io/badge/Django-4.2-green?style=flat-square&logo=django" />
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=flat-square" />
</p>

<p align="center">
  <strong>A modern Django-based platform for generating, managing, distributing, and verifying certificates at scale.</strong>
</p>

---

## ✨ Features

### Core Features

| Feature                         | Description                                                         |
| ------------------------------- | ------------------------------------------------------------------- |
| 📄 Bulk Certificate Generation  | Generate hundreds or thousands of certificates from Excel/CSV files |
| 🎨 Custom Certificate Templates | Upload PNG/JPG certificate backgrounds and customize layouts        |
| 🆔 Unique Certificate IDs       | Automatically generated IDs such as `CERT-2026-0001`                |
| 📱 QR Code Verification         | QR codes linked to public verification pages                        |
| ✉️ Email Automation             | Send certificates individually or in bulk                           |
| 📦 ZIP Export                   | Download all certificates of an event as a ZIP archive              |
| 🔍 Public Verification Portal   | Verify certificates using ID or QR scan                             |
| 📊 Analytics Dashboard          | Certificate generation and email delivery statistics                |

---

## 🖼️ Screenshots

### Dashboard

![Dashboard](docs/dashboard.png)

*Manage events, certificates, and statistics from a single dashboard.*

### Certificate Generation

![Generation](docs/generate.png)

*Generate certificates instantly with a single click.*

### Verification Portal

![Verification](docs/verify.png)

*Public portal for certificate authenticity verification.*

---

## 🔄 Workflow

```text
Create Event
      ↓
Import Participants
      ↓
Upload Template
      ↓
Generate Certificates
      ↓
Download / Email
      ↓
Verify via QR Code
```

---

## 🚀 How It Works

### 1. Create Event

Create a new event and enter event details.

### 2. Add Participants

Import participants using:

* CSV Files
* Excel Files (.xlsx)
* Manual Entry

Required columns:

```text
name
email
college
course
```

### 3. Upload Template

Upload a certificate template and configure:

* Name Position
* Course Position
* Date Position
* QR Position

### 4. Generate Certificates

Select:

* Event
* Template

Click **Generate Certificates**.

### 5. Download or Email

Available options:

* Individual PDF Download
* Bulk ZIP Download
* Single Email Delivery
* Bulk Email Delivery

### 6. Verify Certificates

Users can verify certificates by:

* Certificate ID
* QR Code Scan

Example:

```text
CERT-2026-0001
```

---

## ⚙️ Technology Stack

| Layer            | Technology              |
| ---------------- | ----------------------- |
| Backend          | Django 4.2              |
| Language         | Python 3.10+            |
| Database         | SQLite / PostgreSQL     |
| PDF Generation   | Pillow + ReportLab      |
| QR Generation    | qrcode                  |
| Excel Processing | openpyxl                |
| Frontend         | Bootstrap 5             |
| Deployment       | Docker, Gunicorn, Nginx |

---

## 🚀 Quick Start

### Prerequisites

* Python 3.10+
* pip

### Installation

```bash
git clone https://github.com/mhd-humraz/certifypro.git

cd certifypro

bash setup.sh

source venv/bin/activate

python manage.py runserver
```

Open:

```text
http://localhost:8000
```

Default Admin:

```text
Username: admin
Password: admin123
```

---

## 🐳 Docker Deployment

```bash
docker-compose up --build
```

Application will be available at:

```text
http://localhost
```

---

## 📁 Project Structure

```text
certifypro/
│
├── certifypro/
│   ├── settings.py
│   └── urls.py
│
├── certificates/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── utils.py
│   └── urls.py
│
├── templates/
├── static/
├── media/
│
├── sample_participants.csv
├── requirements.txt
├── setup.sh
├── Dockerfile
└── docker-compose.yml
```

---

## 🔒 Production Setup

### Security

```python
DEBUG = False

ALLOWED_HOSTS = [
    "your-domain.com"
]
```

### Email Configuration

```python
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = "your@email.com"
EMAIL_HOST_PASSWORD = "your_app_password"
```

### Database

Replace SQLite with PostgreSQL for production deployments.

---

## 🗺️ Roadmap

### Version 2.0

* [ ] Drag & Drop Certificate Designer
* [ ] WhatsApp Certificate Delivery
* [ ] Digital Signature Support
* [ ] Multi-Organization Support
* [ ] Certificate Expiry Management
* [ ] Public REST API

### Version 3.0

* [ ] AI Certificate Designer
* [ ] Canva Integration
* [ ] Blockchain Verification
* [ ] Advanced Analytics
* [ ] White-Label Solution
* [ ] Enterprise SSO

---

## 🌟 Upcoming Highlight

### Visual Drag & Drop Certificate Designer

Current Method:

```text
Name X = 450
Name Y = 300
```

Future Method:

```text
Upload Template
     ↓
Drag Name
     ↓
Drag Date
     ↓
Drag QR
     ↓
Save Layout
```

This feature will make CertifyPro feel like a commercial SaaS platform.

---

## 📈 Why CertifyPro?

✅ Generate 1000+ certificates in minutes

✅ QR-based public verification

✅ Bulk CSV/XLSX imports

✅ Custom certificate templates

✅ Automated email delivery

✅ ZIP export support

✅ Docker-ready deployment

✅ Event-based certificate management

---

## 👨‍💻 Author

### Muhammed Humraz H

**BCA Student • Flutter Developer • Community Builder • AI Enthusiast**

GitHub:
https://github.com/mhd-humraz

LinkedIn:
https://linkedin.com/in/muhammed-humraz-283a5435b

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/amazing-feature
```

3. Commit your changes

```bash
git commit -m "Add amazing feature"
```

4. Push your branch

```bash
git push origin feature/amazing-feature
```

5. Open a Pull Request

---

## 📄 License

Licensed under the **MIT License**.

See the `LICENSE` file for more information.

---

<p align="center">
  ⭐ If you like this project, please give it a star on GitHub! ⭐
</p>
