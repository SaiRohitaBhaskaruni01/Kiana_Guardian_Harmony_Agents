import pandas as pd
import random
import numpy as np

NUM_ROWS = 100
OUTPUT_FILE = "health_metrics.csv"

# Some sample names
first_names = ["Ava", "Liam", "Noah", "Emma", "Olivia", "Ethan", "Sophia", "Mia", "Isabella", "Lucas"]
last_names = ["Smith", "Johnson", "Lee", "Brown", "Garcia", "Martinez", "Davis", "Patel", "Lopez", "Taylor"]

def random_name():
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_row(emp_id):
    return {
        "employee_id": emp_id,
        "employee_name": random_name(),
        "date": pd.Timestamp("2025-01-01") + pd.Timedelta(days=random.randint(0, 60)),
        
        # Wearable metrics
        "heart_rate_bpm": random.randint(55, 110),        
        "steps": random.randint(1000, 15000),
        "calories_burned": random.randint(1500, 3500),
        "sleep_hours": round(random.uniform(4.0, 9.0), 1),
        "spo2_percent": random.randint(92, 100),
        "stress_level": random.randint(1, 10),
        "body_temperature_c": round(random.uniform(35.5, 37.8), 1),
    }

# Generate dataset
rows = [generate_row(emp_id=1000+i) for i in range(NUM_ROWS)]

df = pd.DataFrame(rows)

# Save
df.to_csv(OUTPUT_FILE, index=False)

print(f"Created {OUTPUT_FILE} with {NUM_ROWS} rows.")


print(df.head(8))