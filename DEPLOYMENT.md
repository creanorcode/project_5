# DEPLOYMENT

This guide explains how to deploy **Artea Studio** (Django) locally and on Heroku.

---

## 1. Requirements
- Python 3.12+
- Git
- Heroku account + Heroku CLI
- PostgreSQL (Heroku Postgres)
- AWS S3 bucket for media (production)
- Stripe account (test keys)
- SMTP provider (Resend)

---

## 2. Local Setup

### 2.1 Clone & Install
``` bash
git clone https://github.com/creanorcode/project_5.git
cd project_5
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2.2 Environment Variables (.env)

Create a `.env` file (use `env.example` as template):

Required:
- `SECRET_KEY`
- `DEBUG=True`
- `DATABASE_URL` (optional locally if using SQLite)
- `ALLOWED_HOSTS=127.0.0.1, localhost`

Optional services (if you want to test them locally):
- Stripe: `STRIPE_PUBLISHABLE_KEY`, `STRIPE_SECRET_KEY`
- SMTP: `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `CONTACT_RECIPIENT_EMAIL`

### 2.3 Run migrations & server
``` bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 3. Heroku Deployment

### 3.1 Create Heroku app

``` bash

heroku create <your-app-name>
```
### 3.2 Add Heroku Postgres
``` bash

heroku addons:create heroku-postgresql:essential-0
```
### 3.3 Config Vars (Heroku)
Set these in Heroku dashboard (Settings → Config Vars):

**Core**:
- `SECRET_KEY`
- `DEBUG=False`
- `ALLOWED_HOSTS=your-app.herokuapp.com,www.artea.studio,artea.studio`
- `DATABASE_URL` (created automatically by Heroku Postgres)
- `DJANGO_SETTINGS_MODULE=project_5.settings`

**Stripe**:
- `STRIPE_PUBLISHABLE_KEY`
- `STRIPE_SECRET_KEY`
- `STRIPE_WEBHOOK_SECRET_HEROKU` (if used)

**Email (Resend SMTP)**:
- `EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend`
- `EMAIL_HOST=smtp.resend.com`
- `EMAIL_PORT=465`
- `EMAIL_USE_SSL=True`
- `EMAIL_USE_TLS=False`
- `EMAIL_HOST_USER=resend`
- `EMAIL_HOST_PASSWORD=<your-resend-smtp-password>`
- `DEFAULT_FROM_EMAIL=Artea Studio <admin@artea.studio>`
- `CONTACT_RECIPIENT_EMAIL=admin@artea.studio`

**AWS S3 Media**:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_STORAGE_BUCKET_NAME`
- `AWS_S3_REGION_NAME`

---

## 4. AWS S3 Media Setup (Production)
1. Create S3 bucket (region matches `AWS_S3_REGION_NAME`)
2. Configure public access/bucket policy as required for media delivery
3. Create IAM user with S3 permissions
4. Add AWS credentials to Heroku config vars
5. Confirm uploads render correctly on deployed site

---

## 5. Static Files
- Production uses WhiteNoise for static files.

**On deploy, run**:
``` bash

python manage.py collectstatic --noinput
```

---

## 6. Database Migrations on Heroku

**After deploy**
``` bash

heroku run python manage.py migrate
heroku run python manage.py createsuperuser
``` 
 ---

## 7. Stripe Webhooks (Optional/If implemented)

**If using webhooks in production**:
 1. Create webhook endpoint in Stripe dashboard
 2. Set Webhook URL to:
    - https://<your-domain>/orders/stripe/webhook/ (example)
 3. Add the signing secret to Heroku config vars:
    - `STRIPE_WEBHOOK_SECRET_HEROKU`

---

## 8. SMTP Provider Setup (Resend)
1. Verify domain in Resend
2. Add DNS records in Porkbun (SPF/DKIM/MX as required by Resend)
3. Use Resend SMTP credentials in Heroku config vars
4. Test email via Contact form in rpoduction

---

## 9. Verify Deployment
Manual smoke tests after deploy:
- Home/Portfolio/Products load
- Cart + Stripe Checkout works (test card)
- Contact form saves + sends email
- Admin pages open without errors
- `robots.txt` and `sitemap.xml` load
