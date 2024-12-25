import asyncio
from utils.language_definition.languages import languages
from utils.language_definition.definition_using_completion import choose_the_most_popular_language


async def choose_language(region):
    if region in languages.keys():
        language = languages[region]
    else:
        language = await choose_the_most_popular_language(region)
        if language is None:
            language = region
    return language