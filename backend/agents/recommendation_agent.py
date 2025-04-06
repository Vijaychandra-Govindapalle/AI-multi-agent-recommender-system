# backend/agents/recommendation_agent.py

import heapq
from backend.agents.customer_agent import CustomerAgent
from backend.agents.product_agent import ProductAgent
from backend.embeddings.embedding_generator import get_embedding
from backend.utils.similarity import cosine_similarity


class RecommendationAgent:
    def __init__(self):
        self.customer_agent = CustomerAgent()
        self.product_agent = ProductAgent()

    def recommend_products(self, customer_id, top_n=5):
        customer_profile = self.customer_agent.get_customer_profile(customer_id)
        intent = self.customer_agent.extract_intent(customer_profile)
        if not intent:
            return []

        intent_embedding = get_embedding(intent, entity_id=customer_id, entity_type="customer")

        product_scores = []
        for product_id, product_embedding in self.product_agent.embeddings.items():
            score = cosine_similarity(intent_embedding, product_embedding)
            product_scores.append((score, product_id))

        top_matches = heapq.nlargest(top_n, product_scores, key=lambda x: x[0])
        recommended_products = [product_id for _, product_id in top_matches]
        return recommended_products
