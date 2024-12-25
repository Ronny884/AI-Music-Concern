import asyncio
from openai import AsyncOpenAI
from departments.communication_department.prompts import \
    prompt_for_email_message_creating_en, \
    prompt_for_email_message_creating_ru
from config.config_reader import settings

client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)


async def create_email_message(company_name, language):
    try:
        response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": prompt_for_email_message_creating_en(company_name, language)
                },
            ]
            }
        ]
        )
        content = response.choices[0].message.content
        return str(content)
    except Exception as e:
        print(e)
        return None