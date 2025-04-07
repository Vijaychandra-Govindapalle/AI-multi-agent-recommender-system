import json
import pandas as pd
import requests

class CustomerAgent:
    def __init__(self, csv_path: str = "data/customers.csv"):
        self.customers = pd.read_csv(csv_path)
        self.ollama_url = "http://ollama:11434/api/chat"

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

        payload = {
            "model": "llama3",
            "messages": [{"role": "user", "content": prompt}],
            "stream": False  # Make sure stream is disabled for a single JSON response
        }

        try:
            response = requests.post(self.ollama_url, json=payload)
            response.raise_for_status()
            response_data = response.json()  # should now be a single JSON object
            return response_data["message"]["content"].strip()
        except json.JSONDecodeError as e:
            raise RuntimeError(f"JSON decoding failed: {e}\nRaw response:\n{response.text}")
        except Exception as e:
            raise RuntimeError(f"Failed to extract intent from customer profile: {e}")