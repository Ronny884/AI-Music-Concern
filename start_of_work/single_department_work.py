import asyncio

from config.config_reader import settings
from email_clients.smtp_client import send
from db.orm import *

from departments.areas_scoping_department.scoping_crew import ScopingCrew
from departments.companies_searching_department.search_crew import CompaniesResearchCrew
from departments.detail_research_department.research_agency import DetailResearchAgency
from departments.music_creating_department.music_creating_using_completion import write_song
from departments.communication_department.email_generation_completion import create_email_message

from utils.language_definition.choose_language import choose_the_most_popular_language

from APIs.hunter_io_api.hunter_io_api import get_contacts


def run_scoping_crew(areas_count):
    scoping_crew_inputs = {
        'count': areas_count,
        'GoodAI_url': 'goodai_url'
    }
    areas_dict = ScopingCrew(scoping_crew_inputs).find_areas_using_marketing_methods()
    print(areas_dict)
    return areas_dict


def run_companies_searching_crew(companies_count, area, region):
    companies_research_inputs = {
        'count': companies_count,
        'area': area,
        'region': region
    }
    companies = CompaniesResearchCrew(companies_research_inputs).make_crew()
    print(companies)
    return companies


def run_research_for_single_company(company_name, area):
    company_detail_info = DetailResearchAgency(name=company_name, area=area,
                                               contacts_searching=False).research()
    print(company_detail_info)
    return company_detail_info


async def make_email_message(company_name, language):
    message = await create_email_message(company_name, language)
    print(message)
    return message


async def make_music_text(research_material, language):
    music = await write_song(research_material, language)
    music_text = music[0]
    print(music_text)
    return music_text

