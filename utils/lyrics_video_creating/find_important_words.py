import asyncio
import json
from openai import AsyncOpenAI
from config.config_reader import settings

client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)


def create_prompt(song_text):
    return f"""
Внимательно проанализируй текст песни:
{song_text}.

Найди все важные слова данной песни, ими могут быть:
1) имена и фамилии
2) любые названия (компаний и организаций, городов, стран, улиц)
3) любые даты и цифры

ВАЖНО: 
* в твоём ответе они должны быть перечислены в строку через запятую
* все найденные слова должны быть перечислены в той же форме (склонении),
в которой они находятся в тексте песни! 
* написаны они должны быть на том же языке, что и в тексте
"""


async def find_important_words(song_text):
    try:
        response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": create_prompt(song_text)
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