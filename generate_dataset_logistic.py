import pandas as pd
import random

rows = []

for _ in range(1000):
    speed = random.randint(40, 100)
    trips = random.randint(3, 35)
    time = random.randint(15, 100)

    # Base logic (risk increases with values)
    risk_score = (
        (speed / 100) * 0.4 +
        (trips / 35) * 0.3 +
        (time / 100) * 0.3
    )

    # Add noise (VERY IMPORTANT)
    noise = random.uniform(-0.15, 0.15)
    risk_score += noise

    # Convert to class
    risk = 1 if risk_score > 0.5 else 0

    rows.append([speed, trips, time, risk])

df = pd.DataFrame(rows, columns=["speed", "trips", "time", "risk"])

# Save CSV (choose separator based on your project)
df.to_csv("data/car_risk_data.csv", index=False, sep=";")

print("Dataset generated successfully (1000 rows)")