from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.crew import StartupAnalysisCrew
import uvicorn
import os

app = FastAPI(title="Startup Insight API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class IdeaRequest(BaseModel):
    idea: str

@app.post("/analyze")
async def analyze_idea(request: IdeaRequest):
    if not request.idea.strip():
        raise HTTPException(status_code=400, detail="Idea cannot be empty")
    
    try:
        analysis_crew = StartupAnalysisCrew(request.idea)
        result = analysis_crew.run()
        
        tasks_output = []
        for task in result.tasks_output:
            tasks_output.append({
                "agent": task.agent,
                "raw": task.raw
            })
            
        return {
            "summary": result.raw,
            "tasks": tasks_output,
            "stats": {
                "total_tokens": result.token_usage.total_tokens,
                "prompt_tokens": result.token_usage.prompt_tokens,
                "completion_tokens": result.token_usage.completion_tokens,
                "successful_requests": result.token_usage.successful_requests
            }
        }
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if not os.path.exists("static"):
    os.makedirs("static")

app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)