import json
import asyncio
from openai import AsyncOpenAI
from config.config_reader import settings
from departments.music_creating_department.music_creating_prompts import *


client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)


async def write_song(research_material, language):
    try:
        # генерация текста песни
        response_song = await client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": f"{topic_for_music_creating(language)}, here are the material: {research_material}"
                },
            ]
            }
        ],
        tool_choice={"type": "function", "function": {"name": "lyrics_function"}},
        tools=[lyrics_function_json]
        )
        content = response_song.choices[0].message.content
        tool_calls = response_song.choices[0].message.tool_calls

        try:
            lyrics = str(json.loads(tool_calls[0].function.arguments)['lyrics'])
        except Exception as e:
            print(e)
            lyrics = str(content)

        # генерация названия песни и подбор её стиля
        response_title_style = await client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": topic_for_style_and_name_creating(language, research_material, lyrics)
                        },
                    ]
                }
            ],
            tool_choice={"type": "function", "function": {"name": "set_title_and_style"}},
            tools=[function_json]
        )
        tool_calls = response_title_style.choices[0].message.tool_calls
        title = str(json.loads(tool_calls[0].function.arguments)['title'])
        style = str(json.loads(tool_calls[0].function.arguments)['style'])

        # return lyrics, title, style
        return {
            'lyrics': lyrics,
            'title': title,
            'style': style
        }

    except Exception as e:
        print(e)
        return None