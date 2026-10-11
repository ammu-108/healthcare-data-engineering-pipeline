import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(100)

output_dir = Path("/Workspace/Users/durga20010615@gmail.com/healthcare-data-engineering-pipeline/data/incoming")
output_dir.mkdir(parents=True, exist_ok=True)



# Generate 20 new claims
claims = []

for i in range(301, 321):
    claims.append({
        "claim_id": f"CLM{i:05d}",
        "member_id": f"MEM{np.random.randint(1, 101):04d}",
        "provider_id": f"PRV{np.random.randint(1, 31):03d}",
        "claim_date": pd.Timestamp("2026-10-01")
            + pd.Timedelta(days=np.random.randint(0, 10)),
        "diagnosis_code": np.random.choice(
            ["D001", "D002", "D003", "D004", "D005"]
        ),
        "procedure_code": np.random.choice(
            ["P101", "P102", "P103", "P104", "P105"]
        ),
        "claim_amount": round(np.random.uniform(100, 10000), 2),
        "claim_status": np.random.choice(
            ["Approved", "Rejected", "Pending"]
        )
    })

claims_df = pd.DataFrame(claims)

claims_df.to_csv(output_dir / "claims_batch_001.csv", index=False)

print(f"Generated {len(claims_df)} new claims")
print(claims_df.head())