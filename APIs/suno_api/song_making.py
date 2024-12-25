import json
import requests
import time
from config.config_reader import settings


def make_a_song(prompt: str,
                tags: str,
                title: str):
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
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        response_data = response.json()
        print(response_data)
        ids = [item.get('id') for item in response_data]  # вытаскиваю id новых песенок
        print(ids)
        urls = []
        for id in ids:
            urls.append(f"https://suno.com/song/{id}")  # это ссылки на сгенерированные песни

        print('Start')
        time.sleep(180)  # Задержка на 180 секунд чтоб песни успели сгенерироваться
        print('Executed after 180 seconds')
        paths = []
        for id in ids:
            response_audio = requests.get(f"https://cdn1.suno.ai/{id}.mp3")  # скачивание аудио
            response_video = requests.get(f"https://cdn1.suno.ai/{id}.mp4")  # скачивание видео

            path_audio = f'D:\Python_projects_2\music_making\media\\{title}\\{id}.mp3'
            path_video = f'D:\Python_projects_2\music_making\media\\{title}\\{id}.mp4'

            with open(path_audio, 'wb') as file:
                file.write(response_audio.content)
                paths.append(path)
        return paths
    else:
        print("resronse status code: ")
        print(response_audio.status_code)
        print("ошибка генерации")
        return False


