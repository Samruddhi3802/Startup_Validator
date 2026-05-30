import os
from crewai import Agent, LLM
from dotenv import load_dotenv

load_dotenv()

ceo_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

worker_llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

class StartupAgents:
    def research_agent(self, tools):
        return Agent(
            role='Market Research Specialist',
            goal='Find current market trends and competitor gaps for {idea}',
            backstory='You are a top-tier analyst who uncovers hidden market opportunities.',
            tools=tools,
            llm=worker_llm,
            verbose=True
        )

    def feasibility_agent(self, tools):
        return Agent(
            role='Technical Feasibility Analyst',
            goal='Evaluate the technical requirements and build-time for {idea}',
            backstory='You are a CTO with 20 years of experience in software architecture.',
            tools=tools,
            llm=worker_llm,
            verbose=True
        )

    def monetization_agent(self):
        return Agent(
            role='Business Strategist',
            goal='Design a high-growth revenue model for {idea}',
            backstory='You specialize in SaaS and marketplace monetization strategies.',
            llm=worker_llm,
            verbose=True
        )

    def risk_agent(self):
        return Agent(
            role='Risk Auditor',
            goal='Identify potential legal, market, and execution risks for {idea}',
            backstory='You are a conservative auditor who ensures no blind spots remain.',
            llm=worker_llm,
            verbose=True
        )

    def summary_agent(self):
        return Agent(
            role='Chief Executive Officer',
            goal='Synthesize all agent reports into a final executive summary',
            backstory='You are a visionary leader who makes the final "Go/No-Go" decision.',
            llm=ceo_llm,
            verbose=True
        )