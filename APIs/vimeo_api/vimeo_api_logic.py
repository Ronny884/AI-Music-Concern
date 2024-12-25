import json
import time
import vimeo
from config.config_reader import settings


client = vimeo.VimeoClient(
    token=settings.VIMEO_TOKEN,
    key=settings.VIMEO_KEY,
    secret=settings.VIMEO_SECRET
  )


def upload_video(file_name, video_name, description):
    uri = client.upload(file_name, data={
        'name': video_name,
        'description': description
    })
    print(uri)
    return uri


def check_transcoding_status(uri):
    response = client.get(uri + '?fields=transcode.status').json()
    status = response['transcode']['status']
    if status == 'complete':
        print('Видео транскодировано')
        return status
    elif status == 'in_progress':
        print('Видео в процессе транскодирования')
        return status
    else:
        print('Ошибка транскодирования')
        return 'error'


def get_video_link(uri):
    response = client.get(uri + '?fields=link').json()
    print(response['link'])
    return response['link']


def upload_to_vimeo(
        file_path,
        video_name,
        description
):
    uri = upload_video(file_path, video_name, description)
    link = get_video_link(uri)

    transcoding_ststus = 'in_progress'
    while transcoding_ststus == 'in_progress':
        time.sleep(10)
        transcoding_ststus = check_transcoding_status(uri)
        if transcoding_ststus == 'error':
            raise Exception('Видео не может быть загружено на vimeo')
    return link


def get_img(video_id):
    response = client.get(f'https://api.vimeo.com/videos/{video_id}/pictures').json()
    print(response)






