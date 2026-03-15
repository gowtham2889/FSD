from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'car-rental-secret-key-2024'

# ─── In-memory car catalogue ────────────────────────────────────────────────
CARS = [
    {
        "id": 1,
        "name": "Model S",
        "brand": "Tesla",
        "category": "Electric",
        "price": 9999,
        "seats": 5,
        "transmission": "Automatic",
        "fuel": "Electric",
        "rating": 4.9,
        "image": "tesla_model_s.png",
        "description": "Experience the future of driving with Tesla's flagship sedan. Blazing acceleration, cutting-edge autopilot, and zero emissions make every journey extraordinary.",
        "features": ["Autopilot", "Premium Sound", "Glass Roof", "Wireless Charging", "360° Camera"]
    },
    {
        "id": 2,
        "name": "M4 Competition",
        "brand": "BMW",
        "category": "Sports",
        "price": 12500,
        "seats": 4,
        "transmission": "Automatic",
        "fuel": "Petrol",
        "rating": 4.8,
        "image": "bmw_m4.png",
        "description": "The ultimate driving machine. Twin-turbo inline-six power, rear-wheel drive precision, and an interior that blends luxury with motorsport DNA.",
        "features": ["M Sport Exhaust", "Carbon Roof", "Head-Up Display", "Harman Kardon", "Adaptive Suspension"]
    },
    {
        "id": 3,
        "name": "G-Class AMG",
        "brand": "Mercedes",
        "category": "SUV",
        "price": 16500,
        "seats": 5,
        "transmission": "Automatic",
        "fuel": "Petrol",
        "rating": 4.9,
        "image": "mercedes_g.png",
        "description": "Iconic, unstoppable, and unapologetically luxurious. Command the road in one of the most recognizable vehicles ever built.",
        "features": ["AMG V8 Biturbo", "Leather Interior", "Off-Road Package", "Burmester Sound", "Heated Seats"]
    },
    {
        "id": 4,
        "name": "911 Carrera",
        "brand": "Porsche",
        "category": "Sports",
        "price": 14999,
        "seats": 2,
        "transmission": "Manual",
        "fuel": "Petrol",
        "rating": 4.9,
        "image": "porsche_911.png",
        "description": "Legendary performance meets timeless design. The 911 delivers an unmatched driving experience that has defined the sports car for over 60 years.",
        "features": ["Sport Chrono", "PASM Suspension", "Bose Sound", "Sport Exhaust", "Rear-Axle Steering"]
    },
    {
        "id": 5,
        "name": "Range Rover Sport",
        "brand": "Land Rover",
        "category": "SUV",
        "price": 13500,
        "seats": 5,
        "transmission": "Automatic",
        "fuel": "Diesel",
        "rating": 4.7,
        "image": "range_rover.png",
        "description": "Effortless refinement meets unstoppable capability. From city boulevards to rugged trails, the Range Rover Sport conquers every terrain in absolute comfort.",
        "features": ["Terrain Response", "Meridian Sound", "Panoramic Roof", "Air Suspension", "Pixel LED Lights"]
    },
    {
        "id": 6,
        "name": "A5 Sportback",
        "brand": "Audi",
        "category": "Sedan",
        "price": 7999,
        "seats": 5,
        "transmission": "Automatic",
        "fuel": "Petrol",
        "rating": 4.6,
        "image": "audi_a5.png",
        "description": "Where elegance meets efficiency. The A5 Sportback combines coupe-like styling with quattro all-wheel drive and a beautifully crafted interior.",
        "features": ["Quattro AWD", "Virtual Cockpit", "Matrix LED", "Bang & Olufsen", "Park Assist"]
    },
    {
        "id": 7,
        "name": "Mustang GT",
        "brand": "Ford",
        "category": "Sports",
        "price": 8999,
        "seats": 4,
        "transmission": "Manual",
        "fuel": "Petrol",
        "rating": 4.7,
        "image": "ford_mustang.png",
        "description": "Raw American muscle with a modern edge. The 5.0L V8 roar, aggressive styling, and exhilarating performance create pure automotive passion.",
        "features": ["5.0L V8 Engine", "Launch Control", "MagneRide Damping", "B&O Sound", "Track Apps"]
    },
    {
        "id": 8,
        "name": "Camry Hybrid",
        "brand": "Toyota",
        "category": "Sedan",
        "price": 4999,
        "seats": 5,
        "transmission": "Automatic",
        "fuel": "Hybrid",
        "rating": 4.5,
        "image": "toyota_camry.png",
        "description": "Reliability redefined. The Camry Hybrid delivers exceptional fuel economy without compromising on comfort, safety, or style.",
        "features": ["Hybrid Synergy", "Toyota Safety Sense", "JBL Audio", "Wireless CarPlay", "Adaptive Cruise"]
    },
    {
        "id": 9,
        "name": "Model Y",
        "brand": "Tesla",
        "category": "Electric",
        "price": 8499,
        "seats": 7,
        "transmission": "Automatic",
        "fuel": "Electric",
        "rating": 4.8,
        "image": "tesla_model_y.png",
        "description": "The versatile electric SUV that seats up to seven. Incredible range, expansive cargo space, and Tesla's renowned technology ecosystem.",
        "features": ["Full Self-Driving", "15\" Touchscreen", "HEPA Filter", "Camp Mode", "Third Row Seats"]
    },
]

# ─── In-memory bookings store ───────────────────────────────────────────────
bookings = []


def get_car(car_id):
    """Look up a car by its integer id."""
    return next((c for c in CARS if c["id"] == car_id), None)


# ─── Routes ─────────────────────────────────────────────────────────────────
@app.route("/")
def home():
    featured = CARS[:3]
    return render_template("index.html", featured_cars=featured)


@app.route("/cars")
def cars():
    category = request.args.get("category", "all")
    if category and category != "all":
        filtered = [c for c in CARS if c["category"].lower() == category.lower()]
    else:
        filtered = CARS
    categories = sorted(set(c["category"] for c in CARS))
    return render_template("cars.html", cars=filtered, categories=categories, selected=category)


@app.route("/cars/<int:car_id>")
def car_detail(car_id):
    car = get_car(car_id)
    if car is None:
        return redirect(url_for("cars"))
    return render_template("car_detail.html", car=car)


@app.route("/booking/<int:car_id>", methods=["GET", "POST"])
def booking(car_id):
    car = get_car(car_id)
    if car is None:
        return redirect(url_for("cars"))

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        pickup = request.form.get("pickup_date", "").strip()
        returnd = request.form.get("return_date", "").strip()
        location = request.form.get("location", "").strip()

        # Basic validation
        if not all([name, email, phone, pickup, returnd, location]):
            flash("Please fill in all fields.", "error")
            return render_template("booking.html", car=car)

        try:
            pickup_dt = datetime.strptime(pickup, "%Y-%m-%d")
            return_dt = datetime.strptime(returnd, "%Y-%m-%d")
            if return_dt <= pickup_dt:
                flash("Return date must be after the pickup date.", "error")
                return render_template("booking.html", car=car)
            days = (return_dt - pickup_dt).days
        except ValueError:
            flash("Invalid date format.", "error")
            return render_template("booking.html", car=car)

        total = days * car["price"]
        booking_info = {
            "id": len(bookings) + 1,
            "car": car,
            "name": name,
            "email": email,
            "phone": phone,
            "pickup": pickup,
            "return": returnd,
            "location": location,
            "days": days,
            "total": total,
            "status": "confirmed",
        }
        bookings.append(booking_info)
        return render_template("booking_confirmation.html", booking=booking_info)

    return render_template("booking.html", car=car)


@app.route("/my-bookings")
def my_bookings():
    return render_template("my_bookings.html", bookings=bookings)


@app.route("/cancel-booking/<int:booking_id>", methods=["GET", "POST"])
def cancel_booking(booking_id):
    booking = next((b for b in bookings if b["id"] == booking_id), None)
    if booking and booking.get("status") == "confirmed":
        booking["status"] = "cancelled"
        flash(f"Booking #{booking_id} for {booking['car']['brand']} {booking['car']['name']} has been cancelled.", "success")
    elif booking:
        flash("This booking is already cancelled.", "error")
    else:
        flash("Booking not found.", "error")
    return redirect(url_for("my_bookings"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thank you for your message! We'll get back to you soon.", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
