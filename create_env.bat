@echo off
REM Django Environment Setup Script for Windows
REM This script helps generate a secure .env file
REM Usage: create_env.bat

setlocal enabledelayedexpansion

echo.
echo ===== G-CLASSICS Django Environment Setup =====
echo.

REM Check if .env already exists
if exist .env (
    echo Warning: .env file already exists
    set /p overwrite="Do you want to overwrite it? (y/n): "
    if /i not "!overwrite!"=="y" (
        echo Keeping existing .env file
        exit /b 0
    )
)

echo Generating Django SECRET_KEY...
for /f "delims=" %%i in ('python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"') do set SECRET_KEY=%%i

echo Creating .env file...

(
    echo # ============================================================================
    echo # DJANGO CORE SETTINGS
    echo # ============================================================================
    echo.
    echo DJANGO_SECRET_KEY=%SECRET_KEY%
    echo DEBUG=True
    echo DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
    echo.
    echo # ============================================================================
    echo # DATABASE CONFIGURATION
    echo # ============================================================================
    echo.
    echo DB_ENGINE=django.db.backends.sqlite3
    echo DB_NAME=db.sqlite3
    echo DB_USER=
    echo DB_PASSWORD=
    echo DB_HOST=
    echo DB_PORT=
    echo.
    echo # ============================================================================
    echo # AWS S3 / CLOUD STORAGE CONFIGURATION
    echo # ============================================================================
    echo.
    echo USE_S3=False
    echo AWS_ACCESS_KEY_ID=
    echo AWS_SECRET_ACCESS_KEY=
    echo AWS_STORAGE_BUCKET_NAME=
    echo AWS_S3_REGION_NAME=us-east-1
    echo.
    echo # ============================================================================
    echo # EMAIL CONFIGURATION
    echo # ============================================================================
    echo.
    echo EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
    echo EMAIL_HOST=smtp.gmail.com
    echo EMAIL_PORT=587
    echo EMAIL_USE_TLS=True
    echo EMAIL_HOST_USER=
    echo EMAIL_HOST_PASSWORD=
    echo DEFAULT_FROM_EMAIL=noreply@g-classics.com
    echo.
    echo # ============================================================================
    echo # PAYMENT GATEWAY CONFIGURATION
    echo # ============================================================================
    echo.
    echo PAYPAL_MODE=sandbox
    echo PAYPAL_CLIENT_ID=
    echo PAYPAL_SECRET_KEY=
    echo.
    echo STRIPE_PUBLIC_KEY=
    echo STRIPE_SECRET_KEY=
    echo.
    echo # ============================================================================
    echo # SECURITY SETTINGS
    echo # ============================================================================
    echo.
    echo CSRF_TRUSTED_ORIGINS=http://localhost:8000,http://127.0.0.1:8000
    echo SECURE_SSL_REDIRECT=False
    echo SESSION_COOKIE_SECURE=False
    echo CSRF_COOKIE_SECURE=False
    echo SECURE_BROWSER_XSS_FILTER=True
    echo.
    echo # ============================================================================
    echo # SOCIAL AUTHENTICATION
    echo # ============================================================================
    echo.
    echo GOOGLE_CLIENT_ID=
    echo GOOGLE_CLIENT_SECRET=
    echo.
    echo FACEBOOK_APP_ID=
    echo FACEBOOK_APP_SECRET=
    echo.
    echo # ============================================================================
    echo # SITE CONFIGURATION
    echo # ============================================================================
    echo.
    echo SITE_NAME=G-CLASSICS
    echo SITE_URL=http://localhost:8000
    echo SUPPORT_EMAIL=support@g-classics.com
    echo.
    echo # ============================================================================
    echo # CACHING
    echo # ============================================================================
    echo.
    echo CACHE_BACKEND=django.core.cache.backends.locmem.LocMemCache
    echo CACHE_LOCATION=unique-snowflake
    echo REDIS_HOST=localhost
    echo REDIS_PORT=6379
    echo REDIS_DB=0
    echo REDIS_PASSWORD=
    echo.
    echo # ============================================================================
    echo # LOGGING CONFIGURATION
    echo # ============================================================================
    echo.
    echo LOG_LEVEL=INFO
    echo LOG_FILE=logs/django.log
    echo.
    echo # ============================================================================
    echo # APPLICATION SPECIFIC SETTINGS
    echo # ============================================================================
    echo.
    echo PAGINATION_PAGE_SIZE=50
    echo MAX_LOGIN_ATTEMPTS=5
    echo PASSWORD_RESET_TIMEOUT=3600
    echo SESSION_TIMEOUT=1800
    echo.
    echo # ============================================================================
    echo # DEVELOPMENT TOOLS
    echo # ============================================================================
    echo.
    echo DEBUG_TOOLBAR=False
    echo API_DOCS_URL=/api/docs/
    echo.
    echo # Generated: %date% %time%
    echo # Please keep this file secure and never commit it to version control
) > .env

echo.
echo ===== Setup Summary =====
echo [OK] Django SECRET_KEY generated
echo [OK] .env file created successfully!
echo.
echo [WARNING] TODO: Update placeholder values in .env
echo.
echo Next Steps:
echo 1. Open .env and update placeholder values:
echo    - AWS credentials
echo    - PayPal/Stripe keys
echo    - Email settings
echo    - Database credentials
echo.
echo 2. Test your configuration:
echo    python manage.py check
echo.
echo 3. Run migrations:
echo    python manage.py migrate
echo.
echo 4. Create superuser:
echo    python manage.py createsuperuser
echo.
echo 5. Start development server:
echo    python manage.py runserver
echo.
echo [WARNING] SECURITY REMINDER:
echo - Never commit .env to version control
echo - Regenerate SECRET_KEY in production
echo - Use strong, unique passwords
echo - Rotate credentials regularly
echo.
echo Setup complete!
echo.
pause
