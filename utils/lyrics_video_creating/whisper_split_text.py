import asyncio
from openai import AsyncOpenAI
from config.config_reader import settings


client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)


async def get_split_text(audio_file, prompt):
    with open(audio_file, "rb") as f:
        transcription = await client.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            response_format="verbose_json",
            timestamp_granularities=["segment"],
            prompt=prompt,
            language="en",
        )
        print(transcription.dict())
        return transcription.dict()