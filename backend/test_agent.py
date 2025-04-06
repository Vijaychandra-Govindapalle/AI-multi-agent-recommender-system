# backend/test_recommendation_agent.py

from agents.recommendation_agent import RecommendationAgent

print("🚀 Starting recommendation test...")

agent = RecommendationAgent()
recommendations = agent.recommend_products("C1001", top_n=5)

if recommendations:
    print("✅ Recommendations:", recommendations)
else:
    print("❌ No recommendations returned.")
