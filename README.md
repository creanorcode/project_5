## Executive Summary

**Artea Studio** is a full-stack e-commerce platform built with Django, designed for selling and delivering creative digital products and custom design services.  
It combines a minimalist user experience with secure Stripe payments, automated email confirmations, and an intuitive admin interface for managing orders and uploads.  
The project demonstrates a complete commercial workflow — from browsing and checkout to post-purchase delivery — and applies modern UX, SEO, and Agile principles throughout the development process.  

---

# Artea Studio - Graghic Design Shop

**Artea Studio** is a full-stack Django e-commerce web application designed to offer design products and custom creative services. The platform enables users to browse, purchase, and download digital assets, as well as submit custom design requests directly through the site.

- Deployed Site: [https://www.artea.studio](https://www.artea.studio)
- GitHub Repository: [https://github.com/creanorcode/project_5.git](https://github.com/creanorcode/project_5.git)

[![Artea-Mockup.png](https://i.postimg.cc/k5x9hK64/Artea-Mockup.png)](https://postimg.cc/t1CLs1zQ)

---
## Artea – Digital Design Marketplace

**Artea** is a modern and user-friendly web application for ordering, managing, and delivering custom graphic design products. Built with Django, HTML/CSS, JavaScript and Stripe integration, the platform connects clients with designers and streamlines the creative workflow from design request to secure download.

Key features include:
- A dynamic storefront with filterable design products
- Custom design order form with file upload
- Stripe payments for both physical products and completed design deliveries
- Admin panel for managing orders, uploads, and payment status
- User dashboard with messaging, downloads, and order history

The platform is fully responsive and optimized for both desktop and mobile users.

---

## Table of Contents

1. [Overview](#overview)  
2. [UX and Design](#ux-and-design)  
3. [Features](#features)  
4. [Full Features Walkthrough](#full-features-walkthrough)
5. [Data Model](#data-model)  
6. [Agile Development & User Stories](#agile-development--user-stories)  
7. [Payments & E-commerce Flow](#payments--e-commerce-flow)  
8. [Testing](#testing)  
9. [SEO Implementation](#seo-implementation)  
10. [Marketing & Business Model](#marketing--business-model)  
11. [Deployment](#deployment)  
12. [Code Quality & Validation](#code-quality--validation)  
13. [Technologies Used](#technologies-used)  
14. [Project Structure](#project-structure)
15. [Assessor Evidence Summary](#assessor-evidence-summary)
16. [Known Limitations & Future Work](#known-limitations--future work)
17. [Credits](#credits)

---

## Overview

**Artea Studio** combines creativity and digital commerce.

**Users can:**
- Browse and purchase downloadable design assets.
- Submit custom design orders.
- Pay securely using Stripe Checkout.
- Receive email confirmations and access completed designs.

The application prioritizes clarity, usability, and scalability, following Django´s MVT pattern and Code Institute best practices.

---

## UX and Design

### Branding
A calm, creative visual language reflecting the artistic identity of *Artea Studio*.  
- **Color Scheme**
  - Primary: '#2d89ef'
  - Secondary: '#f59e0b'
  - Accents: '#f9d342', '#dd4c4f', '#207f62'
- **Typography:** clean sans-serif with subtle contrast  
- **Layout:** grid-based with clear hierarchy
- **Hero with CTAs**, dynamic role-based nav and footer
- **Forms:** manually rendered with role-aware behavior
- **Feedback:** Django messages for success/errors

### Wireframes & Mockups
Se `/docs/wireframes` for key screens and flows.

---

## Features

This section describes all implemented functionality of the Artea Studio application.  
The platform includes secure user authentication, Stripe checkout, CRUD-based product and design management, and an intuitive UX across devices.  
Below is a detailed breakdown of all key features and how they appear throughout the user journey.

### Existing Features
- Fully responsive layout (mobile, tablet, desktop).
- Portfolio page with design examples.
- Design Order form with file upload and notes.
- Stripe payment integration (test mode)
- User registration / login / logout.
- User dashboard with downloadable files.
- Admin panel for orders/files and payment status.
- Contact form (email), newsletter signup (mock).
- Custom 404 page, `robots.txt` and `sitemap.xml`.
- Role-based navigation (user, staff, superuser).

#### User Features
  - Browse featured & bespoke designs
  - Register, log in/out, manage account
  - Place design requests with file upload
  - Pay securely with Stripe
  - View order history and download completed work
  - Subscribe to newsletter (mockup)

#### Admin Features
  - Django Admin with enhanced lists & filters
  - Manage users, orders, designs, and messages
  - Mark designs as completed/paid
  - Staff-only frontend admin shortcuts.

#### Payment Integration
  - Stripe checkout with success/cancel pages
  - Payment status stored per orders/design
  - Download link shown after payment

#### Responsive Design
  - Responsive menus for all devices
  - Accessible layout with strong UX focus

### Future Features
- Ratings & reviews; richer messaging (attachments, read status)
- PDF preview before download
- Topic-based template categories
- AI-assisted recommendations
- Admin notifications; order status workflow
- Secure token/expiry for downloads
- Export order history (CSV)
- Dark mode toggle; improved staff dashboard
- Social gallery integrations


### Limitations & Areas for Improvement
  - Some Python files still contain long lines and lack full flake8 compliance
  - The mobile menu dropdown had display inconsistencies across devices during development
  - The Facebook dummy login feature has not yet been implemented
  - The README could benefit from additional screenshots and testing documentation
  - Admin functionality is minimal and could be expanded
  - Payment success flow for custom design orders needs polish to avoid 500 errors
  - User experience (UX) flow can be further improved with animations and transitions
  - Error handling is basic and can be enhanced across the platform

---

## Full Features Walkthrough

This walkthrough demonstrates key pages, features, and user interactions.
Each section provides brief context and screenshot placeholders.

### Home Page
- Hero with CTAs, welcome text, quick links to Products/Portfolio/Contact, and featured content.

Screenshots:  
[![screenshot-hero.png](https://i.postimg.cc/B6H48yfM/screenshot-hero.png)](https://postimg.cc/njF6g3zD)
[![screenshot-footer.png](https://i.postimg.cc/cJVdLW2v/screenshot-footer.png)](https://postimg.cc/v1LJ0JQy)

### Portfolio
- Responsive image grid; titles & descriptions; mobile-friendly.

[![screenshot-portfolio.png](https://i.postimg.cc/KzRQJS8D/screenshot-portfolio.png)](https://postimg.cc/ygCF8G9D)


### Products
- Grid of product cards (image, title, price); detail pages.

Product grid page
[![screenshot-productpage.png](https://i.postimg.cc/gkNXkwDr/screenshot-productpage.png)](https://postimg.cc/KR3v08Cy)
product item page
[![screenshot-productitempage.png](https://i.postimg.cc/kgGVVn1s/screenshot-productitempage.png)](https://postimg.cc/mPxZJGG1)

### Design Order
- Core flow for custome requests; validated form with clean UX.

[![screenshot-designform.png](https://i.postimg.cc/nzGVR5SM/screenshot-designform.png)](https://postimg.cc/XGX0X2b0)

### Cart
- Itemized list, quantities, totals; connects to Stripe test payments.

[![screenshot-cart.png](https://i.postimg.cc/nV6jsbbf/screenshot-cart.png)](https://postimg.cc/F1Vsq6HT)

### Contact
- Name, email, message; Django messages for feedback.

[![screenshot-contact.png](https://i.postimg.cc/6pBQRBMg/screenshot-contact.png)](https://postimg.cc/GHSrnnwx)

### My Account (Authenticated)
- **My Orders**, **My Designs**, **My Messages**, **My Conversations**, secure Logout.

Menu:
[![screenshot-myaccount-menu.png](https://i.postimg.cc/HsgMZDS4/screenshot-myaccount-menu.png)](https://postimg.cc/z3x3vMYV)


**My Designs (unpaid vs paid)**
[![screenshot-mydesigns-notpaid.png](https://i.postimg.cc/fRKngTpN/screenshot-mydesigns-notpaid.png)](https://postimg.cc/LJnbJRmC)
[![screenshot-mydesigns.png](https://i.postimg.cc/HLHRwDkh/screenshot-mydesigns.png)](https://postimg.cc/fV28sPXc)


**My Orders**
[![screenshot-myorders.png](https://i.postimg.cc/bw8fT26g/screenshot-myorders.png)](https://postimg.cc/rKhHyz2R)
[![screenshot-orderitems.png](https://i.postimg.cc/Dy1KLccm/screenshot-orderitems.png)](https://postimg.cc/xcj7SMhS)


**My Messages**
[![screenshot-My-Contact-Messages.png](https://i.postimg.cc/Kz6T9sG3/screenshot-My-Contact-Messages.png)](https://postimg.cc/gXKrjs6G)
[![screenshot-My-Contact-Message-Thread.png](https://i.postimg.cc/0QMm0qsq/screenshot-My-Contact-Message-Thread.png)](https://postimg.cc/zbNVq6vd)


**My Conversations**
[![screenshot-My-Conversations.png](https://i.postimg.cc/SRcMH7RT/screenshot-My-Conversations.png)](https://postimg.cc/zHXvghnK)
[![screenshot-My-Conversations-Thread.png](https://i.postimg.cc/Y2FY4kR6/screenshot-My-Conversations-Thread.png)](https://postimg.cc/CdFzt3W5)

### Admin Panel (Backend)
- Manage design orders, messages, users, and completed designs.

[![screenshot-admin-backend.png](https://i.postimg.cc/44LYjXCp/screenshot-admin-backend.png)](https://postimg.cc/rz4yrXwp)


### Staff Tools (Frontend)
- Quick actions to mark paid, manage uploaded work.

[![screenshot-adminpanel-frontend.png](https://i.postimg.cc/L5Y2cKfV/screenshot-adminpanel-frontend.png)](https://postimg.cc/dZYbCf57)

### Navigation & Responsiveness
- Mobile/tablet hamburger; hover/click behaviors; accessible layout.

**iPhone 14 Pro Max**
[![screenshot-main-nav-i-Phone-14-pro-max.png](https://i.postimg.cc/W1LTy1nW/screenshot-main-nav-i-Phone-14-pro-max.png)](https://postimg.cc/Tp9zLGBg)

**iPad pro**
[![screenshot-main-Nav-ipad-pro.png](https://i.postimg.cc/hvt1cn1N/screenshot-main-Nav-ipad-pro.png)](https://postimg.cc/bD4t9KMR)

**Landscape mode**
[![screenshot-man-Nav-ipad-pro-landscape.png](https://i.postimg.cc/zv2SfQdv/screenshot-man-Nav-ipad-pro-landscape.png)](https://postimg.cc/BPD1Ymff)

### Auth Screens
**Login**
[![screenshot-login-Page.png](https://i.postimg.cc/Bbb7NHk8/screenshot-login-Page.png)](https://postimg.cc/QKLqd9Xs)

**Logout**
[![screenshot-logoutpage.png](https://i.postimg.cc/pVc6rc5K/screenshot-logoutpage.png)](https://postimg.cc/DmsgYggz)

### Register
[![screenshot-registerpage.png](https://i.postimg.cc/G2qSkq7w/screenshot-registerpage.png)](https://postimg.cc/R6JRmQxX)

---

## Example User Flow

1. User lands on homepage  
2. Clicks on "Products" to explore items  
3. Adds product to cart and proceeds to checkout  
4. Or fills out the Design Order form for a custom request  
5. Logs in to track "My Orders" and "My Designs"  
6. Uses "My Conversations" to message the designer  
7. Staff log in to manage requests via admin panel

---

---

## Data Model

Relational schema via Django ORM.

**Key models:**
- `Product` – digital items for sale  
- `DesignOrder` – user-submitted design requests  
- `CompletedDesign` – uploaded results of custom orders (unlock after payment)  
- `Order`, `OrderItem` – e-commerce order management  
- `DesignType` – categorization for custom services  

Each model supports CRUD operations and integrates with Django Admin.

*(Add ERD image or link here - e.g. `doc/erd/artea-erd.png`)*

---

## Agile Development & User Stories

- Agile-inspired workflow using GitHub Projects: `To Do -> In Progress -> Done`.
- User stories follow the format “As a user, I want to … so that I can …”

| ID | User Story | Implementation |
|----|-------------|----------------|
| US-01 | As a visitor, I want to understand the brand quickly | Home hero with cleart CTAs |
| US-02 | As a user, I want to register/login to manager my orders | Accounts app, auth views |
| US-03 | As a user, I want to submit a custom design request | DesignOrder form & storage|
| US-04 | As a user, I want to pay securely | Stripe Checkout |
| US-05 | As a user, I want to download completed designs | CompletedDesign with paid gate |
| US-06 | As admin, I want to manage orders/designs | Enhanced Django Admin views |

*(Optional) Include a screenshot of GitHub Projects board in `docs/screenshots/`.*

---

## Payments & E-Commerce Flow

Two flows are supported:

1. **Shop flow (predefined products)**  
2. **Custom design flow (pay for a completed design)**  

After a successful Stripe payment:
- User is redirected to `/payment/success/`
- A **confirmation email** is sent
- The related order/design instance is marked as `paid`

Test with Stripe´s card: `4242 4242 4242 4242` (aný future expiry, any CVC).

Success/Cancel templates: `templates/orders/payment_success.html` and `payment_cancelled.html`.

---

## Testing
For the complete testing process and validation evidence, see the [TESTING.md](./TESTING.md) file.

### Manual Feature Testing

| Feature | Action | Expected | Result |
|----------|---------|----------|---------|
| Register / Login | Submit valid credentials | Redirect to dashboard | ✅ |
| Product Checkout | Pay with test card | Success page + email | ✅ |
| Design Payment | Pay for completed design | Unlock download + email | ✅ |
| robots.txt / sitemap.xml | Open endpoints | Valid responses | ✅ |

*(Add more rows as needed)*

### Validator Testing
- **HTML/CSS** W3C Validators - no critical errors  
- **Python** `ruff check . --fix` - no E/F-level issues  
- **Lighthouse** Performance > 90, Accessibility > 95  
- **Stripe** Test transactions completed successfully  

Screenshots stored in `docs/screenshots/`.

---

## SEO Implementation

- `robots.txt` at site root
- Dynamic `sitemap.xml`(Django sitemaps)
- Meta descriptions on key pages
- `rel="noopener noreferrer"`for external links
- Open Graph tags (title/description)

Validation via local endpoints and screenshots included

---

## Marketing & Business Model

- **Business Model:** Hybrid - digital products sales + custom design services.
- **Revenue:** One-off Stripe payments; future bundles/subscriptions.
- **Target Users:** Small business owners, creators, educators, influencers.
- **Marketing:** Newsletter signup (mock), Facebook page mockup (screenshot), SEO metadata.

- **Value Proposition:** Personal, mindful design with efficient digital delivery.

---

## Deployment

### Hosting & Stack
- **Platform:** Heroku (Gunicorn, Whitenoise) 
- **Database:** PostgreSQL (prod), SQLite (dev)  
- **Media:** Local in dev; S3 for prod

### Environment Configuration
Use `.env` (see `.env.example`).

```env
SECRET_KEY=your-secret
DEBUG=False
DATABASE_URL=your-heroku-postgres-url
ALLOWED_HOSTS=artea-studio-*.herokuapp.com, www.artea.studio, artea.studio
CSRF_TRUSTED_ORIGINS=https://artea-studio-*.herokuapp.com, https://www.artea.studio, https://artea.studio
STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...
SITE_URL=https://www.artea.studio
```

### Steps
1. Connect GitHub repo to Heroku app.
2. Set Config Vars (above).
3. Run:
```
bash

python manage.py migrate
python manage.py collectstatic --noinput
```
4. (Optional) Create superuser & seed demo data.

---

## Code Quality & Validation
- Code linted & formatted with **Ruff**:
  '''
  bash

  ruff check . --fix
  '''
- PEP8 conventions followed (line-length exceptions documented if needed).
- Production security: `DEBUG=False`, SSL redirect, HSTS, secure cookies.

---

## About Artea – Vision & Market Position ?????????????????????????????

**Artea** offers a clean and elegant solution for digital design services. It's designed for individuals, entrepreneurs and small businesses who need fast, affordable, and customized visual content—without hiring a full-time designer.

### Problem
Most digital design solutions today are either:
- Too complex (enterprise tools with steep learning curves)
- Too expensive (agencies or subscription-based platforms)
- Too limited (template-based tools with no customization)

### Solution
Artea solves this by providing:
- A direct channel to request custom designs
- A simple, one-time payment flow per project
- Personal download access after delivery
- Optional messaging between customer and designer
- Admin control to manage design uploads and payment status

### Target Users
- Entrepreneurs and small business owners
- Creatives in need of album covers, flyers, branding assets
- Social media managers and influencers

### Future Potential
- Add freelancer onboarding and bidding
- Add customer reviews and portfolios
- Offer bundled design packages or subscriptions

**Artea** is more than a demo — it's a scalable foundation for a design-focused e-commerce service.

---

## Technologies Used
- **Frontend:** HTML5, CSS3, Javascript, Bootstrap
- **Backend:** Python 3, Django 5
- **Payments:** Stripe Checkout
- **Database:** SQLite (dev), PostgreSQL (prod)
- **DevOps:** Heroku, Gunicorn, Whitenoise
- **Tooling:** Ruff, Pillow, python-dotenv
- **VCS:** Git & GitHub

---

## Project Structure (Overview)
```
project_5/
├── manage.py
├── requirements.txt
├── runtime.txt
├── Procfile
├── README.md
├── check_default_storage.py
├── check_storage.py
├── static/
│ ├── css/
│ ├── js/
│ └── images/
├── templates/
│ ├── 404.html
│ ├── base.html
│ ├── home.html
│ ├── logout.html
│ ├── newsletter.html
│ ├── portfolio.html
│ ├── accounts/
│ ├── contact/
│ ├── orders/
│ └── registration/
├── accounts/
│ ├── forms.py
│ ├── urls.py
│ ├── views.py
│ └── ...
├── cart/
│ ├── urls.py
│ ├── views.py
│ └── ...
├── contact/
│ ├── forms.py
│ ├── urls.py
│ ├── views.py
│ └── ...
├── orders/
│ ├── forms.py
│ ├── urls.py
│ ├── views.py
│ └── ...
├── portfolio/
│ ├── forms.py
│ ├── urls.py
│ ├── views.py
│ └── ...
├── products/
│ ├── models.py
│ ├── urls.py
│ ├── views.py
│ └── ...
├── project_5/
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ ├── asgi.py
│ ├── custom_storages.py
│ └── init.py
```

---

## Assessor Evidence Summary
| Requirement         | Evidence                                                 |
| ------------------- | -------------------------------------------------------- |
| E-commerce payments | Stripe Checkout with success/cancel; confirmation emails |
| CRUD & Models       | Product, DesignOrder, CompletedDesign, Order/OrderItem   |
| Agile               | User story table + Project board (screenshot)            |
| Testing             | Manual test table + validators + screenshots             |
| SEO                 | `robots.txt`, `sitemap.xml`, meta & OG tags              |
| Marketing           | Newsletter + Facebook mockup                             |
| Deployment          | Heroku steps + env config                                |
| Code Quality        | Ruff/PEP8 compliance                                     |

---

## Deployment & Access ??????????????????????

The Artea platform is currently deployed and publicly accessible at the following address:

**Live site:** [https://artea-studio-571c2301b41f.herokuapp.com](https://artea-studio-571c2301b41f.herokuapp.com)
**Live site:** [https://www.artea.studio](https://www.artea.studio)
**Live site:** [https://artea.studio](https://artea.studio)

You can explore the site as a guest, or register as a user to:
- Browse the portfolio
- Submit a design request
- View your own orders
- Send messages and view your conversation history

**Admin access (for demonstration purposes):**
- Admin panel: [https://artea-studio-571c2301b41f.herokuapp.com/admin/](https://artea-studio-571c2301b41f.herokuapp.com/admin/)
- Username: `SuperAdmin`
- Password: `superadmin7654` *(or insert your actual demo credentials)*

**User access (for demonstration purposes):**
- User login: [https://artea-studio-571c2301b41f.herokuapp.com/accounts/login/](https://artea-studio-571c2301b41f.herokuapp.com/accounts/login/)
- Username: `Test`
- Password: `testkund7654` *(or insert your actual demo credentials)*

This site was deployed using **Heroku**, with static files managed via **WhiteNoise**, and media files hosted in development only.

---

## Known Limitations & Future Work
- Remaining long lines in some Python files (documented; style-fix ongoing)
- Specific tablet dropdown edge cases under review
- Facebook login mock not implemented
- More screenshots & testing matrices to be added over time
- Webhook enhancements to solidify paid status (if not already implemented)

---

## Credits
- **Code Institute – Boutique Ado Walkthrough** (structural inspiration)
- **Stripe Documentation** – payment integration guidance
- **Django Documentation** – sitemaps, email, security settings
- **All images & assets** – © Artea Studio
- Developed by **Thomas Eriksson (2025)**

---

## Deployment ???????????????????

### Local Deployment
```
bash
```

To get started you make a local copy of this project. You can clone it in your IDE Terminal, type the following command to clone my repository:

```
git clone https://github.com/creanorcode/project_5.git
cd project_5
```

After cloning the repository you will have to:

1. create and activate virtual environment:

```
python -m venv env
source env/bin/activate  # On Windows: venv\Script\activate
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Add a ```.env```file:

```
cp .env.example .env
---
# Django settings
SECRET_KEY=your-so-very-secret-key
DEBUG=True
ALLOWED_HOSTS=your-name.herokuapp.com, localhost,127.0.0.1:8000
DJANGO_SETTINGS_MODULE=project_5.settings
DATABASES=

# Stripe test keys
STRIPE_PUBLIC_KEY=stripe-public-key
STRIPE_SECRET_KEY=stripe-secret-key
STRIPE_WEBHOOK_SECRET_DOMAIN=for-your-custom-domain
STRIPE_WEBHOOK_SECRET_HEROKU=for-your-heroku-app

# AWS S3 
AWS_ACCESS_KEY_ID=access-key
AWS_S3_REGION_NAME=region-name
AWS_SECRET_ACCESS_KEY=secret-key
AWS_STORAGE_BUCKET_NAME=bucket-name
```

4. Run migrations and start server:

```
python manage.py migrate
python manage.py runserver

```

---