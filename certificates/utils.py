"""
Certificate generation utilities using Pillow and ReportLab.
"""
import io
import os
import qrcode
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from django.conf import settings


def get_font(size=30, bold=False):
    """Try to load a system font, fall back to default."""
    font_paths = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
        '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
        '/System/Library/Fonts/Helvetica.ttc',
        'C:/Windows/Fonts/arial.ttf',
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()


def hex_to_rgb(hex_color):
    """Convert hex color string to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def generate_qr_code(url, size=150):
    """Generate a QR code image for a given URL."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=3,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color='black', back_color='white').convert('RGB')
    qr_img = qr_img.resize((size, size), Image.LANCZOS)
    return qr_img


def generate_certificate_image(template_obj, participant_name, event_name,
                                issue_date, certificate_id, verify_url,
                                certificate_type='participation'):
    """
    Generate a certificate as a PIL Image by overlaying text on the template image.
    Returns a PIL Image object.
    """
    # Open template image
    template_path = os.path.join(settings.MEDIA_ROOT, str(template_obj.template_file))

    if os.path.exists(template_path):
        img = Image.open(template_path).convert('RGB')
    else:
        # Create a default certificate background
        img = create_default_certificate_background(certificate_type)

    draw = ImageDraw.Draw(img)
    width, height = img.size

    # Helper to center text
    def draw_centered_text(text, y, font_size, color='#1a1a2e', x_override=None):
        font = get_font(font_size, bold=True)
        try:
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
        except AttributeError:
            text_width = len(text) * font_size * 0.6
        x = x_override if x_override else (width - text_width) // 2
        draw.text((x, y), text, font=font, fill=color)

    # Draw participant name (large, centered)
    name_font_size = template_obj.name_font_size or 48
    name_color = template_obj.name_color or '#1a1a2e'
    name_y = int(template_obj.name_y or height * 0.45)
    name_font = get_font(name_font_size, bold=True)
    try:
        bbox = draw.textbbox((0, 0), participant_name, font=name_font)
        text_width = bbox[2] - bbox[0]
    except AttributeError:
        text_width = len(participant_name) * name_font_size * 0.6
    name_x = (width - text_width) // 2
    draw.text((name_x, name_y), participant_name, font=name_font, fill=name_color)

    # Draw event name
    event_font_size = template_obj.event_font_size or 24
    event_y = int(template_obj.event_y or height * 0.57)
    draw_centered_text(event_name, event_y, event_font_size, color='#374151')

    # Draw date
    date_font_size = template_obj.date_font_size or 18
    date_y = int(template_obj.date_y or height * 0.65)
    draw_centered_text(
        f"Date: {issue_date.strftime('%B %d, %Y')}",
        date_y, date_font_size, color='#6b7280'
    )

    # Draw Certificate ID
    cert_id_font_size = template_obj.cert_id_font_size or 12
    cert_id_x = int(template_obj.cert_id_x or 60)
    cert_id_y = int(template_obj.cert_id_y or height - 70)
    cert_font = get_font(cert_id_font_size)
    draw.text((cert_id_x, cert_id_y), f"Certificate ID: {certificate_id}",
              font=cert_font, fill='#9ca3af')

    # Generate and paste QR code
    qr_size = int(template_obj.qr_size or 100)
    qr_x = int(template_obj.qr_x or width - qr_size - 60)
    qr_y = int(template_obj.qr_y or height - qr_size - 60)
    qr_img = generate_qr_code(verify_url, size=qr_size)
    img.paste(qr_img, (qr_x, qr_y))

    return img


def create_default_certificate_background(certificate_type='participation'):
    """Create a professional certificate background using Pillow."""
    width, height = 842, 595  # A4 landscape in pixels at 100dpi

    # Color schemes by type
    schemes = {
        'participation': {'bg': '#f8f9ff', 'accent': '#4f46e5', 'border': '#818cf8'},
        'completion': {'bg': '#f0fdf4', 'accent': '#16a34a', 'border': '#86efac'},
        'achievement': {'bg': '#fffbeb', 'accent': '#d97706', 'border': '#fcd34d'},
        'internship': {'bg': '#f0f9ff', 'accent': '#0284c7', 'border': '#7dd3fc'},
        'appreciation': {'bg': '#fdf4ff', 'accent': '#9333ea', 'border': '#d8b4fe'},
    }
    scheme = schemes.get(certificate_type, schemes['participation'])

    img = Image.new('RGB', (width, height), scheme['bg'])
    draw = ImageDraw.Draw(img)

    bg_color = hex_to_rgb(scheme['bg'])
    accent_color = hex_to_rgb(scheme['accent'])
    border_color = hex_to_rgb(scheme['border'])

    # Outer border
    margin = 20
    draw.rectangle([margin, margin, width - margin, height - margin],
                   outline=border_color, width=3)
    # Inner border
    inner_margin = 30
    draw.rectangle([inner_margin, inner_margin, width - inner_margin, height - inner_margin],
                   outline=accent_color, width=1)

    # Decorative top bar
    draw.rectangle([0, 0, width, 8], fill=accent_color)
    draw.rectangle([0, height - 8, width, height], fill=accent_color)

    # Header section background
    draw.rectangle([inner_margin + 5, inner_margin + 5, width - inner_margin - 5, 120],
                   fill=accent_color)

    # App name / header
    header_font = get_font(16, bold=True)
    draw.text((width // 2 - 60, 45), 'CertifyPro', font=header_font, fill='white')
    sub_font = get_font(11)
    cert_label = certificate_type.upper() + ' CERTIFICATE'
    draw.text((width // 2 - 70, 72), cert_label, font=sub_font, fill='rgba(255,255,255,180)')

    # "This is to certify that" text
    body_font = get_font(16)
    draw.text((width // 2 - 100, 155), 'This is to certify that', font=body_font, fill='#6b7280')

    # Decorative line under name area
    draw.line([(200, 310), (width - 200, 310)], fill=border_color, width=2)

    # "has successfully" text
    draw.text((width // 2 - 85, 325), 'has successfully participated in', font=body_font, fill='#6b7280')

    # Signature lines
    sig_y = height - 110
    draw.line([(100, sig_y), (260, sig_y)], fill='#d1d5db', width=1)
    draw.line([(width - 260, sig_y), (width - 100, sig_y)], fill='#d1d5db', width=1)
    sig_font = get_font(10)
    draw.text((140, sig_y + 5), 'Authorized Signatory', font=sig_font, fill='#9ca3af')
    draw.text((width - 220, sig_y + 5), 'Event Coordinator', font=sig_font, fill='#9ca3af')

    return img


def image_to_pdf(pil_image):
    """Convert a PIL Image to a PDF bytes object."""
    img_byte_arr = io.BytesIO()
    pil_image.save(img_byte_arr, format='PNG', dpi=(150, 150))
    img_byte_arr.seek(0)

    pdf_buffer = io.BytesIO()
    img_width, img_height = pil_image.size

    # Scale to A4 landscape at 72 dpi
    a4_w, a4_h = 842, 595
    c = canvas.Canvas(pdf_buffer, pagesize=(a4_w, a4_h))
    c.drawImage(ImageReader(img_byte_arr), 0, 0, width=a4_w, height=a4_h)
    c.save()

    pdf_buffer.seek(0)
    return pdf_buffer.read()
