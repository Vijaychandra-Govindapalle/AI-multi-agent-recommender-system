import pandas as pd
from embeddings.embedding_generator import get_embedding
import os
import pickle

class ProductAgent:
    def __init__(self, product_csv_path="backend/data/products.csv", cache_path="backend/embeddings/product_embeddings.pkl"):
        self.products = pd.read_csv(product_csv_path)
        self.cache_path = cache_path
        self.embeddings = self.load_or_generate_embeddings()

    def generate_description(self, row):
        desc = f"This is a {row['Category']} product under the {row['Subcategory']} subcategory from {row['Brand']}, "
        desc += f"popular in {row['Season']} in {row['Geographical_Location']}."
        desc += " Recommended for holidays." if row['Holiday'] == "Yes" else " Not recommended for holidays."
        return desc

    def load_or_generate_embeddings(self):
        if os.path.exists(self.cache_path):
            with open(self.cache_path, "rb") as f:
                return pickle.load(f)
        embeddings = {}
        for _, row in self.products.iterrows():
            product_id = row["Product_ID"]
            description = self.generate_description(row)
            embeddings[product_id] = get_embedding(description, product_id, "product")
        with open(self.cache_path, "wb") as f:
            pickle.dump(embeddings, f)
        return embeddings

    def get_all_product_embeddings(self):
        return self.embeddings

    def get_product_by_id(self, product_id):
        return self.products[self.products["Product_ID"] == product_id].to_dict(orient="records")[0]
