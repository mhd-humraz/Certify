#!/bin/bash
# CertifyPro – Quick Setup Script
set -e

echo "=== CertifyPro Setup ==="

# 1. Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
echo "Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt

# 3. Run migrations
echo "Running migrations..."
python manage.py makemigrations certificates
python manage.py migrate

# 4. Create superuser
echo ""
echo "Creating admin user (username: admin, password: admin123)..."
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@certifypro.com', 'admin123')
    print('Admin user created.')
else:
    print('Admin user already exists.')
"

# 5. Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput 2>/dev/null || true

echo ""
echo "=== Setup complete! ==="
echo ""
echo "To start the server, run:"
echo "  source venv/bin/activate"
echo "  python manage.py runserver"
echo ""
echo "Then open: http://localhost:8000"
echo "Login:     admin / admin123"
echo ""
