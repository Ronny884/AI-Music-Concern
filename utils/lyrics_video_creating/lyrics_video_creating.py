import os
import asyncio
import aiofiles
from io import BytesIO
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageOps, ImageFont
import numpy as np
from moviepy.editor import *
from utils.lyrics_video_creating.whisper_split_text import *
from utils.lyrics_video_creating.create_images import *
from utils.lyrics_video_creating.find_important_words import find_important_words


async def create_video(image, audio_path, output_path, lyrics):
    # Конвертируем изображение в RGBA
    image = image.convert("RGBA")
    width, height = image.size

    # Создание клипа с изображением
    image_clip = ImageClip(np.array(image)).set_duration(AudioFileClip(audio_path).duration)

    # Поиск важных слов в песне
    prompt = await find_important_words(lyrics)

    # Разделение текста на сегменты
    lyrics_timing = await get_split_text(audio_path, prompt)

    # Создание клипа с текстом
    def make_frame(t):
        img = image.copy()
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arialbd.ttf", 23)
        current_segment = ""

        # Определение текущего четверостишия и слова
        for segment_info in lyrics_timing['segments']:
            start_time = segment_info['start']
            end_time = segment_info['end']
            if start_time <= t <= end_time:
                current_segment = segment_info['text']
                break

        # Отображение сегмента
        y_offset = height // 2 + 150
        lines = current_segment.split(',')
        max_lines = 5

        for i, line in enumerate(lines):
            if line:
                line = line.lstrip()
                line = line[0].upper() + line[1:]
            if i >= max_lines:
                break
            color = 'white'
            text_bbox = draw.textbbox((0, 0), line, font=font)
            text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

            # Разделение строки на две, если она превышает 500 пикселей
            if text_width > 500:
                words = line.split()
                line1, line2 = "", ""
                for word in words:
                    if draw.textbbox((0, 0), line1 + word, font=font)[2] - \
                            draw.textbbox((0, 0), line1, font=font)[0] <= 400:
                        line1 += word + " "
                    else:
                        line2 += word + " "
                lines.insert(i + 1, line2.strip())
                line = line1.strip()

            text_bbox = draw.textbbox((0, 0), line, font=font)
            text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
            x_offset = (width - text_width) // 2

            draw.text((x_offset, y_offset), line, font=font, fill=color)
            y_offset += text_height + 10

        return np.array(img.convert("RGB"))

    text_clip = VideoClip(make_frame, duration=AudioFileClip(audio_path).duration)

    # Объединение клипов
    video = CompositeVideoClip([image_clip, text_clip])
    video = video.set_audio(AudioFileClip(audio_path))

    # Сохранение видео
    video.write_videofile(output_path, codec="libx264", fps=24)


async def get_default_img(img_name):
    current_path = os.path.abspath(__file__)
    project_root = os.path.dirname(current_path)
    while not os.path.exists(os.path.join(project_root, 'default_media')):
        project_root = os.path.dirname(project_root)
    wotermark_path = os.path.join(project_root, 'default_media', img_name)
    return wotermark_path


async def get_company_media_path(company_name, area, media_name):
    # Получаем путь к текущему файлу
    current_path = os.path.abspath(__file__)

    # Поднимаемся на несколько уровней вверх, пока не достигнем корневой папки проекта
    project_root = os.path.dirname(current_path)
    while not os.path.exists(os.path.join(project_root, 'media')):
        project_root = os.path.dirname(project_root)

    save_path = os.path.join(project_root, 'media', area, company_name, media_name)
    return save_path


async def create_lyrics_video(
        image_path,
        song_name,
        music_path,
        lyrics,
        company_name,
        area
):
    blurred_background = await create_blurred_background(image_path)
    combine_image = await add_image_on_top(image_path, blurred_background)
    image_with_text = await add_text_to_image(combine_image, song_name)

    # получение дефолтных изображений логотипа и кнопки
    wotermark = await get_default_img('logo-goodai.png')
    button = await get_default_img('play_button.png')

    # получение объекта финального изображения перед созданием видео
    finish_image_with_wotermark = await add_image_watermark(image_with_text, wotermark)

    # получение окончательных путей к видео и превью
    video_output_path = await get_company_media_path(company_name, area, 'lyrics_video.mp4')
    image_with_button_output_path = await get_company_media_path(company_name, area, 'image_with_button.png')

    # создание и сохранение превью для видео
    await add_play_button(image_path, button, image_with_button_output_path)

    # создание и сохранение видео
    await create_video(
        image=finish_image_with_wotermark,
        audio_path=music_path,
        output_path=video_output_path,
        lyrics=lyrics
    )

    return {
        'video': video_output_path,
        'image_with_button': image_with_button_output_path
    }

