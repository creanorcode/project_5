# Welcome to Artea Studio - Graghic Design Shop

[![Artea-Mockup.png](https://i.postimg.cc/k5x9hK64/Artea-Mockup.png)](https://postimg.cc/t1CLs1zQ)

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

#### User Features
  - Browse featured and custom-made designs
  - Register, log in/out, and manage account
  - Place design request with file upload
  - Pay securely with Stripe
  - View order history and download completed work
  - Subscribe to newsletter (email mockup only)

#### Admin Features
  - Full admin panel via Django Admin
  - Manage users, orders, designs, and message
  - Mark designs as completed and notify users
  - Secure admin-only frontend dashboard

#### Payment Integration
  - Stripe checkout with success and cancel pages
  - Payment status stored per order
  - Download link only shown after successful payment

#### Responsive Design
  - Fully responsive meny for desktop, tablet and mobile
  - Dropdown "My Account" works across devices
  - Clean, accessible layout with focus on UX


### Future Features
- Product rating system and user reviews
- Enhanced messaging features (e.g. file attachments, message read status)
- PDF preview before download (for completed designs)
- Design templates categorized by topic
- AI-assisted design recommendations
- Admin notifications for new orders/messages
- Order status tracking (e.g. in progress, delivered)
- Download expiration or secure token system
- Export order history as CSV
- Dark mode toggle
- Mobile-first redesign of admin dashboard
- Integration with Instagram or Behance gallery

---

## Full Features Walkthrough

This walkthrough demonstrates all key pages, features, and interactions of the **Artea Studio** web application.

Every section includes a brief explanation of its purpose and functionality, along with placeholders for screenshots to visually support each part.

---

### Home Page

The homepage introduces the Artea Studio brand and its services. It is fully responsive and includes:

- A **hero section** with call-to-action buttons
- Welcome text and branding
- Links to important sections (Products, Portfolio, Contact)
- A featured section with highlighted works or offers

Screenshot placeholders:  
[![screenshot-hero.png](https://i.postimg.cc/B6H48yfM/screenshot-hero.png)](https://postimg.cc/njF6g3zD)
[![screenshot-footer.png](https://i.postimg.cc/cJVdLW2v/screenshot-footer.png)](https://postimg.cc/v1LJ0JQy)
---

### Portfolio Page

The portfolio showcases selected works by the designer.

- Responsive **image grid**
- Each portfolio item includes a title and description
- Optimized for both mobile and desktop viewing


[![screenshot-portfolio.png](https://i.postimg.cc/KzRQJS8D/screenshot-portfolio.png)](https://postimg.cc/ygCF8G9D)

---

### Products Page

The products page lists all available digital design items.

- Displayed as product cards with image, title, and price
- Clicking a card opens the detailed product page
- Accessible layout with responsive grid

Product grid page
[![screenshot-productpage.png](https://i.postimg.cc/gkNXkwDr/screenshot-productpage.png)](https://postimg.cc/KR3v08Cy)

product item page
[![screenshot-productitempage.png](https://i.postimg.cc/kgGVVn1s/screenshot-productitempage.png)](https://postimg.cc/mPxZJGG1)

---

### Design Order Page

This is a core feature where users can submit a custom design request.

- Clean and structured **form with multiple fields**
- Dropdowns, text inputs, and textarea
- Validated fields with clear feedback
- Uses Django backend to store design requests


[![screenshot-designform.png](https://i.postimg.cc/nzGVR5SM/screenshot-designform.png)](https://postimg.cc/XGX0X2b0)

---

### Cart Page

A cart system lets users review and adjust their selected items.

- Itemized list with prices and quantities
- Update/remove buttons per item
- Displays total cost
- Connects to Stripe (test mode)


[![screenshot-cart.png](https://i.postimg.cc/nV6jsbbf/screenshot-cart.png)](https://postimg.cc/F1Vsq6HT)

---

### Contact Page

Users can send messages directly to the designer.

- Name, email, and message fields
- Success/failure feedback through Django messages
- Submitted messages appear in user's dashboard


[![screenshot-contact.png](https://i.postimg.cc/6pBQRBMg/screenshot-contact.png)](https://postimg.cc/GHSrnnwx)

---

### My Account – Authenticated Users

Once logged in, users gain access to personal account features via the "My Account" dropdown:

- **My Orders**: View submitted orders
- **My Designs**: Access completed work
- **My Messages**: View replies from the designer
- **My Conversations**: Ongoing communication with the team
- Secure **logout button**
- Admin shortcut for staff

My Account Menu
[![screenshot-myaccount-menu.png](https://i.postimg.cc/HsgMZDS4/screenshot-myaccount-menu.png)](https://postimg.cc/z3x3vMYV)

My Design page

Order History page

---

### 🛠️ Admin Panel (Staff/Superuser)

Staff users can access the admin panel to manage site content:

- View and manage all design orders
- Respond to contact messages
- Access user conversations
- Moderate completed designs

📸  
![Admin view](path/to/admin-panel.png)

---

### 🌐 Navigation and Responsiveness

The site navigation is fully responsive:

- **Hamburger menu** for mobile and tablet
- **Dropdown behavior** adapts for click on mobile and hover on desktop
- Layout scales smoothly for:
  - Mobile (portrait and landscape)
  - Tablets (including iPad)
  - Desktops and large screens

📸  
![Mobile nav](path/to/mobile-nav.png)  
![Tablet view](path/to/ipad-view.png)

---

## 🔄 Example User Flow

1. User lands on homepage  
2. Clicks on "Products" to explore items  
3. Adds product to cart and proceeds to checkout  
4. Or fills out the Design Order form for a custom request  
5. Logs in to track "My Orders" and "My Designs"  
6. Uses "My Conversations" to message the designer  
7. Staff log in to manage requests via admin panel

---

## ✅ Summary

The Artea Studio web application offers a complete custom design platform with:

- Seamless navigation
- Responsive layout across devices
- Integrated Stripe test checkout
- User login, order tracking, and secure messaging
- Admin control panel

Screenshots and walkthrough reflect the final version of the deployed project.


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


### Tech Stack
  - Python 3.12
  - Django 5
  - HTML5, CSS3, JavaScript
  - PostgreSQL (in production)
  - Stripe API
  - Heroku (deployment)
  - Gunicorn, psycopg2, Whitenoise

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

## Deployment

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




```
pkill uptime.sh
rm .vscode/uptime.sh
```