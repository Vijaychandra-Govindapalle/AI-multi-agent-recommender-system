import pandas as pd
import subprocess
import json

class CustomerAgent:
    def __init__(self, csv_path: str = "backend/data/customers.csv"):
        self.customers = pd.read_csv(csv_path)

    def get_customer_profile(self, customer_id: str) -> dict:
        customer = self.customers[self.customers["Customer_ID"] == customer_id]
        if customer.empty:
            raise ValueError("Customer ID not found.")
        return customer.iloc[0].to_dict()

    def extract_intent(self, customer_profile: dict) -> str:
        prompt = (
            f"Given the following customer profile, describe what kind of products "
            f"this customer is likely to be interested in:\n\n{json.dumps(customer_profile, indent=2)}\n\n"
            f"Only output the customer intent in one sentence."
        )

        result = subprocess.run(
            ["ollama", "run", "llama3", prompt],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            raise RuntimeError("Failed to extract intent from customer profile")

        return result.stdout.strip()
