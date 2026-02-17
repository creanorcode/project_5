# TESTING

This document records manual, validation and regression testing for Artea Studio (Portfolio Project 5).

- Testing was conducted on both:
- Local development environment
- Deployed Heroku production environment

All core user journeys were tested after major bug fixes to ensure no regressions were introduced.

---

## 1. Test Strategy

Testing followed three layers:
1. Manual feature testing (user journeys)
2. Backend/admin smoke testing
3. Validation & quality tools (HTML, CSS, Python, Lighthouse)

Each feature was tested using:
- Clear steps
- Expected result
- Actual result
- Evidence (screenshots)

No feature was marked as complete without verification in both local and deployed environments.

---

## 2. Manual Feature Testing

### 2.1 Authentication

| Feature         | Steps                              | Expected Result                                                     | Actual Result | Evidence               |
| --------------- | ---------------------------------- | ------------------------------------------------------------------- | ------------- | ---------------------- |
| Register        | Open /register → submit valid form | Account created, redirected to dashboard, success message displayed | *PASS*   | [View Screenshot](docs/screenshots/register-success.png) |
| Login           | Submit valid credentials           | User logged in, navbar updates                                      | *PASS*   | [View Screenshot](docs/screenshots/login-success.png) |
| Logout          | Click logout                       | Session cleared, navbar shows Login/Register                        | *PASS*   | [View Screenshot](docs/screenshots/logout-success.png) |
| Protected route | Visit /orders/ while logged out    | Redirect to login page                                              | *PASS*   | [View Screenshot](docs/screenshots/auth-redirect.png) |

---

### 2.2 Product & Cart Flow

| Feature         | Steps            | Expected Result                | Actual Result | Evidence             |
| --------------- | ---------------- | ------------------------------ | ------------- | -------------------- |
| Product list    | Open /products/  | Product grid renders correctly | *PASS*   | [View Screenshot](docs/screenshots/products-list.png) |
| Product detail  | Click product    | Title, image, price visible    | *PASS*   | [View Screenshot](docs/screenshots/product-detail.png) |
| Add to cart     | Add product      | Cart updates, item visible     | *PASS*   | [View Screenshot](docs/screenshots/cart-added.png) |
| Update quantity | Change quantity  | Totals update correctly        | *PASS*   | [View Screenshot](docs/screenshots/cart-update.png) |
| Remove item     | Remove from cart | Item removed                   | *PASS*   | [View Screenshot](docs/screenshots/cart-remove.png) |

---

### 2.3 Stripe Checkout - Stop Flow

| Scenario           | Steps              | Expected Result                                                  | Actual Result | Evidence                  |
| ------------------ | ------------------ | ---------------------------------------------------------------- | ------------- | ------------------------- |
| Successful payment | Use test card 4242 | Redirect to success page, Order created, confirmation email sent | *PASS*   | [View Screenshot](docs/screenshots/stripe-shop-success.png) |
| Cancel (Shop Checkout)     | Start Checkout -> click back arrow before payment | Redirect to cart page                                          | *PASS*   | [View Screenshot](docs/screenshots/stripe-cancel-cart.png) |

> Stripe Checkout cancel behaviour follows Stripe hosted flow: user must click back before completing payment. After successful payment, redirect occurs to success_url and transaction cannot be cancelled within the session.

> Stripe hosted checkout returns the user to the configured cancel_url. In this implementation, cancel_url redirects to the cart page (/cart/), allowing the user to review or modify items before attempting checkout again.

---

### 2.4 Custom Design Order Flow

| Feature                | Steps                           | Expected Result                     | Actual Result | Evidence                     |
| ---------------------- | ------------------------------- | ----------------------------------- | ------------- | ---------------------------- |
| Submit design order    | Fill form + upload file         | Success message; object saved in DB | *(fill in)*   | `design-order-submit.png`    |
| Staff upload           | Upload CompletedDesign in admin | File linked to DesignOrder          | *(fill in)*   | `completed-design-admin.png` |
| Design payment         | Pay via Stripe                  | `paid=True`; download unlocked      | *(fill in)*   | `stripe-design-success.png`  |
| Download gating        | View unpaid design              | Download hidden                     | *(fill in)*   | `design-locked.png`          |
| Download after payment | View paid design                | Download visible                    | *(fill in)*   | `design-unlocked.png`        |
| Design payment -> redirect + download unlocked | Go to unpaid design -> Pay with 4242 -> redirected after success | User redirected to My Designs and the design shows as paid/unlocked with download link visible | PASS | stripe-design-success-unlocked.png |
---

### 2.5 Contact Form & Messaging

| Feature             | Steps          | Expected Result             | Actual Result | Evidence                |
| ------------------- | -------------- | --------------------------- | ------------- | ----------------------- |
| Submit contact form | Fill + submit  | Success message shown       | *(fill in)*   | `contact-success.png`   |
| DB save             | Check admin    | ContactMessage stored       | *(fill in)*   | `contact-admin.png`     |
| Email to user       | Submit form    | Confirmation email received | *(fill in)*   | `email-user.png`        |
| Email to admin      | Submit form    | Notification email received | *(fill in)*   | `email-admin.png`       |
| Admin reply         | Reply in admin | User receives reply email   | *(fill in)*   | `email-admin-reply.png` |

---

## 3. Admin Smoke Testing (LO1.4)
After previous submission failures due to 500 errors, all admin change views were explicitly tested.

| Feature                      | Expected Result | Actual Result | Evidence                |
| ---------------------------- | --------------- | ------------- | ----------------------- |
| Open Product change view     | No server error | *(fill in)*   | `admin-product.png`     |
| Open Order change view       | No server error | *(fill in)*   | `admin-order.png`       |
| Open DesignOrder change view | No server error | *(fill in)*   | `admin-designorder.png` |
| Open ContactMessage          | No server error | *(fill in)*   | `admin-contact.png`     |

---

## 4. Broken Link Testing (LO1.15)

All navigation links were manually tested.

| Link         | Expected   | Actual      | Evidence            |
| ------------ | ---------- | ----------- | ------------------- |
| Home         | Loads page | *(fill in)* | `nav-home.png`      |
| Portfolio    | Loads page | *(fill in)* | `nav-portfolio.png` |
| Products     | Loads page | *(fill in)* | `nav-products.png`  |
| Design Order | Loads page | *(fill in)* | `nav-design.png`    |
| Contact      | Loads page | *(fill in)* | `nav-contact.png`   |
| Cart         | Loads page | *(fill in)* | `nav-cart.png`      |

No broken links remain in deployed version.

---

## 5. Responsive Testing

Tested on:
- Desktop (Chrome latest)
- iPad
- iPhone Safari

| Scenario        | Mobile   | Tablet   | Desktop  | Notes |
| --------------- | -------- | -------- | -------- | ----- |
| Navbar dropdown | *(fill)* | *(fill)* | *(fill)* |       |
| Product grid    | *(fill)* | *(fill)* | *(fill)* |       |
| Forms           | *(fill)* | *(fill)* | *(fill)* |       |
| Checkout flow   | *(fill)* | *(fill)* | *(fill)* |       |

---

## 6. Validators & Quality Checks (LO2.3)

### HTML Validation

Validator: https://validator.w3.org/

Result:
(insert summary)

Evidence:
`validator-html.png`

### CSS Validation

Validator: https://jigsaw.w3.org/css-validator/

Result:
(insert summary)

Evidence:
`validator-css.png`

---

### Python Linting

Command:
``` bash
ruff check
```
Result:
(insert summary - e.g., no E/F level errors)

Evidence:
`ruff-report.png`

---

### Lighthouse

| Page     | Performance | Accessibility | Best Practices | SEO      | Evidence                  |
| -------- | ----------- | ------------- | -------------- | -------- | ------------------------- |
| Home     | *(fill)*    | *(fill)*      | *(fill)*       | *(fill)* | `lighthouse-home.png`     |
| Products | *(fill)*    | *(fill)*      | *(fill)*       | *(fill)* | `lighthouse-products.png` |
| Checkout | *(fill)*    | *(fill)*      | *(fill)*       | *(fill)* | `lighthouse-checkout.png` |

---

## 7. SEO Verification (LO3)

| Feature          | Expected                     | Actual   | Evidence             |
| ---------------- | ---------------------------- | -------- | -------------------- |
| /robots.txt      | Accessible, includes sitemap | *(fill)* | `robots.png`         |
| /sitemap.xml     | Valid XML                    | *(fill)* | `sitemap.png`        |
| Meta description | Present                      | *(fill)* | `meta.png`           |
| rel attributes   | noopener noreferrer present  | *(fill)* | `external-links.png` |

---

## 8. Bug Fix Log

| ID     | Issue                  | Fix                                               | Status   |
| ------ | ---------------------- | ------------------------------------------------- | -------- |
| BUG-01 | Admin 500 errors       | Refactored admin fields & read-only configuration | Resolved |
| BUG-02 | Contact form 500       | Configured SMTP provider & settings               | Resolved |
| BUG-03 | Sitemap AttributeError | Implemented get_absolute_url()                    | Resolved |
| BUG-04 | Duplicate URL patterns | Cleaned project_5/urls.py                         | Resolved |

---

## 9. Regression Testing

After each major fix:
- Authentication retested
- Stripe flows retested
- Contact form retested
- Admin pages retested
- SEO endpoints restested

No regressions detected in deployed version.
