# TESTING

This document summarizes manual and validator testing for **Artea Studio** (PP5).

## 1. How to Run Locally
- Repo: `<link to repo>`
- `.env` created from `.env.example`
- Commands:
  ```
  bash

  python manage.py migrate
  python manage.py runserver
  ```

- Test Stripe card: 4242 4242 4242 4242 (any future expiry, any CVC)

---

## 2. Test Environment

| Environment      | URL / Notes                                                          |
| ---------------- | -------------------------------------------------------------------- |
| Local            | [http://127.0.0.1:8000](http://127.0.0.1:8000)                       |
| Staging/Prod     | [https://www.artea.studio](https://www.artea.studio)                 |
| Browser versions | Chrome (latest), Firefox (latest), Safari (latest), iOS Safari (14+) |

---

## 3. Manual Feature Tests

> Fill out Expected vs Actual. Add screenshots in `docs/screenshots/`and reference them.

| Feature         | Steps                    | Expected                              | Actual | Evidence                                     |
| --------------- | ------------------------ | ------------------------------------- | ------ | -------------------------------------------- |
| Register        | Fill form → Submit       | Account created, redirect             |        | `docs/screenshots/register.png`              |
| Login/Logout    | Login → Logout           | Login succeeds; logout clears session |        |                                              |
| Product list    | Open /products/          | Grid renders, cards link to detail    |        |                                              |
| Product detail  | Open product page        | Title, image, price visible           |        |                                              |
| Cart            | Add item, update qty     | Totals update correctly               |        |                                              |
| Checkout (shop) | Pay with 4242 card       | `/payment/success/` + email           |        | `docs/screenshots/stripe-success-shop.png`   |
| Design order    | Submit form + file       | Confirmation UI, stored in DB         |        |                                              |
| Design payment  | Pay for completed design | Marked paid; download visible         |        | `docs/screenshots/stripe-success-design.png` |
| My Designs      | View list                | Paid show download, unpaid locked     |        |                                              |
| Contact form    | Submit message           | Success message shown                 |        |                                              |
| 404 page        | Visit missing URL        | Custom 404 shown                      |        |                                              |

---

## 4. Responsive / Cross-Browser Checks

| Scenario                        | Mobile | Tablet | Desktop | Notes |
| ------------------------------- | ------ | ------ | ------- | ----- |
| Navbar & dropdowns              |        |        |         |       |
| Hero & CTAs                     |        |        |         |       |
| Product grid                    |        |        |         |       |
| Forms (register/order/checkout) |        |        |         |       |
| My Account pages                |        |        |         |       |

---

## 5. Stripe Scenarios

| Scenario         | Steps                         | Expected                        | Actual | Evidence |
| ---------------- | ----------------------------- | ------------------------------- | ------ | -------- |
| Success (shop)   | Add product → checkout → 4242 | Redirect to success; email sent |        |          |
| Cancel           | Start checkout → cancel       | Redirect to cancel page         |        |          |
| Success (design) | Pay design → 4242             | `paid=True`; download allowed   |        |          |

---

## 6. Validators & Quality

### HTML/CSS
- W3C HTML Validator: `<result summary/link>`
- W3C CSS Validator: `<result summary/link>`

### Javascript (if applicable)
- ESLint / console errors: `<summary>`

### Python
- Ruff:
```
bash

ruff check . --fix
```

### Lighthouse (Home, Products, Checkout)
| Page     | Perf | Acc | Best Prac | SEO | Evidence |
| -------- | ---: | --: | --------: | --: | -------- |
| Home     |      |     |           |     |          |
| Products |      |     |           |     |          |
| Checkout |      |     |           |     |          |

---

## 7. Accessibility Quick Checks

| Check                       | Result | Notes |
| --------------------------- | ------ | ----- |
| Landmarks (`<main>`, nav)   |        |       |
| Alt text for images         |        |       |
| Color contrast              |        |       |
| Focus states & keyboard nav |        |       |
| Form labels & errors        |        |       |

---

## 8. SEO Evidence
| Endpoint/Meta                    | Expected                       | Actual | Evidence                       |
| -------------------------------- | ------------------------------ | ------ | ------------------------------ |
| `/robots.txt`                    | Allows indexing + sitemap link |        | `docs/screenshots/robots.png`  |
| `/sitemap.xml`                   | Valid XML with URLs            |        | `docs/screenshots/sitemap.png` |
| Meta description                 | Present on key pages           |        |                                |
| rel="noopener" on external links | Present                        |        |                                |
| Open Graph tags                  | Present on base                |        |                                |

---

## 9. Bugs & Fixes Log
| ID     | Description | Steps to Reproduce | Fix | Status        |
| ------ | ----------- | ------------------ | --- | ------------- |
| BUG-01 |             |                    |     | Resolved/Open |
| BUG-02 |             |                    |     |               |

---

## 10. Regression Checklist (Post-fix)
 - Register/login still work
 - Cart totals correct
 - Stripe success/cancel behave as expected
 - Design payment unlocks download
 - Admin pages render correctly
 - robots/sitemap respond correctly

---

## 11. Screenshots Index
List screenshots placed in docs/screenshots/:
- `stripe-success-shop.png`
- `stripe-success-design.png`
- `robots.png`
- `sitemap.png`
- `validator-html.png`
- `validator-css.png`
- `ruff-report.png`
- `lighthouse-home.png`, `lighthouse-products.png`, `lighthouse-checkout.png
