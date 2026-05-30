from crewai import Task

class StartupTasks:  
    def research_task(self, agent, idea):
        return Task(
            description=f"Analyze market trends, competitor gaps, and industry growth for the idea: {idea}. Use the 'market_report_tool' with a relevant search query to get the latest data from our internal reports.",
            agent=agent,
            expected_output="A comprehensive report on market size, top 3 competitors, and current trends."
        )

    def feasibility_task(self, agent, idea):
        return Task(
            description=f"Evaluate the technical requirements, potential tech stack, and estimated development timeline for: {idea}.",
            agent=agent,
            expected_output="A technical roadmap including suggested tools and a 6-month development plan."
        )

    def monetization_task(self, agent, idea):
        return Task(
            description=f"Design a sustainable revenue model for: {idea}. Consider SaaS, marketplace fees, or freemium models.",
            agent=agent,
            expected_output="A detailed monetization strategy with 3 specific pricing tiers."
        )

    def risk_task(self, agent, idea):
        return Task(
            description=f"Identify potential legal, execution, and market risks for the startup idea: {idea}.",
            agent=agent,
            expected_output="A risk assessment table with 5 key risks and their corresponding mitigation strategies."
        )

    def summary_task(self, agent, idea):
        return Task(
            description=f"Synthesize the findings from the research, feasibility, monetization, and risk reports for: {idea}.",
            agent=agent,
            expected_output="A final 1-page Investment Memo that provides a clear 'Go/No-Go' recommendation."
        )