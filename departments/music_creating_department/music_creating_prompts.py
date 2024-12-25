
def topic_for_music_creating(language):
    return f"""
YOUR TASKS:
1) Generate a song in the {language} language using the facts provided, 
including as much as possible 
fun information about the company, the text should be 1000-1500 characters long including spaces, 
use eight lines.
Use rhymes that fit the {language} language.

2) Make sure to call the 'lyrics_function' function and 
pass only the text with verse and chorus indications as an argument to it. 
You're only supposed to pass on the text without further explanation, 
but with verse and chorus indications.
"""


def topic_for_style_and_name_creating(language, research_material, lyrics):
    return f"""
Analyze the company's data:
{research_material}

Look at the song we wrote about this company:
{lyrics}

YOUR TASKS:
1) Think of a good title for this song. 
The title should include 2-4 words, there should be no punctuation
The title must include the name of the company.
The title of the song should be in {language}, 
but the company name should be spelled strictly as it appears in the material about the company.

2) Think about what style would be suitable for this song based on the information about the company
and on the nature of the company. 
Choose one style from the following: pop, rock, hip-hop, pop-rock, electronic, jazz.

3) You make sure you call a 'set_title_and_style' function and 
pass the song title and song style you came up with to it
"""


lyrics_function_json = \
        {
            "type": "function",
            "function": {
            "name": "lyrics_function",
            "description": f"generated lyrics",
            "parameters": {
                "type": "object",
                "properties": {
                    "lyrics": {
                        "type": "string",
                        "description": "generated lyrics",
                    }
                },
                "required": ["lyrics"],
            },
        }
        }


function_json = \
        {
            "type": "function",
            "function": {
            "name": "set_title_and_style",
            "description": f"Set title and style for music",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "music title",
                    },
                    "style": {
                        "type": "string",
                        "description": "music style",
                    }
                },
                "required": ["title", "style"],
            },
        }
        }