#!/bin/bash
# Django Environment Setup Script
# This script helps generate a secure .env file with random values
# Usage: bash create_env.sh

set -e

# Color codes for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== G-CLASSICS Django Environment Setup ===${NC}\n"

# Check if .env already exists
if [ -f .env ]; then
    echo -e "${YELLOW}Warning: .env file already exists${NC}"
    read -p "Do you want to overwrite it? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Keeping existing .env file"
        exit 0
    fi
fi

# Function to generate a random secret key
generate_secret_key() {
    python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
}

# Function to generate a random string
generate_random_string() {
    openssl rand -base64 32 | tr -d "=+/" | cut -c1-25
}

echo -e "${GREEN}Generating secure values...${NC}\n"

# Generate Django Secret Key
echo "Generating Django SECRET_KEY..."
SECRET_KEY=$(generate_secret_key)

# Generate random passwords
echo "Generating random values..."
DB_PASSWORD=$(generate_random_string)
REDIS_PASSWORD=$(generate_random_string)

# Create .env file
cat > .env << EOF
# ============================================================================
# DJANGO CORE SETTINGS
# ============================================================================

DJANGO_SECRET_KEY=$SECRET_KEY
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

# ============================================================================
# DATABASE CONFIGURATION
# ============================================================================

DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

# ============================================================================
# AWS S3 / CLOUD STORAGE CONFIGURATION
# ============================================================================

USE_S3=False
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_STORAGE_BUCKET_NAME=
AWS_S3_REGION_NAME=us-east-1

# ============================================================================
# EMAIL CONFIGURATION
# ============================================================================

EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
DEFAULT_FROM_EMAIL=noreply@g-classics.com

# ============================================================================
# PAYMENT GATEWAY CONFIGURATION
# ============================================================================

PAYPAL_MODE=sandbox
PAYPAL_CLIENT_ID=
PAYPAL_SECRET_KEY=

STRIPE_PUBLIC_KEY=
STRIPE_SECRET_KEY=

# ============================================================================
# SECURITY SETTINGS
# ============================================================================

CSRF_TRUSTED_ORIGINS=http://localhost:8000,http://127.0.0.1:8000
SECURE_SSL_REDIRECT=False
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False
SECURE_BROWSER_XSS_FILTER=True

# ============================================================================
# SOCIAL AUTHENTICATION
# ============================================================================

GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=

FACEBOOK_APP_ID=
FACEBOOK_APP_SECRET=

# ============================================================================
# SITE CONFIGURATION
# ============================================================================

SITE_NAME=G-CLASSICS
SITE_URL=http://localhost:8000
SUPPORT_EMAIL=support@g-classics.com

# ============================================================================
# CACHING
# ============================================================================

CACHE_BACKEND=django.core.cache.backends.locmem.LocMemCache
CACHE_LOCATION=unique-snowflake
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
REDIS_PASSWORD=$REDIS_PASSWORD

# ============================================================================
# LOGGING CONFIGURATION
# ============================================================================

LOG_LEVEL=INFO
LOG_FILE=logs/django.log

# ============================================================================
# APPLICATION SPECIFIC SETTINGS
# ============================================================================

PAGINATION_PAGE_SIZE=50
MAX_LOGIN_ATTEMPTS=5
PASSWORD_RESET_TIMEOUT=3600
SESSION_TIMEOUT=1800

# ============================================================================
# DEVELOPMENT TOOLS
# ============================================================================

DEBUG_TOOLBAR=False
API_DOCS_URL=/api/docs/

# Generated on: $(date)
# Please keep this file secure and never commit it to version control
EOF

echo -e "${GREEN}✓ .env file created successfully!${NC}\n"

# Set appropriate file permissions
chmod 600 .env
echo -e "${GREEN}✓ File permissions set to 600 (readable/writable by owner only)${NC}\n"

# Display summary
echo -e "${GREEN}=== Setup Summary ===${NC}"
echo -e "${GREEN}✓ Django SECRET_KEY generated${NC}"
echo -e "${GREEN}✓ File permissions secured${NC}"
echo -e "${YELLOW}⚠ TODO: Update placeholder values in .env${NC}"
echo -e "${YELLOW}⚠ TODO: Add .env to .gitignore (already done)${NC}\n"

# Show next steps
echo -e "${GREEN}Next Steps:${NC}"
echo "1. Open .env and update placeholder values:"
echo "   - AWS credentials"
echo "   - PayPal/Stripe keys"
echo "   - Email settings"
echo "   - Database credentials"
echo ""
echo "2. Test your configuration:"
echo "   python manage.py check"
echo ""
echo "3. Run migrations:"
echo "   python manage.py migrate"
echo ""
echo "4. Create superuser:"
echo "   python manage.py createsuperuser"
echo ""
echo "5. Start development server:"
echo "   python manage.py runserver"
echo ""

echo -e "${RED}⚠ SECURITY REMINDER:${NC}"
echo "- Never commit .env to version control"
echo "- Regenerate SECRET_KEY in production"
echo "- Use strong, unique passwords"
echo "- Rotate credentials regularly"
echo ""

echo -e "${GREEN}Setup complete!${NC}"
