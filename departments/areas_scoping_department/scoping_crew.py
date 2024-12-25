from crewai import Agent, Crew, Process, Task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from pydantic import BaseModel, Field

from departments.areas_scoping_department.tasks_prompts import *
from departments.areas_scoping_department.agents_prompts import *


class Area(BaseModel):
    top_number: str = Field(..., description="Номер в топе для данной сферы")
    area_name: str = Field(..., description="Название сферы бизнеса")
    description: str = Field(..., description="Краткое описание в 1-2 предложения, "
                                              "почему данная сфера релевантна")


class Areas(BaseModel):
    areas: list[Area] = Field(..., description="Список всех найденных сфер бизнеса")


class Case(BaseModel):
    area_name: str = Field(..., description="Название сферы бизнеса, где был внедрён ИИ")
    description: str = Field(..., description="Краткое описание в 2-3 предложения, "
                                              "данного кейса внедрения ИИ")


class Cases(BaseModel):
    cases: list[Case] = Field(..., description="Список всех найденных кейсов внедрения ИИ")


class ScopingCrew:
    def __init__(self, inputs):
        self.inputs = inputs

        self.market_analyst = Agent(
            role="market_analyst",
            goal=market_analyst_goal,
            backstory=market_analyst_backstory,
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
            # max_iter=20
        )

        self.relevance_and_ranking_specialist = Agent(
            role="relevance_and_ranking_specialist",
            goal=relevance_and_ranking_specialist_goal,
            backstory=relevance_and_ranking_specialist_backstory,
            verbose=True,
            # max_iter=20
        )

        self.goodai_analyze = Task(
            expected_output=goodai_analyze_output,
            description=goodai_analyze_description,
            agent=self.market_analyst,
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
        )

        self.market_and_competitor_research = Task(
            expected_output=market_and_competitor_research_output,
            description=market_and_competitor_research_description,
            agent=self.market_analyst,
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            context=[self.goodai_analyze]
        )

        self.definition_of_relevance_criteria = Task(
            expected_output=definition_of_relevance_criteria_output,
            description=definition_of_relevance_criteria_description,
            agent=self.relevance_and_ranking_specialist,
            context=[self.market_and_competitor_research, self.goodai_analyze]
        )

        self.make_areas_list = Task(
            expected_output=make_areas_list_output,
            description=make_areas_list_description,
            agent=self.relevance_and_ranking_specialist,
            context=[self.market_and_competitor_research, self.definition_of_relevance_criteria]
        )

        self.assessment_and_ranking_of_business_areas = Task(
            expected_output=assessment_and_ranking_of_business_areas_output,
            description=assessment_and_ranking_of_business_areas_description,
            agent=self.relevance_and_ranking_specialist,
            context=[self.definition_of_relevance_criteria, self.make_areas_list],
            output_json=Areas
        )

        self.find_interesting_cases = Task(
            expected_output=find_interesting_cases_output,
            description=find_interesting_cases_description,
            agent=self.market_analyst,
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            output_json=Cases
        )

    def find_areas_using_marketing_methods(self):
        find_areas_crew = Crew(agents=[self.market_analyst, self.relevance_and_ranking_specialist],
                               tasks=[self.goodai_analyze, self.market_and_competitor_research,
                                      self.definition_of_relevance_criteria, self.make_areas_list,
                                      self.assessment_and_ranking_of_business_areas],
                               process=Process.sequential)
        find_areas_crew.kickoff(inputs=self.inputs)
        areas_dict = self.assessment_and_ranking_of_business_areas.output.json_dict
        return areas_dict

    def find_areas_using_interesting_cases(self):
        find_areas_crew = Crew(agents=[self.market_analyst],
                               tasks=[self.goodai_analyze, self.find_interesting_cases],
                               process=Process.sequential)
        find_areas_crew.kickoff(inputs=self.inputs)
        areas_dict = self.find_interesting_cases.output.json_dict
        return areas_dict





