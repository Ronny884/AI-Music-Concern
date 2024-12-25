import json
import aiohttp
import asyncio
from config.config_reader import settings


async def fetch_song(session, url, path):
    async with session.get(url) as response:
        content = await response.read()
        with open(path, 'wb') as file:
            file.write(content)
        return path


async def make_a_song(prompt: str, tags: str, title: str):
    url = settings.SUNO_API_CUSTOM_GENERATE_URL  # для генерации
    print(url)

    data = {
        "prompt": prompt,
        "make_instrumental": False,
        "wait_audio": False,
        "tags": tags,
        "title": title,
    }
    headers = {
        "Content-Type": "application/json"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=json.dumps(data)) as response:
            if response.status_code == 200:
                response_data = await response.json()
                ids = [item.get('id') for item in response_data]  # вытаскиваю id новых песенок
                print(ids)
                urls = [f"https://suno.com/song/{id}" for id in ids]  # это ссылки на сгенерированные песни

                print('Start')
                await asyncio.sleep(180)  # Задержка на 180 секунд
                print('Executed after 180 seconds')

                tasks = []
                for id in ids:
                    path = f'songs/{title}/{id}.mp3'
                    tasks.append(fetch_song(session, f"https://cdn1.suno.ai/{id}.mp3", path))

                paths = await asyncio.gather(*tasks)
                return paths
            else:
                print("response status code: ")
                print(response.status_code)
                print("ошибка генерации")
                return False
