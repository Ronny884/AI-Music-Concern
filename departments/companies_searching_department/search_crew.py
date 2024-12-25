from crewai import Agent, Crew, Process, Task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

from departments.companies_searching_department.prompts import *


class Company(BaseModel):
    name: str = Field(..., description="Название компании")
    website: str = Field(..., description="URL сайта компании")


class Companies(BaseModel):
    data: list[Company] = Field(..., description="Все названия и URL's компаний")


class CompaniesResearchCrew:
    def __init__(self, inputs):
        self.inputs = inputs

        self.marketer = Agent(
            role="marketer",
            goal=marketer_goal,
            backstory=marketer_backstory,
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
            max_iter=100
        )

        self.director = Agent(
            role="director",
            goal=director_goal,
            backstory=director_backstory,
            verbose=True,
            max_iter=100
        )

        self.find_companies = Task(
            expected_output=find_companies_output,
            description=find_companies_description,
            agent=self.marketer,
            output_json=Companies
        )

        self.check_result = Task(
            expected_output=check_result_output,
            description=check_result_description,
            agent=self.director,
        )

    def make_crew(self):
        find_companies_crew = Crew(agents=[self.marketer, self.director],
                       tasks=[self.find_companies, self.check_result],
                       process=Process.hierarchical,
                       manager_llm=ChatOpenAI(model="gpt-4o-mini"))
        find_companies_crew.kickoff(inputs=self.inputs)
        companies_list = self.find_companies.output.json_dict
        return companies_list['data']
