import aiohttp
import asyncio
from config.config_reader import settings


async def get_json_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()


async def get_contacts(domain):
    url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={settings.HUNTER_IO_API_KEY}"
    json_data = await get_json_response(url)
    if json_data:
        emails = []
        for email in json_data['data']['emails']:
            emails.append(email['value'])
        company_contacts_data = {
            'email': emails,
            'linkedin': json_data['data'].get('linkedin'),
            'instagram': json_data['data'].get('instagram'),
            'telegram': json_data['data'].get('telegram')
        }

        print('Найдено с hunter.io:')
        print(company_contacts_data)
        return company_contacts_data







