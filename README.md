# 🚗 SuperCars — Premium Car Rental Website

A full-stack car rental web application built with **Flask**, **HTML**, **CSS**, and **JavaScript**. Features a premium dark/light theme, real car photos, booking system with cancellation, and responsive design.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-green?logo=flask)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🏎️ **Car Catalog** | 9 premium cars (Sports, Electric, SUV, Sedan) with real photos |
| 🔍 **Search & Filter** | Filter by category, search by name |
| 📅 **Booking System** | Full booking flow with date selection & price calculation |
| ❌ **Cancel Booking** | Cancel reservations from the My Bookings page |
| 🌙 **Dark/Light Mode** | Toggle theme with localStorage persistence |
| 💰 **₹ Pricing** | All prices in Indian Rupees with comma formatting |
| 📱 **Responsive** | Mobile-first design, works on all screen sizes |
| ⚡ **Animations** | Scroll-reveal effects, hover transitions, micro-animations |

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Fonts:** Google Fonts (Outfit)
- **Icons:** Font Awesome 6.5

---

## 📁 Project Structure

```
FSD_PRO/
├── app.py                  # Flask application & routes
├── requirements.txt        # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css       # Complete design system & styles
│   ├── js/
│   │   └── main.js         # Theme toggle, animations, forms
│   └── images/             # Car photos (9 images)
└── templates/
    ├── base.html            # Base layout (navbar, footer)
    ├── index.html           # Homepage
    ├── cars.html            # Car catalog with filters
    ├── car_detail.html      # Individual car details
    ├── booking.html         # Booking form
    ├── booking_confirmation.html
    ├── my_bookings.html     # View & cancel bookings
    ├── about.html           # About page
    └── contact.html         # Contact page
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed

### Installation

```bash
# Clone the repository
git clone https://github.com/gowtham2889/FSD.git
cd FSD

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

---

## 📸 Pages

| Page | Route | Description |
|------|-------|-------------|
| Home | `/` | Hero section, featured cars, testimonials |
| Cars | `/cars` | Full fleet with category filters & search |
| Car Detail | `/cars/<id>` | Specifications, features & booking CTA |
| Booking | `/booking/<id>` | Form with live price estimation |
| My Bookings | `/my-bookings` | View all bookings, cancel if needed |
| About | `/about` | Company story, stats, team values |
| Contact | `/contact` | Contact form & info cards |

---

## 🎨 Color Theme

| Mode | Background | Accent | Secondary |
|------|-----------|--------|-----------|
| 🌙 Dark | Deep Navy `#0c1222` | Amber `#e8973e` | Teal `#2da4b8` |
| ☀️ Light | Warm Gray `#f8f9fb` | Amber `#e8973e` | Teal `#2da4b8` |

---

## 🚘 Available Cars

| Car | Category | Price/Day |
|-----|----------|-----------|
| Toyota Camry Hybrid | Sedan | ₹4,999 |
| Audi A5 Sportback | Sedan | ₹7,999 |
| Tesla Model Y | Electric | ₹8,499 |
| Ford Mustang GT | Sports | ₹8,999 |
| Tesla Model S | Electric | ₹9,999 |
| BMW M4 Competition | Sports | ₹12,500 |
| Range Rover Sport | SUV | ₹13,500 |
| Porsche 911 Carrera | Sports | ₹14,999 |
| Mercedes G-Class AMG | SUV | ₹16,500 |

---

## 👨‍💻 Author

**Gowtham Reddy Pakkiru**

- GitHub: [@gowtham2889](https://github.com/gowtham2889)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
