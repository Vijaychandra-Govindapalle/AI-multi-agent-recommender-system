from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.recommendation_agent import RecommendationAgent
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
agent = RecommendationAgent()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace * with frontend URL for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RecommendRequest(BaseModel):
    customer_id: str

@app.post("/recommend")
def recommend(request: RecommendRequest):
    try:
        recommendations = agent.recommend_products(request.customer_id)
        return {"customer_id": request.customer_id, "recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
