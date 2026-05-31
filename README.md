# Startup Validator — AI-Powered Startup Idea Analyzer

An intelligent multi-agent system built with **CrewAI** and **Groq LLaMA** that evaluates your startup idea from multiple expert perspectives — market research, technical feasibility, monetization strategy, risk auditing — and delivers an executive-level Go/No-Go decision.

---

## What It Does

Enter any startup idea and a crew of specialized AI agents analyzes it in parallel:

| Agent | Role |
|---|---|
| Market Research Specialist | Identifies trends, competitors & market gaps |
| Technical Feasibility Analyst | Evaluates tech stack, build time & complexity |
| Business Strategist | Designs revenue models & monetization paths |
| Risk Auditor | Flags legal, market & execution risks |
| CEO (Summary Agent) | Synthesizes all reports into a final decision |

The system uses a **sequential CrewAI process** with a CEO-level LLM (LLaMA 3.3-70B) for final synthesis and faster worker LLMs (LLaMA 3.1-8B) for specialized tasks.

---

## Project Structure

```
Startup_Validator/
├── app.py               # FastAPI backend server
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not committed)
├── .env.example         # Template for environment variables
├── data/
│   └── market_reports.txt  # Market research data used by agents
└── src/
    ├── agents.py        # Agent definitions (roles, goals, backstory)
    ├── crew.py          # Crew orchestration & tool setup
    └── tasks.py         # Task definitions for each agent
```

---

## Tech Stack

- **Backend:** FastAPI + Uvicorn
- **AI Framework:** [CrewAI](https://crewai.com/)
- **LLM Provider:** [Groq](https://groq.com/) (LLaMA 3.3-70B & LLaMA 3.1-8B)
- **Frontend:** Vanilla HTML/CSS/JS (served as static files)

---

## Getting Started

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd Startup_Validator
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

```bash
cp .env.example .env
```

Open `.env` and add your API keys:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> Get your free Groq API key at [console.groq.com](https://console.groq.com/)

### 5. Run the Application

```bash
python app.py
```

The server will start at **http://localhost:8000**

Open your browser and navigate to `http://localhost:8000` to use the app.

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/analyze` | Analyze a startup idea |

**Request Body:**
```json
{
  "idea": "An AI-powered recipe app that generates meals based on what's in your fridge"
}
```

**Response:**
```json
{
  "summary": "Executive summary with Go/No-Go decision...",
  "tasks": [
    { "agent": "Market Research Specialist", "raw": "..." },
    ...
  ],
  "stats": {
    "total_tokens": 5000,
    "prompt_tokens": 3000,
    "completion_tokens": 2000,
    "successful_requests": 5
  }
}
```

---

## Requirements

- Python 3.9+
- Groq API Key (free tier available)

---
