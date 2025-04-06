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

        # Split multi-interest intent into individual topics
        interest_phrases = [s.strip() for s in intent.split(',') if s.strip()]
        if not interest_phrases:
            interest_phrases = [intent.strip()]

        interest_embeddings = [
            get_embedding(interest, entity_id=f"{customer_id}_{i}", entity_type="customer_intent")
            for i, interest in enumerate(interest_phrases)
        ]

        # Get top matches per interest
        selected_products = set()
        for interest_emb in interest_embeddings:
            best_score = -1
            best_product = None
            for product_id, product_embedding in self.product_agent.embeddings.items():
                if product_id in selected_products:
                    continue
                score = cosine_similarity(interest_emb, product_embedding)
                if score > best_score:
                    best_score = score
                    best_product = product_id
            if best_product:
                selected_products.add(best_product)

        # Fill remaining slots if we haven't hit top_n
        if len(selected_products) < top_n:
            remaining_slots = top_n - len(selected_products)
            additional_scores = []
            for product_id, product_embedding in self.product_agent.embeddings.items():
                if product_id in selected_products:
                    continue
                similarities = [cosine_similarity(emb, product_embedding) for emb in interest_embeddings]
                avg_score = sum(similarities) / len(similarities)
                additional_scores.append((avg_score, product_id))

            additional_scores.sort(reverse=True)
            for _, product_id in additional_scores[:remaining_slots]:
                selected_products.add(product_id)

        recommended_products = [
            self.product_agent.get_product_by_id(pid) for pid in selected_products
        ]
        return recommended_products
