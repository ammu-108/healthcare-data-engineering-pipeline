import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(200)

output_dir = Path(
    "/Workspace/Users/durga20010615@gmail.com/healthcare-data-engineering-pipeline/data/incoming"
)
output_dir.mkdir(parents=True, exist_ok=True)

claims = []

for i in range(321, 331):
    claims.append({
        "claim_id": f"CLM{i:05d}",
        "member_id": f"MEM{np.random.randint(1, 101):04d}",
        "provider_id": f"PRV{np.random.randint(1, 31):03d}",
        "claim_date": pd.Timestamp("2026-10-11")
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
claims_df.to_csv(output_dir / "claims_batch_002.csv", index=False)

print("Generated claims:", len(claims_df))
print("Claim IDs:", claims_df["claim_id"].min(), "to", claims_df["claim_id"].max())