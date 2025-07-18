# Welcome to Artea Studio - Graghic Design Shop

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

## Overview
**Artea Studio** is a modern fullstack e-commerce platform for ordering custom graphic design. It offers a smooth way for customers to order, pay for, and receive custom graphic design services online.

**The platform is built with django and allows customers to:**
- Explore previous work (portfolio)
- Place custom orders via a form
- Pay securely through Stripe
- Access final design files via a logged-in dashboard

---

## Key Features
 - User registration and secure login system
 - Fully responsive layout (desktop, tablet, mobile)
 - Interactive navigation menu with dropdowns
 - Browse and purchase digital products
 - Dynamic shopping cart with Stripe checkout integration
 - Submit design requests via custom form
 - Admin panel for managing orders and completed designs
 - Clients can pay and download completed designs
 - Built-in messaging system between users and admin
 - Styled alerts using Django messages framework
 - Clean visual layout with modern UI design

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

**My Account Menu**
[![screenshot-myaccount-menu.png](https://i.postimg.cc/HsgMZDS4/screenshot-myaccount-menu.png)](https://postimg.cc/z3x3vMYV)


#### My Designs

***My Design Page (unpaid design, not downloadble)**
[![screenshot-mydesigns-notpaid.png](https://i.postimg.cc/fRKngTpN/screenshot-mydesigns-notpaid.png)](https://postimg.cc/LJnbJRmC)

**My Design page (paid and downloadble)**
[![screenshot-mydesigns.png](https://i.postimg.cc/HLHRwDkh/screenshot-mydesigns.png)](https://postimg.cc/fV28sPXc)


#### My Orders

**My Orders (Order History)**
[![screenshot-myorders.png](https://i.postimg.cc/bw8fT26g/screenshot-myorders.png)](https://postimg.cc/rKhHyz2R)

**My Orders (Order Item)**
[![screenshot-orderitems.png](https://i.postimg.cc/Dy1KLccm/screenshot-orderitems.png)](https://postimg.cc/xcj7SMhS)


#### My Messages

The **"My Messages"** section provides a simple and organized view of internal system messages sent to the user. These messages may include admin replies to design orders, updates regarding payment status, or service notifications.

- **Location:** Accessible from the My Account dropdown in the top navigation bar.
- **Design:**
      - Messages are shown in message boxes with clear visual styling.
      - Each message is styled according to its type (e.g., info, warning, success).
- **Functionality:**
      - Users can view all received messages in reverse chronological order.
      - Messages may include admin replies, status updates, or system feedback after order events.

[![screenshot-My-Contact-Messages.png](https://i.postimg.cc/Kz6T9sG3/screenshot-My-Contact-Messages.png)](https://postimg.cc/gXKrjs6G)

[![screenshot-My-Contact-Message-Thread.png](https://i.postimg.cc/0QMm0qsq/screenshot-My-Contact-Message-Thread.png)](https://postimg.cc/zbNVq6vd)


#### My Conversations

The **"My Conversations"** section enables logged-in users to view and revisit message threads from submitted design orders or support-related inquiries.

- **Location:** *My Account* > *My Conversations*
- **Purpose:** Serves as a basic inbox/outbox for ongoing dialogues between the user and admin or designer.
- **Features:**
      - Displays a list of conversation threads.
      - Each thread shows:
            - The subject or context of the message
            - Time and date of the message
            - A button linking to the full conversation thread
- **Design:**
      - Each conversation is presented in a message card with clear headings and spacing.
      - Button: "View Conversation" leads to a detailed thread page.

- **Note:**
    - This feature is intended to simulate a real-world communication flow between clients and the service provider.
    - It enhances user experience by allowing reference to prior discussions or clarifications without using external email or messaging tools.

[![screenshot-My-Conversations.png](https://i.postimg.cc/SRcMH7RT/screenshot-My-Conversations.png)](https://postimg.cc/zHXvghnK)

[![screenshot-My-Conversations-Thread.png](https://i.postimg.cc/Y2FY4kR6/screenshot-My-Conversations-Thread.png)](https://postimg.cc/CdFzt3W5)
---

### Admin Panel (Staff/Superuser on backend)

Staff users can access the admin panel to manage site content:

- View and manage all design orders
- Respond to contact messages
- Access user conversations
- Moderate completed designs


[![screenshot-admin-backend.png](https://i.postimg.cc/44LYjXCp/screenshot-admin-backend.png)](https://postimg.cc/rz4yrXwp)


### Admin panel on frontend

Staff are able to manage designorders, mark them as paid and download them.

[![screenshot-adminpanel-frontend.png](https://i.postimg.cc/L5Y2cKfV/screenshot-adminpanel-frontend.png)](https://postimg.cc/dZYbCf57)

---

### Navigation and Responsiveness

The site navigation is fully responsive:

- **Hamburger menu** for mobile and tablet
- **Dropdown behavior** adapts for click on mobile and hover on desktop
- Layout scales smoothly for:
  - Mobile (portrait and landscape)
  - Tablets (including iPad)
  - Desktops and large screens


Screenshot on iPhone 14 Pro Max
[![screenshot-main-nav-i-Phone-14-pro-max.png](https://i.postimg.cc/W1LTy1nW/screenshot-main-nav-i-Phone-14-pro-max.png)](https://postimg.cc/Tp9zLGBg)

Screenshot on iPad pro
[![screenshot-main-Nav-ipad-pro.png](https://i.postimg.cc/hvt1cn1N/screenshot-main-Nav-ipad-pro.png)](https://postimg.cc/bD4t9KMR)

Landscape mode
[![screenshot-man-Nav-ipad-pro-landscape.png](https://i.postimg.cc/zv2SfQdv/screenshot-man-Nav-ipad-pro-landscape.png)](https://postimg.cc/BPD1Ymff)

---

### Login- and logout page

Login page
[![screenshot-login-Page.png](https://i.postimg.cc/Bbb7NHk8/screenshot-login-Page.png)](https://postimg.cc/QKLqd9Xs)

Logoutpage with links to login again and home
[![screenshot-logoutpage.png](https://i.postimg.cc/pVc6rc5K/screenshot-logoutpage.png)](https://postimg.cc/DmsgYggz)

---

### Register page

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

## Summary

The Artea Studio web application offers a complete custom design platform with:

- Seamless navigation
- Responsive layout across devices
- Integrated Stripe test checkout
- User login, order tracking, and secure messaging
- Admin control panel

Screenshots and walkthrough reflect the final version of the deployed project.

---

## About Artea – Vision & Market Position

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

## Deployment & Access

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


# Final Note

This project represents a major personal and technical milestone. While many key features are fully functional – including product browsing, custom design ordering, checkout with Stripe, user authentication, and admin tools – I recognize that the project is **not yet complete in every respect**.

Due to time constraints and unexpected technical challenges during the final 24 hours before submission, some elements are missing or partially implemented:

 - The README lacks full walkthrough sections and testing documentation with screenshots.

 - The code still contains flake8 warnings (e.g., long lines, formatting issues).

 - Some responsive styling and layout consistency (especially on tablets) could be improved.

 - A Facebook marketing mockup was not completed.

 - More detailed marketing and user strategy descriptions are planned but not included yet.

Despite this, I am proud of the core features implemented and the learning curve I have navigated. This submission reflects my genuine effort and commitment to building a real, working web product – and I look forward to refining it further beyond the deadline.

Thank you for reviewing my work.


## Completed and Functional Features

- **User registration and login system**
    - With error handling and secure password validation
    - Session-based login/logout

- **Responsive navigation menu**
    - Desktop: hover-based dropdown
    - Tablet and mobile: click-activated menu with dropdown behavior

- **Home page with dynamic call-to-action and product presentation**

- **Product catalog and individual product detail pages**

- **Shopping cart functionality**
    - Add/remove items
    - Quantity update
    - Total price calculation

- **Checkout with Stripe integration**
    - Stripe Checkout for product purchases
    - Secure payment flow with redirect to success/cancel pages

- **Design order form**
    - Users can submit requests for custom design with file upload

- **Completed designs**
    - Admin can mark as completed
    - Clients can pay for completed designs
    - Download unlocked after successful payment

- **Order history for users ("My Orders")**

- **Admin dashboard for design management**
    - List, filter by payment status, mark as paid

- **Messaging system between admin and users**
    - “My Messages” and “My Conversations” views available

- **Clean layout and styling with custom CSS**
    - Separate mobile, tablet, and desktop styling
    - Button styling, typography, layout containers, form elements

- **Django messages integration for user feedback**
    - Styled feedback for login/logout, form submission, errors, etc.

---