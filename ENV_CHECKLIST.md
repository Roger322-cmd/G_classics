# Environment Configuration Checklist

## 📋 Pre-Setup

- [ ] Python 3.11+ installed
- [ ] Virtual environment activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Git initialized and .gitignore configured

## 🔧 Creating .env File

### Option 1: Automatic Setup (Recommended)

**On Windows:**
```bash
create_env.bat
```

**On macOS/Linux:**
```bash
bash create_env.sh
chmod +x create_env.sh
./create_env.sh
```

### Option 2: Manual Setup

1. Copy template:
```bash
cp .env.example .env
```

2. Update values as needed

## 🔐 Django Core Settings

- [ ] `DJANGO_SECRET_KEY` - Generated and unique (non-development value)
- [ ] `DEBUG` - Set to `False` for production
- [ ] `DJANGO_ALLOWED_HOSTS` - Updated with your domain(s)

## 📊 Database Configuration

### For SQLite (Development)
- [ ] `DB_ENGINE=django.db.backends.sqlite3`
- [ ] `DB_NAME=db.sqlite3`
- [ ] Other fields left empty

### For PostgreSQL (Production)
- [ ] `DB_ENGINE=django.db.backends.postgresql`
- [ ] `DB_NAME=<database_name>`
- [ ] `DB_USER=<username>`
- [ ] `DB_PASSWORD=<secure_password>`
- [ ] `DB_HOST=<host_address>`
- [ ] `DB_PORT=5432` (default)
- [ ] Database created on server
- [ ] Database user has necessary privileges

### For MySQL (Alternative)
- [ ] `DB_ENGINE=django.db.backends.mysql`
- [ ] `DB_NAME=<database_name>`
- [ ] `DB_USER=<username>`
- [ ] `DB_PASSWORD=<secure_password>`
- [ ] `DB_HOST=<host_address>`
- [ ] `DB_PORT=3306` (default)

## ☁️ AWS S3 Configuration (Optional)

- [ ] AWS account created
- [ ] S3 bucket created
- [ ] IAM user created with S3 access
- [ ] `USE_S3=True` (if using S3)
- [ ] `AWS_ACCESS_KEY_ID` - From IAM user
- [ ] `AWS_SECRET_ACCESS_KEY` - From IAM user
- [ ] `AWS_STORAGE_BUCKET_NAME` - Your bucket name
- [ ] `AWS_S3_REGION_NAME` - Correct region

## 📧 Email Configuration

### Using Gmail
- [ ] Gmail account created
- [ ] 2-factor authentication enabled (recommended)
- [ ] App Password generated (Settings > Security > App passwords)
- [ ] `EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend`
- [ ] `EMAIL_HOST=smtp.gmail.com`
- [ ] `EMAIL_PORT=587`
- [ ] `EMAIL_USE_TLS=True`
- [ ] `EMAIL_HOST_USER=<your-gmail@gmail.com>`
- [ ] `EMAIL_HOST_PASSWORD=<app-password>` (NOT regular password)

### Using SendGrid
- [ ] SendGrid account created
- [ ] API key generated
- [ ] `EMAIL_BACKEND=sendgrid_backend.SendgridBackend`
- [ ] `SENDGRID_API_KEY=<your-api-key>`

### Using Custom SMTP
- [ ] SMTP credentials obtained
- [ ] `EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend`
- [ ] `EMAIL_HOST=<smtp-server>`
- [ ] `EMAIL_PORT=<port>` (usually 587 or 465)
- [ ] `EMAIL_USE_TLS=True` (if port 587) or False (if port 465)
- [ ] `EMAIL_HOST_USER=<username>`
- [ ] `EMAIL_HOST_PASSWORD=<password>`

## 💳 Payment Gateway Setup

### PayPal
- [ ] PayPal Business account created
- [ ] Sandbox credentials obtained
- [ ] `PAYPAL_MODE=sandbox` (for testing)
- [ ] `PAYPAL_CLIENT_ID=<your-client-id>`
- [ ] `PAYPAL_SECRET_KEY=<your-secret-key>`

### Stripe
- [ ] Stripe account created
- [ ] API keys obtained
- [ ] `STRIPE_PUBLIC_KEY=pk_test_xxx` (test mode)
- [ ] `STRIPE_SECRET_KEY=sk_test_xxx` (test mode)

## 🔒 Security Settings

### For Development
- [ ] `SECURE_SSL_REDIRECT=False`
- [ ] `SESSION_COOKIE_SECURE=False`
- [ ] `CSRF_COOKIE_SECURE=False`

### For Production
- [ ] `SECURE_SSL_REDIRECT=True`
- [ ] `SESSION_COOKIE_SECURE=True`
- [ ] `CSRF_COOKIE_SECURE=True`
- [ ] `SECURE_BROWSER_XSS_FILTER=True`
- [ ] SSL certificate installed
- [ ] `CSRF_TRUSTED_ORIGINS` updated for your domain(s)

## 📱 Social Authentication (Optional)

### Google OAuth
- [ ] Google Cloud Console project created
- [ ] OAuth 2.0 credentials created (Web application)
- [ ] Authorized redirect URIs configured
- [ ] `GOOGLE_CLIENT_ID=<your-client-id>`
- [ ] `GOOGLE_CLIENT_SECRET=<your-secret>`

### Facebook OAuth
- [ ] Facebook App created
- [ ] App ID and Secret obtained
- [ ] Redirect URIs configured
- [ ] `FACEBOOK_APP_ID=<your-app-id>`
- [ ] `FACEBOOK_APP_SECRET=<your-app-secret>`

## 🔄 Caching Configuration

### For Development (Local Memory)
- [ ] `CACHE_BACKEND=django.core.cache.backends.locmem.LocMemCache`
- [ ] `CACHE_LOCATION=unique-snowflake`

### For Production (Redis)
- [ ] Redis server installed and running
- [ ] `CACHE_BACKEND=django.core.cache.backends.redis.RedisCache`
- [ ] `REDIS_HOST=<your-redis-host>`
- [ ] `REDIS_PORT=6379`
- [ ] `REDIS_DB=0`
- [ ] `REDIS_PASSWORD=<secure-password>` (if required)

## 📝 Logging Configuration

- [ ] `LOG_LEVEL=INFO` (or DEBUG for development)
- [ ] `LOG_FILE=logs/django.log`
- [ ] Logs directory exists or will be created
- [ ] Log file permissions configured

## 🏢 Site Configuration

- [ ] `SITE_NAME=G-CLASSICS` (your site name)
- [ ] `SITE_URL=http://localhost:8000` (or your domain)
- [ ] `SUPPORT_EMAIL=support@g-classics.com` (your email)

## ✅ Verification Steps

### 1. Check Syntax
```bash
python -m py_compile .env
```

### 2. Verify Settings
```bash
python manage.py check
```

### 3. Test Database Connection
```bash
python manage.py dbshell
# Type: .quit or .exit to exit
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
```

### 6. Test Email (if configured)
```bash
python manage.py shell
from django.core.mail import send_mail
send_mail(
    'Test Email',
    'This is a test email',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)
```

### 7. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 8. Start Development Server
```bash
python manage.py runserver
```

## 🔐 Security Checklist

- [ ] `.env` file added to `.gitignore`
- [ ] `.env` file permissions set to 600 (Unix/Linux)
- [ ] Never commit `.env` to version control
- [ ] All placeholder values replaced
- [ ] Secrets rotated from any backups
- [ ] Database user has minimal required privileges
- [ ] HTTPS enabled in production
- [ ] Secret keys are environment-specific
- [ ] Sensitive logs are not tracked in git

## 📦 Deployment Preparation

### Before Going to Production

- [ ] All environment variables tested locally
- [ ] Debug mode set to False
- [ ] ALLOWED_HOSTS configured correctly
- [ ] Static files collected
- [ ] Media directory configured
- [ ] Database backed up
- [ ] Email service tested
- [ ] Monitoring and logging configured
- [ ] Backup and recovery plan documented
- [ ] SSL certificate installed

## 🆘 Troubleshooting

| Issue | Solution |
|-------|----------|
| `django.core.exceptions.ImproperlyConfigured` | Check if .env exists and variable is spelled correctly |
| Database connection error | Verify DB credentials and ensure database is running |
| Email not sending | Check SMTP settings, enable "Less secure apps" for Gmail |
| Static files not loading | Run `python manage.py collectstatic` |
| Permission denied on .env | Run `chmod 600 .env` on Unix/Linux |
| Secret key error | Regenerate with `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'` |

## 📞 Support Resources

- [Django Environment Variables](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)
- [Python-dotenv Documentation](https://python-dotenv.readthedocs.io/)
- [AWS S3 Setup](https://docs.aws.amazon.com/s3/latest/userguide/getting-started-with-s3.html)
- [PayPal Integration](https://developer.paypal.com/)
- [Stripe Integration](https://stripe.com/docs)
- [12-Factor App Configuration](https://12factor.net/config)

---

**Last Updated**: January 16, 2026
**Status**: ✅ Ready for Development
