import pandas as pd
import random

random.seed(42)  # reproducibility

rows = []

for _ in range(1000):
    overspeeding = random.randint(0, 1)
    night = random.randint(0, 1)
    phone = random.randint(0, 1)
    braking = random.randint(0, 1)

    # Risk logic (VERY IMPORTANT)
    risk_score = (
        overspeeding * 0.35 +
        night * 0.20 +
        phone * 0.25 +
        braking * 0.20
    )

    # Add noise to avoid perfect model
    noise = random.uniform(-0.15, 0.15)
    risk_score += noise

    risk = 1 if risk_score > 0.5 else 0

    rows.append([
        overspeeding,
        night,
        phone,
        braking,
        risk
    ])

df = pd.DataFrame(rows, columns=[
    "overspeeding",
    "night",
    "phone",
    "braking",
    "risk"
])

df.to_csv("data/driver_behavior.csv", index=False)

print("Bernoulli dataset generated (1000 rows)")