# Environment Variables Setup Guide

## Overview

This project uses environment variables to manage sensitive configuration data and settings. The `.env` file stores these variables locally and should **never be committed to version control**.

## File Structure

- **`.env`** - Your local environment file with actual values (DO NOT commit)
- **`.env.example`** - Template file that can be safely committed to version control
- **`.gitignore`** - Ensures .env files are never accidentally committed

## Quick Start

### 1. Create Your Local .env File

Copy the `.env.example` to `.env`:

```bash
cp .env.example .env
```

### 2. Update with Your Values

Open `.env` and replace all placeholder values with your actual configuration:

```bash
# Example:
DJANGO_SECRET_KEY=your-actual-secret-key-here
DEBUG=False
AWS_ACCESS_KEY_ID=your-actual-aws-key
```

### 3. Verify the .env is Not Tracked

```bash
git status
```

You should NOT see `.env` in the output. If you do, you may have accidentally committed it. See the "Fixing Mistakes" section below.

## Configuration Sections

### Django Core Settings

| Variable | Purpose | Example |
|----------|---------|---------|
| `DJANGO_SECRET_KEY` | Secret key for Django (MUST be unique) | Auto-generated, 50+ chars |
| `DEBUG` | Development mode flag | `True` (dev) / `False` (prod) |
| `DJANGO_ALLOWED_HOSTS` | Allowed hosts for CORS | `localhost,127.0.0.1,example.com` |

### Database Configuration

Configure your database connection:

```env
# SQLite (Default - Development)
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3

# PostgreSQL (Production)
DB_ENGINE=django.db.backends.postgresql
DB_NAME=gclassics_db
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432

# MySQL
DB_ENGINE=django.db.backends.mysql
DB_NAME=gclassics_db
DB_USER=root
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=3306
```

### AWS S3 Storage

To enable cloud storage for media files:

```env
USE_S3=True
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
AWS_STORAGE_BUCKET_NAME=g-classics-bucket
AWS_S3_REGION_NAME=us-east-1
```

### Email Configuration

For sending transactional emails:

```env
# Gmail SMTP
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# SendGrid
EMAIL_BACKEND=sendgrid_backend.SendgridBackend
SENDGRID_API_KEY=your-sendgrid-key
```

### Payment Gateways

#### PayPal

```env
PAYPAL_MODE=sandbox  # sandbox or live
PAYPAL_CLIENT_ID=AbCdEfGhIjKlMnOpQrStUvWxYz1234567890
PAYPAL_SECRET_KEY=EjF1KpL2MnO3PqR4StU5VwX6YzA7BcD8EfG9HiJ0KlM
```

#### Stripe

```env
STRIPE_PUBLIC_KEY=pk_test_51234567890abcdefg
STRIPE_SECRET_KEY=sk_test_1234567890abcdefghij
```

### Security Settings

```env
# HTTPS and Cookie Settings (Production)
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
SECURE_BROWSER_XSS_FILTER=True

# CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS=https://example.com,https://www.example.com
```

### Caching Configuration

```env
# In-Memory (Development)
CACHE_BACKEND=django.core.cache.backends.locmem.LocMemCache

# Redis (Production)
CACHE_BACKEND=django.core.cache.backends.redis.RedisCache
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
REDIS_PASSWORD=your-redis-password
```

## Security Best Practices

### 1. Generate a Strong Secret Key

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Replace the `DJANGO_SECRET_KEY` value with the output.

### 2. Environment-Specific Files

Create separate environment files for different environments:

```
.env.development  # Local development
.env.staging      # Staging server
.env.production   # Production server
```

### 3. Use a Secret Management Tool

For production, use dedicated secret management services:

- **AWS Secrets Manager** - Store secrets in AWS
- **HashiCorp Vault** - Enterprise secret management
- **Azure Key Vault** - Microsoft's secret management
- **1Password** - Team password manager
- **LastPass Enterprise** - Business password management

### 4. Rotate Secrets Regularly

Set reminders to rotate:
- API keys (every 90 days)
- Database passwords (every 180 days)
- Access tokens (as per service requirements)

### 5. Restrict File Permissions

On Unix/Linux:
```bash
chmod 600 .env
```

This restricts the file to be readable/writable only by the owner.

## Development vs Production

### Development Settings (.env)

```env
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
SECURE_SSL_REDIRECT=False
SESSION_COOKIE_SECURE=False
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

### Production Settings (.env)

```env
DEBUG=False
DJANGO_ALLOWED_HOSTS=example.com,www.example.com
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
DB_ENGINE=django.db.backends.postgresql
USE_S3=True
```

## Troubleshooting

### Issue: "django.core.exceptions.ImproperlyConfigured"

**Cause**: Environment variable not found
**Solution**: 
1. Check the variable name spelling in `.env`
2. Verify the file exists and is readable
3. Restart the Django development server

### Issue: Database Connection Error

**Cause**: Incorrect database credentials
**Solution**:
1. Test credentials manually in database client
2. Verify `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`
3. Check firewall rules allow database connection

### Issue: AWS S3 Upload Fails

**Cause**: Invalid AWS credentials or permissions
**Solution**:
1. Verify AWS credentials in AWS Console
2. Check IAM policy allows S3 bucket access
3. Verify bucket name is correct
4. Ensure `USE_S3=True` is set

### Issue: Email Not Sending

**Cause**: SMTP configuration incorrect
**Solution**:
1. Test SMTP credentials with an email client
2. For Gmail, use "App Password" not regular password
3. Enable "Less secure apps" for Gmail (if not using App Password)
4. Check spam folder for test emails

## Fixing Mistakes

### If You Accidentally Committed .env

```bash
# Remove from Git history (careful!)
git rm --cached .env
git commit -m "Remove .env from version control"

# Regenerate secrets
# 1. Generate new Django secret key
# 2. Update all API keys and passwords
# 3. Deploy new .env to servers
```

### If You Exposed Secrets

1. **Immediately revoke** all exposed secrets
2. Generate **new credentials** for all services
3. **Update** all environment files
4. **Redeploy** application with new secrets
5. **Review** git history for other exposures

## Loading Environment Variables

The project automatically loads variables from `.env` using `python-dotenv`:

```python
# In settings.py
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
DEBUG = os.getenv("DEBUG", "False") == "True"
```

## Additional Resources

- [Django Environment Variables](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)
- [Python-dotenv Documentation](https://python-dotenv.readthedocs.io/)
- [12-Factor App - Config](https://12factor.net/config)
- [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)

## Support

For questions or issues with environment setup, refer to:
1. `.env.example` - Template with all available variables
2. `requirements.txt` - All Python dependencies
3. Project documentation
4. GitHub Issues (if applicable)
