from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from dotenv import load_dotenv
import os

# Load environment variables (MODEL and GEMINI_API_KEY should be in your .env)
load_dotenv()

@CrewBase
class MyCrew():
    """Capstone CrewAI Workflow"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Define LLM
    llm = LLM(
        model=os.environ["MODEL"],
        api_key=os.environ["GEMINI_API_KEY"]
    )

    # =========================
    # AGENTS
    # =========================
    @agent
    def input_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['input_agent'],
            verbose=True,
            llm=self.llm
        )

    @agent
    def keyword_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['keyword_agent'],
            verbose=True,
            llm=self.llm
        )

    @agent
    def story_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['story_agent'],
            verbose=True,
            llm=self.llm
        )

    @agent
    def evaluation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['evaluation_agent'],
            verbose=True,
            llm=self.llm
        )

    @agent
    def reporting_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_agent'],
            verbose=True,
            llm=self.llm
        )

    # =========================
    # TASKS
    # =========================
    @task
    def input_task(self) -> Task:
        return Task(
            config=self.tasks_config['input_task']
        )

    @task
    def keyword_task(self) -> Task:
        return Task(
            config=self.tasks_config['keyword_task']
        )

    @task
    def story_task(self) -> Task:
        return Task(
            config=self.tasks_config['story_task']
        )

    @task
    def evaluation_task(self) -> Task:
        return Task(
            config=self.tasks_config['evaluation_task']
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            output_file="final_report.md"  # Save final report here
        )

    # =========================
    # CREW
    # =========================
    @crew
    def crew(self) -> Crew:
        """Creates the Capstone Crew"""
        return Crew(
            agents=self.agents,   # Auto-collected from @agent
            tasks=self.tasks,     # Auto-collected from @task
            process=Process.sequential,  # Sequential pipeline
            verbose=True,
        )
