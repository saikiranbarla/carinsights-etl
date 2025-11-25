# generate_3months_data.py
# Generates sample car sales CSVs for 3 months.
# Requires: pip install faker pandas

import os
import csv
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker()
FOLDER = "sample_data"  # output folder

# configuration: 90 days back from today
start_date = datetime.now().date() - timedelta(days=90)
days = 90

car_models = [
    ("Honda Civic", "Civic-2023"),
    ("Toyota Corolla", "Corolla-2024"),
    ("Hyundai Creta", "Creta-2024"),
    ("Maruti Swift", "Swift-2023"),
    ("Kia Seltos", "Seltos-2023"),
    ("MG Hector", "Hector-2024")
]

os.makedirs(FOLDER, exist_ok=True)

def generate_row(sale_date):
    car_name, car_model = random.choice(car_models)
    owner_name = fake.name()
    phone = fake.phone_number()
    address = fake.address().replace("\n", ", ")
    cost = round(random.uniform(500000, 3000000), 2)  # INR
    return {
        "id": fake.uuid4(),
        "carname": car_name,
        "owner_name": owner_name,
        "owner_phone": ''.join(filter(str.isdigit, phone))[:10],
        "address": address,
        "cost": cost,
        "date_of_purchase": sale_date.isoformat(),
        "car_model": car_model
    }

# Create one CSV per day with random rows (10-50 rows/day)
for i in range(days):
    day = start_date + timedelta(days=i)
    day_folder = os.path.join(FOLDER, day.strftime("%Y-%m"))
    os.makedirs(day_folder, exist_ok=True)
    filename = os.path.join(day_folder, f"sales_{day.isoformat()}.csv")

    rows_count = random.randint(10, 50)
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id","carname","owner_name","owner_phone","address","cost","date_of_purchase","car_model"])
        writer.writeheader()
        for _ in range(rows_count):
            writer.writerow(generate_row(day))

    print(f"Wrote {rows_count} rows to {filename}")
