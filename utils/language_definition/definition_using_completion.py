import asyncio
import json
from openai import AsyncOpenAI
from config.config_reader import settings

client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)


async def choose_the_most_popular_language(region):
    function_json = \
        {
            "type": "function",
            "function": {
            "name": "set_language",
            "description": f"Set the most popular language in {region}",
            "parameters": {
                "type": "object",
                "properties": {
                    "language": {
                        "type": "string",
                        "description": "the most popular language in {region}",
                    }
                },
                "required": ["language"],
            },
        }
        }

    try:
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text":
                f"""
                Identify ONE MOST popular language for the {region} 
                (it doesn't have to be a national language, just the most popular).
                You MUST call the 'set_language' function!
                """
                },
            ]
            }
        ],
            tool_choice={"type": "function", "function": {"name": "set_language"}},
            tools=[function_json]
        )
        content = response.choices[0].message.content
        try:
            tool_calls = response.choices[0].message.tool_calls
            language = json.loads(tool_calls[0].function.arguments)['language']
            return str(language)
        except:
            return str(content)
    except Exception as e:
        print(e)
        return None