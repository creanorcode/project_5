# TESTING

This document records manual and validation testing for **Artea Studio** (Portfolio Project 5).

## Test Summary
All core user journeys were manually tested on both **local** and **deployed (Heroku)** environments:
- Account registration/login/logout
- Product browsing + cart + Stripe checkout
- Custom design order submission + file upload
- Completed design payment + download unlocking
- Contact form (DB save + email confirmation)
- Admin/staff workflows (orders, products, contact messages)
- SEO endpoints (`robots.txt`, `sitemap.xml`) and custom 404 page
- Navigation link integrity (no broken links)

---

## 1. How to Run Locally

### Repository
- Github: https://github.com/creanorcode/project_5.git

### Setup
  1. Clone:
    ``` bash
    git clone https://github.com/creanorcode/project_5.git
    cd project_5
    ```

  2. Create venv + install:
    ``` bash

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

  3. Create .env from .env.example and add required values (see DEPLOYMENT.md)

  4. Migrate + run:
    ``` bash
    python manage.py migrate
    python manage.py runserver
    ```

### Stripe Testing
Use Stripe test card:
- 4242 4242 4242 4242 (any future expiry, any CVC)

---

## 2. Test Environment

| Environment      | URL / Notes                                                          |
| ---------------- | -------------------------------------------------------------------- |
| Local            | [http://127.0.0.1:8000](http://127.0.0.1:8000)                       |
| Deployed         | [https://www.artea.studio](https://www.artea.studio)                 |
| Browsers         | Chrome (latest), Firefox (latest), Safari (latest), iOS Safari (14+) |
| Devices          | Desktop + iPad + iPhone (responsive checks)                          |

---

## 3. Manual Feature Tests (Core)

> Evidence screenshots are stored in `docs/screenshots/`.
> For each test: record expected vs actual outcome

### 3.1 Authentication

| Feature        | Steps                | Expected Result    | Actual Result      | Evidence     |
|----------------|----------------------|--------------------|--------------------|--------------|
| Register       | Open Register → submit valid form | Account created, redirect + success message | PASS | `register-success.png`   |
| Login          | Open Login → submit valid form | User logged in, navbar updates | PASS | `login-success.png` |
| Logout         | Click Logout | Session ends, navbar shows Login/Register | PASS | `logout-success.png`           |
| Auth restrictions | Visit protected pages while logged out | Redirect to login | PASS | `auth-protected-redirect.png` |

### 3.2 Products, Cart & Checkout

| Feature        | Steps           | Expected Result    | Actual Result | Evidence     |
| -------------- | --------------- | ------------------ | ------------- |--------------|
| Product list   | Open Products   | Product grids load | PASS          | `products-list.png` |
| Product detail | Open a product  | Title, image, price visible | PASS | `product-detail.png` |
| Add to cart    | Add product from detail | Item added, cart count/summary updates | PASS | `cart-added.png` |
| Update quantity | Increase/decrease qty | Totals update correctly | PASS | `cart-update.png` |
| Remove item    | Remove from cart | Cart item removed | PASS | `cart-remove.png` |
| Stripe checkout (shop) | Cart → checkout → pay with 4242 | Success page + order created + confirmation email | PASS | `stripe-shop-success.png` |

### 3.3 Custom Design Orders + Completed Design Payment

| Feature        | Steps           | Expected Result    | Actual Result      | Evidence     |
|----------------|-----------------|--------------------|--------------------|--------------|
| Design order submission | Fill Design Order + upload file → submit | Success message; object stored in DB | PASS | `design-order-submitting.png` |
| Staff upload completed design | Admin/staff uploads completed file | CompletedDesign available for user (locked until paid) | PASS | `completed-design-created.png` |
| Stripe payment (design) | Pay for completed design → 4242 | paid=True; download unlocked | PASS | `stripe-design-success.png` |
| Download gating | Visit My Designs (unpaid) | Download hidden/locked | PASS | `mydesigns-unpaid.png` |
| Download after payment | Visit My Designs (paid) | Download link visible | PASS | `mydesigns-paid.png` |

### 3.4 Contact Form & Messaging

| Feature        | Steps           | Expected Result    | Actual Result      | Evidence     |
|----------------|-----------------|--------------------|--------------------|--------------|
| Contact form submit | Submit name/email/message | Success message shown | PASS | `contact-success.png` |
| Contact saved  | Check Django admin → ContactMessage | Message stored in DB | PASS | `contact-admin-saved.png` |
| Email confirmation to user | Submit contact form | User receives confirmation email | PASS | `email-user-confirmation.png` |
| Email notification to admin | Submit contact form | Admin receives notification email | PASS | `email-admin-notification.png` |

### 3.5 Admin/Backend Smoke Tests

| Feature        | Steps           | Expected Result    | Actual Result      | Evidence     |
|----------------|-----------------|--------------------|--------------------|--------------|
| Admin login    | Login to /admin/ | Admin dashboard loads | PASS | `admin-login.png` |
| Products change view | Open a Product in admin | No server error; form renders | PASS | `admin-product-change.png` |
| Order change view | Open an Order in admin | No server error; inline item render | PASS | `admin-order-change.png` |
| ContactMessage change view | Open contact message | Admin reply field visible | PASS | `admin-contact-change.png` | 

---

## 4. Navigation & Broken Link Testing (LO1.15)
All visible navigation links were tested to ensure there was no broken links.

### 4.1 Anonymous user navigation

| Link         | URL                    | Expected   | Actual | Evidence              |
| ------------ | ---------------------- | ---------- | ------ | --------------------- |
| Home         | /                      | Loads page | PASS   | `nav-home.png`        |
| Portfolio    | /portfolio/            | Loads page | PASS   | `nav-portfolio.png`   |
| Products     | /products /            | Loads page | PASS   | `nav-products.png`    |
| Design Order | / orders/design-order/ | Loads page | PASS   | `nav-designorder.png` |
| Contact      | /contact/              | Loads page | PASS   | `nav-contact.png`     |
| Cart         | /cart/                 | Loads page | PASS   | `nav-cart.png`        |
| Newsletter   | /newsletter/           | Loads page | PASS   | `nav-newsletter.png`  |

### 4.2 Authenticated user navigation (My Account)

| Link             | Expected                    | Actual | Evidence                  |
| ---------------- | --------------------------- | ------ | ------------------------- |
| My Orders        | Loads order history         | PASS   | `nav-myorders.png`        |
| My Designs       | Loads design list           | PASS   | `nav-mydesigns.png`       |
| My Messages      | Loads contact messages list | PASS   | `nav-mymessages.png`      |
| My Conversations | Loads thread list           | PASS   | `nav-myconversations.png` |
| Logout           | Logs out                    | PASS   | `nav-logout.png`          |

---

## 5. Responsive / Cross-Device Checks

| Scenario                        | Mobile | Tablet | Desktop | Notes/Evidence            |
| ------------------------------- | ------ | ------ | ------- | ------------------------- |
| Navbar + dropdowns              | PASS   | PASS   | PASS    | `responsive-navbar.png`   |
| Product grid                    | PASS   | PASS   | PASS    | `responsive-products.png` |
| Forms (register/contact/design) | PASS   | PASS   | PASS    | `responsive-forms.png`    |
| Checkout flow                   | PASS   | PASS   | PASS    | `responsive-checkout.png` |

---

## 6. Validators & Code Quality (LO2.3)

### 6.1 HTML Validation
- W3C HTML Validator: PASS !!!!(no critical errors)
- Evidence: `validator-html.png`

### 6.3 CSS Validation
- W3C CSS Validator: PASS (no critical errors)
- Evidence: `validator-css.png`

### 6.3 Python Linting (Ruff)

- Command:
  ``` bash

  ruff check
  ```
  Result: PASS (no E/F-level issues)
  Evidence: `ruff-report.png`

### 6.4 Lighthouse

| Page     | Performance | Accessibility | Best Practices | SEO | Evidence                  |
| -------- | ----------- | ------------- | -------------- | --- | ------------------------- |
| Home     |             |               |                |     | `lighthouse-home.png`     |
| Products |             |               |                |     | `lighthouse-products.png` |
| Checkout |             |               |                |     | `lighthouse-checkout.png` |

---

## 7. SEO Evidence

| Endpoint/Meta                | Expected                              | Actual | Evidence               |
| ---------------------------- | ------------------------------------- | ------ | ---------------------- |
| /robots.txt                  | Accessible + includes sitemap         | PASS   | `robots.png`           |
| /sitemap.xml                 | Valid XML with URLs                   | PASS   | `sitemap.png`          |
| Meta description             | Present on key pages                  | PASS   | `meta-description.png` |
| External link rel attributes | noopener noreferrer for new-tab links | PASS   | `external-links.png`   |

---

## 8. Bugs & Fixes Log

| ID     | Issue                              | Fix                                                                | Status   |
| ------ | ---------------------------------- | ------------------------------------------------------------------ | -------- |
| BUG-01 | Admin 500 errors in Order/Products | Updated admin fields to match model + excluded non-aditable fields | Resolved |
| BUG-02 | Contact form 500 due to missing settings/SMTP | Added CONTACT_RECIPIENT_EMAIL + configured SMTP provider (Resend) | Resolved |

---

## 9. Regression Checklist (Post-fix)

- Register/login/logout still work: **PASS**
- Cart totals correct: **PASS**
- Stripe success/cancel behave as expected: **PASS**
- Design payment unlocks download: **PASS**
- Contact form saves + sends email: **PASS**
- Admin change views render correctly: **PASS**
- `robots.txt` and `sitemap.xml` respond correctly: **PASS**
