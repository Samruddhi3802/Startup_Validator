from crewai import Crew, Process
from crewai.tools import tool
from .agents import StartupAgents
from .tasks import StartupTasks 

@tool("market_report_tool")
def market_report_tool(search_query: str) -> str:
    """Reads the primary market research reports from the data directory. 
    Input should be a search query string relevant to the data you are looking for.
    Use this tool to get data on market trends, benchmarks, and monetization insights."""
    try:
        with open('data/market_reports.txt', 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error reading market reports: {str(e)}"

class StartupAnalysisCrew:
    def __init__(self, idea):
        self.idea = idea

    def run(self):
        agents = StartupAgents()
        tasks = StartupTasks()

        research_agent = agents.research_agent([market_report_tool])
        feasibility_agent = agents.feasibility_agent([market_report_tool])
        monetization_agent = agents.monetization_agent()
        risk_agent = agents.risk_agent()
        summary_agent = agents.summary_agent()

        t1 = tasks.research_task(research_agent, self.idea)
        t2 = tasks.feasibility_task(feasibility_agent, self.idea)
        t3 = tasks.monetization_task(monetization_agent, self.idea)
        t4 = tasks.risk_task(risk_agent, self.idea)
        t5 = tasks.summary_task(summary_agent, self.idea)

        crew = Crew(
            agents=[research_agent, feasibility_agent, monetization_agent, risk_agent, summary_agent],
            tasks=[t1, t2, t3, t4, t5],
            process=Process.sequential,
            verbose=True,
            cache=True,
            max_rpm=10
        )

        result = crew.kickoff()
        
        print(f"\n{'='*30}")
        print(f"TOTAL TOKEN USAGE: {result.token_usage}")
        print(f"{'='*30}\n")
        
        return result