# Welcome to Artea Studio - Graghic Design Shop

[![mockup-arteastudio.png](https://i.postimg.cc/d13ZHVMg/mockup-arteastudio.png)](https://postimg.cc/8J8CsDzb)

## Overview
**Artea Studio** is a modern fullstack e-commerce platform for ordering custom graphic design. It offers a smooth way for customers to order, pay for, and receive custom graphic design services online.

**The platform is built with django and allows customers to:**
- Explore previous work (portfolio)
- Place custom orders via a form
- Pay securely through Stripe
- Access final design files via a logged-in dashboard

---

## Features

### Existing Features

- Fully responsive layout (mobile, tablet, desktop).
- Portfolio page with design examples.
- Order form with upload and notes.
- Stripe payment integration (test mode)
- User registration / login / logout.
- User dashboard with downloadable files.
- Admin panel for order and file management.
- Contact form (with email function).
- Newsletter signup (dummy).
- Custom 404 page, robots.txt and sitemap.xml.
- Role-based navigation (user, staff, superuser).

### Future Features

- 
- 
- 
- 
- 

---

## Full Features Walkthrough

Below is a step-by-step guide to every user flow and UI component in Artea Studio with screenshots from live site.

---

### 1. Landing page (Home)
---

## Design and UX

- **Artea Color Scheme**
  - Primary: '#2d89ef'
  - Secondary: '#f59e0b'
  - Accents: '#f9d342', '#dd4c4f', '#207f62'
- Heo section with CTA buttons
- Footer links rendered based on user role
- All form manually rendered based on user role
- Feedback via Django messages

---

## Technologies Used

| Components | Description |
|------------|-------------|
| Django     | Backend framework |
| SQLite     | Local database |
| Stripe     | Payment integration |
| Git/GitHub | Version control |
| HTML/CSS   | Frontend structure and styling |
| Heroku     | Deployment platform |

---

## Testing

- Manually tested:
  - Registration -> Order -> Stripe -> File delivery
  - Role-based access to admin panel and dashboard
  - Custom 404 page and error handling
  - Success messages and redirects
- Responsive across screen sizes
- Favicon visible in browser tab

---

## SEO & Extra Files

- **'robots.txt'** allows indexing of the entire site
- **'sitemap.xml'** includes home, protfolio, and contact pages
- **'404.html'** provides a user-friendly not found page
- **'/newsletter/'** includes a dummy subscription form (email only)

---

## Marketing Features

- Newsletter signup form available via '/newsletter/'
- Facebook page mockup provided (or see screenshot below)

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

## Getting Started Locally

```
bash
git clone https://github.com/YOUR-USERNAME/YOUR-PROJECT-NAME.git
cd YOUR-PROJECT-NAME
python -m venv env
source env/bin/activate

pip install -r requirements.txt

cp .env.example .env
python manage.py migrate
python manage.py runserver

```

---




```
pkill uptime.sh
rm .vscode/uptime.sh
```