from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.agents.recommendation_agent import RecommendationAgent

app = FastAPI()
agent = RecommendationAgent()

class RecommendRequest(BaseModel):
    customer_id: str

@app.post("/recommend")
def recommend(request: RecommendRequest):
    try:
        recommendations = agent.recommend_products(request.customer_id)
        return {"customer_id": request.customer_id, "recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
