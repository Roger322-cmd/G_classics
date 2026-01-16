# Environment Variables Quick Reference

## 📚 Files Created

| File | Purpose |
|------|---------|
| `.env` | **Your actual configuration** (DO NOT commit) |
| `.env.example` | Template for reference (CAN commit) |
| `.gitignore` | Prevents .env from being committed |
| `ENV_SETUP.md` | Comprehensive setup guide |
| `ENV_CHECKLIST.md` | Step-by-step verification checklist |
| `create_env.sh` | Automated setup script for Unix/Linux |
| `create_env.bat` | Automated setup script for Windows |

## 🚀 Quick Start

### Step 1: Generate .env
**Windows:**
```bash
create_env.bat
```

**Mac/Linux:**
```bash
bash create_env.sh
```

### Step 2: Edit .env
Open `.env` and replace placeholder values with your actual configuration.

### Step 3: Verify Configuration
```bash
python manage.py check
```

### Step 4: Run Migrations
```bash
python manage.py migrate
```

## 🔑 Essential Variables

### Minimal Setup (Development)
```env
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=True
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
```

### Complete Setup (Production)
```env
DJANGO_SECRET_KEY=your-production-secret-key
DEBUG=False
DJANGO_ALLOWED_HOSTS=example.com,www.example.com
DB_ENGINE=django.db.backends.postgresql
DB_NAME=gclassics_prod
DB_USER=postgres_user
DB_PASSWORD=secure_password_here
DB_HOST=prod-db.example.com
DB_PORT=5432
USE_S3=True
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
AWS_STORAGE_BUCKET_NAME=prod-bucket
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

## 📖 Common Configurations

### PostgreSQL
```env
DB_ENGINE=django.db.backends.postgresql
DB_NAME=gclassics
DB_USER=postgres
DB_PASSWORD=postgres_password
DB_HOST=localhost
DB_PORT=5432
```

### MySQL
```env
DB_ENGINE=django.db.backends.mysql
DB_NAME=gclassics
DB_USER=root
DB_PASSWORD=mysql_password
DB_HOST=localhost
DB_PORT=3306
```

### Gmail SMTP
```env
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### AWS S3
```env
USE_S3=True
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
AWS_STORAGE_BUCKET_NAME=my-bucket-name
AWS_S3_REGION_NAME=us-east-1
```

### Redis Cache
```env
CACHE_BACKEND=django.core.cache.backends.redis.RedisCache
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
REDIS_PASSWORD=redis_password
```

## 🔐 Security Tips

1. **Generate Unique Secret Key**
   ```bash
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```

2. **File Permissions (Unix/Linux)**
   ```bash
   chmod 600 .env
   ```

3. **Never Commit .env**
   ```bash
   # Already in .gitignore
   git status  # Should NOT show .env
   ```

4. **Rotate Secrets Regularly**
   - Change every 90 days (API keys)
   - Change every 180 days (Database passwords)

5. **Use Different Values per Environment**
   ```
   Development: localhost, debug=true, local db
   Staging: staging.example.com, debug=false, staging db
   Production: example.com, debug=false, production db
   ```

## 🧪 Testing Configuration

```bash
# Check Django configuration
python manage.py check

# Test database connection
python manage.py dbshell

# Test email
python manage.py shell
# >>> from django.core.mail import send_mail
# >>> send_mail('Test', 'Message', 'from@example.com', ['to@example.com'])

# Test S3 connection
python manage.py shell
# >>> from django.core.files.storage import default_storage
# >>> default_storage.save('test.txt', 'content')
```

## 📋 Variable Categories

### Django Core (7 variables)
- DJANGO_SECRET_KEY
- DEBUG
- DJANGO_ALLOWED_HOSTS

### Database (6 variables)
- DB_ENGINE
- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT

### AWS S3 (5 variables)
- USE_S3
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_STORAGE_BUCKET_NAME
- AWS_S3_REGION_NAME

### Email (7 variables)
- EMAIL_BACKEND
- EMAIL_HOST
- EMAIL_PORT
- EMAIL_USE_TLS
- EMAIL_HOST_USER
- EMAIL_HOST_PASSWORD
- DEFAULT_FROM_EMAIL

### Payments (6 variables)
- PAYPAL_MODE
- PAYPAL_CLIENT_ID
- PAYPAL_SECRET_KEY
- STRIPE_PUBLIC_KEY
- STRIPE_SECRET_KEY

### Security (5 variables)
- CSRF_TRUSTED_ORIGINS
- SECURE_SSL_REDIRECT
- SESSION_COOKIE_SECURE
- CSRF_COOKIE_SECURE
- SECURE_BROWSER_XSS_FILTER

### Social Auth (4 variables)
- GOOGLE_CLIENT_ID
- GOOGLE_CLIENT_SECRET
- FACEBOOK_APP_ID
- FACEBOOK_APP_SECRET

### Other Settings (10+ variables)
- SITE_NAME
- SITE_URL
- SUPPORT_EMAIL
- CACHE_BACKEND
- REDIS_*
- LOG_LEVEL
- LOG_FILE
- PAGINATION_PAGE_SIZE
- MAX_LOGIN_ATTEMPTS
- PASSWORD_RESET_TIMEOUT
- SESSION_TIMEOUT
- DEBUG_TOOLBAR
- API_DOCS_URL

## 🐛 Common Issues & Solutions

### Issue: `ImproperlyConfigured` Exception
```
Solution: Check variable name spelling and .env location
```

### Issue: Database Connection Error
```
Solution: Verify credentials and ensure DB is running
Command: python manage.py dbshell
```

### Issue: Email Not Sending
```
Solution: Test SMTP, enable App Password for Gmail
Note: Use App Password, not regular Gmail password
```

### Issue: Static Files Not Loading
```
Solution: Run collectstatic
Command: python manage.py collectstatic
```

### Issue: S3 Upload Fails
```
Solution: Check IAM permissions and bucket name
Verify: AWS credentials and region are correct
```

## 📞 Need Help?

1. **Read the docs**
   - `ENV_SETUP.md` - Full setup guide
   - `ENV_CHECKLIST.md` - Step-by-step checklist

2. **Check logs**
   ```bash
   tail -f logs/django.log
   ```

3. **Run diagnostics**
   ```bash
   python manage.py check --deploy
   ```

4. **Debug mode**
   ```bash
   DEBUG=True python manage.py runserver
   ```

## 📝 Variable Reference

```
Total Variables: 50+
Mandatory: 3 (SECRET_KEY, DEBUG, DB_*)
Optional: 47 (AWS, Email, Payments, etc.)
```

## 🔗 Resources

- Django Settings: https://docs.djangoproject.com/en/5.0/ref/settings/
- Environment Variables: https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/
- Python-dotenv: https://python-dotenv.readthedocs.io/
- 12-Factor App: https://12factor.net/config

---

**Last Updated**: January 16, 2026
**Version**: 1.0
**Status**: ✅ Production Ready
