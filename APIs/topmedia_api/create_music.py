import os
import json
import aiohttp
import asyncio
from config.config_reader import settings


async def create_music(style, lyrics, company_name, area):
    async with aiohttp.ClientSession() as session:
        try:
            print('1')
            data = {
                "is_auto": 0,
                "prompt": style,
                "lyrics": lyrics,
                "title": company_name,
                "instrumental": 0
            }
            headers = {'x-api-key': settings.TOPMEDIA_API_KEY}
            async with session.post(url='https://api.topmediai.com/v1/music',
                                    json=data,
                                    headers=headers) as response:
                print('2')
                response_data = await response.json()
                res_data = response_data['data']
                if res_data == {}:
                    return None
                paths = []
                step = 0
                save_path = await get_company_media_path(company_name, area)
                image_path = await download_image(res_data[0]['image_file'], save_path)

                for song_data in res_data:
                    step += 1
                    path = await download_music(song_data['audio_file'], save_path, step)
                    paths.append(path)
                paths.append(image_path)
                return {
                    'song_1': paths[0],
                    'song_2': paths[1],
                    'image': paths[2]
                }

        except aiohttp.ClientError as e:
            print(f"Ошибка при выполнении запроса: {e}")
            return None


async def get_company_media_path(company_name, area):
    # Получаем путь к текущему файлу
    current_path = os.path.abspath(__file__)

    # Поднимаемся на несколько уровней вверх, пока не достигнем корневой папки проекта
    project_root = os.path.dirname(current_path)
    while not os.path.exists(os.path.join(project_root, 'media')):
        project_root = os.path.dirname(project_root)

    # Создаем директории, если они не существуют
    save_path = os.path.join(project_root, 'media', area, company_name)
    os.makedirs(save_path, exist_ok=True)

    return save_path


async def download_music(url, save_path, step):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                content = await response.read()

                # Сохраняем файл
                file_path = os.path.join(save_path, f"song_{step}.mp3")
                with open(file_path, 'wb') as file:
                    file.write(content)
                print(f"Музыка успешно скачана и сохранена в {file_path}")
                return file_path
        except aiohttp.ClientError as e:
            print(f"Ошибка при скачивании музыки: {e}")


async def download_image(url, save_path):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.read()
                image_path = os.path.join(save_path, f"image.png")
                with open(image_path, 'wb') as f:
                    f.write(content)
                return image_path
            else:
                print(f"Failed to download image. Status code: {response.status}")


