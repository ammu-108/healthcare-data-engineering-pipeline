import pandas as pd
import numpy as np
from pathlib import Path

# Make the generated data reproducible
np.random.seed(42)

# -----------------------------
# 1. Generate Providers
# -----------------------------

regions = ["NORTH", "SOUTH", "EAST", "WEST", "CENTRAL"]

specialties = [
    "Cardiology",
    "Dermatology",
    "Pediatrics",
    "Orthopedics",
    "Neurology"
]

provider_types = [
    "Clinic",
    "Hospital",
    "Specialty Center"
]

providers = []

for i in range(1, 31):
    providers.append({
        "provider_id": f"PRV{i:03d}",
        "provider_name": f"Provider_{i:03d}",
        "specialty": np.random.choice(specialties),
        "region": np.random.choice(regions),
        "provider_type": np.random.choice(provider_types)
    })

providers_df = pd.DataFrame(providers)


# -----------------------------
# 2. Generate Members
# -----------------------------

genders = ["F", "M"]

plans = [
    "Basic",
    "Standard",
    "Premium"
]

members = []

for i in range(1, 101):
    members.append({
        "member_id": f"MEM{i:04d}",
        "gender": np.random.choice(genders),
        "date_of_birth": pd.Timestamp(
            np.random.randint(
                pd.Timestamp("1960-01-01").value // 10**9,
                pd.Timestamp("2005-12-31").value // 10**9
            ),
            unit="s"
        ).date(),
        "region": np.random.choice(regions),
        "insurance_plan": np.random.choice(plans)
    })

members_df = pd.DataFrame(members)


# -----------------------------
# 3. Generate Claims
# -----------------------------

diagnosis_codes = [
    "D001",
    "D002",
    "D003",
    "D004",
    "D005"
]

procedure_codes = [
    "P101",
    "P102",
    "P103",
    "P104",
    "P105"
]

claim_statuses = [
    "Approved",
    "Rejected",
    "Pending"
]

claims = []

for i in range(1, 301):
    claims.append({
        "claim_id": f"CLM{i:05d}",
        "member_id": np.random.choice(members_df["member_id"]),
        "provider_id": np.random.choice(providers_df["provider_id"]),
        "claim_date": pd.Timestamp(
            "2026-01-01"
        ) + pd.Timedelta(days=np.random.randint(0, 270)),
        "diagnosis_code": np.random.choice(diagnosis_codes),
        "procedure_code": np.random.choice(procedure_codes),
        "claim_amount": round(np.random.uniform(100, 10000), 2),
        "claim_status": np.random.choice(claim_statuses)
    })

claims_df = pd.DataFrame(claims)


# -----------------------------
# 4. Introduce Data Quality Issues
# -----------------------------

# Duplicate claim
claims_df.loc[1, "claim_id"] = claims_df.loc[0, "claim_id"]

# Invalid claim amount
claims_df.loc[10, "claim_amount"] = -500

# Missing provider
claims_df.loc[20, "provider_id"] = None

# Invalid member reference
claims_df.loc[30, "member_id"] = "MEM9999"

# Missing claim status
claims_df.loc[40, "claim_status"] = None

# Inconsistent region value
members_df.loc[5, "region"] = "North"


# -----------------------------
# 5. Save CSV files
# -----------------------------

output_dir = Path("/tmp/healthcare_project_raw")
output_dir.mkdir(parents=True, exist_ok=True)

providers_df.to_csv(output_dir / "providers.csv", index=False)
members_df.to_csv(output_dir / "members.csv", index=False)
claims_df.to_csv(output_dir / "claims.csv", index=False)

print("Data generation completed.")
print(f"Providers: {len(providers_df)}")
print(f"Members: {len(members_df)}")
print(f"Claims: {len(claims_df)}")
print(f"Files created in: {output_dir}")