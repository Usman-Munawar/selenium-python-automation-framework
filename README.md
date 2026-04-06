# Selenium Python Automation Framework

## 📌 Project Overview

This project is a UI automation framework built using **Python, Selenium, and Pytest**.
It automates key user flows of the SauceDemo application, including login, cart, checkout, and logout functionalities.

The framework follows the **Page Object Model (POM)** design pattern to ensure maintainability, scalability, and clean code structure.

---

## 🛠 Tech Stack

* Python 3.12.1
* Selenium WebDriver
* Pytest
* WebDriver Manager

---

## 📁 Project Structure

```
saucedemo-selenium-python/
│
├── config/
│   └── config.json              # Test data (URL, credentials)
│
├── pages/                       # Page Object Model classes
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── checkout_overview_page.py
│   └── checkout_complete_page.py
│
├── tests/                       # Test cases
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_logout.py
│
├── utils/                       # Utility classes
│   ├── driver_factory.py
│   └── config_reader.py
│
├── conftest.py                  # Pytest fixtures (driver setup/teardown)
├── requirements.txt             # Dependencies
├── .gitignore
└── README.md
```

---

## ✅ Test Scenarios Covered

### 🔐 Login

* Valid login
* Invalid login

### 🛒 Cart

* Add product to cart
* Verify cart items

### 💳 Checkout

* Successful checkout
* Validation checks:

  * Missing first name
  * Missing last name
  * Missing postal code

### 🚪 Logout

* Successful logout and redirection to login page

---

## ▶️ How to Run Tests

### 1. Clone the repository

```
git clone https://github.com/Usman-Munawar/selenium-python-automation-framework.git
cd selenium-python-automation-framework
```

### 2. Create virtual environment

```
python -m venv .venv
```

### 3. Activate environment

**Windows:**

```
.venv\Scripts\activate
```

**Mac/Linux:**

```
source .venv/bin/activate
```

### 4. Install dependencies

```
pip install -r requirements.txt
```

### 5. Run tests

```
pytest -v
```

---

## 🧠 Key Concepts Used

* Page Object Model (POM)
* Pytest Fixtures (`conftest.py`)
* Explicit Waits (WebDriverWait)
* Config-driven testing (JSON)
* Modular and scalable test design

---

## 🚀 Future Improvements

* Add pytest parameterization
* Generate HTML reports
* Capture screenshots on test failure
* Integrate with CI/CD (GitHub Actions)

---

## 👨‍💻 Author

**Usman Munawar**

---

## ⭐ Notes

This project is created as part of learning and building a portfolio for automation testing roles.
