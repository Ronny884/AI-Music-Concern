import os
import asyncio
import aiofiles
from io import BytesIO
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageOps, ImageFont


async def create_blurred_background(image_path, blur_radius=30, brightness_factor=1.2):
    # Асинхронное чтение изображения
    async with aiofiles.open(image_path, 'rb') as f:
        image_data = await f.read()

    original_image = Image.open(BytesIO(image_data))

    # Применяем размытие
    blurred_image = original_image.filter(ImageFilter.GaussianBlur(blur_radius))

    # Делаем изображение более светлым
    enhancer = ImageEnhance.Brightness(blurred_image)
    brightened_image = enhancer.enhance(brightness_factor)

    cropped_image = brightened_image.resize((560, 800))
    return cropped_image


async def add_image_on_top(main_image_path, background_image):
    # Открываем основное изображение
    async with aiofiles.open(main_image_path, 'rb') as f:
        image_data = await f.read()

    image = Image.open(BytesIO(image_data)).convert("RGBA")
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0) + image.size, 20, fill=255)
    rounded_image = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    rounded_image.putalpha(mask)

    # Создаем новое изображение с фоновым изображением
    combined_image = background_image.copy()

    # Вставляем основное изображение в верхнюю часть фонового изображения
    main_image_position = (100, 80)
    combined_image.paste(rounded_image, main_image_position, rounded_image)

    return combined_image


async def add_text_to_image(image, text):
    # Параметры для добавления текста
    center_position = (280, 500)
    font_path = "arialbd.ttf"
    font_size = 30
    text_color = "white"
    max_width = 400

    # Создаём объект для рисования
    draw = ImageDraw.Draw(image)

    # Загружаем шрифт
    font = ImageFont.truetype(font_path, font_size)

    # Разбиваем текст на строки, чтобы он вписывался в заданную ширину
    lines = []
    words = text.split()
    line = ""
    for word in words:
        test_line = line + word + " "
        bbox = draw.textbbox((0, 0), test_line, font=font)
        width = bbox[2] - bbox[0]
        if width <= max_width:
            line = test_line
        else:
            lines.append(line)
            line = word + " "
    lines.append(line)  # Добавляем последнюю строку

    # Вычисляем начальную позицию для выравнивания текста по центру
    total_text_height = len(lines) * (font_size + 10) - 10
    y_offset = center_position[1] - total_text_height // 2

    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        x_offset = center_position[0] - text_width // 2
        draw.text((x_offset, y_offset), line, font=font, fill=text_color)
        y_offset += font_size + 10  # Смещение по вертикали для следующей строки

    return image


async def add_image_watermark(image, watermark):
    async with aiofiles.open(watermark, 'rb') as f:
        image_data = await f.read()

    # Изменяем размер водяного знака, если необходимо
    watermark = Image.open(BytesIO(image_data)).convert("RGBA")
    watermark_width, watermark_height = watermark.size
    image_width, image_height = image.size
    scale_factor = 0.25
    new_width = int(image_width * scale_factor)
    new_height = int(watermark_height * (new_width / watermark_width))
    watermark = watermark.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Увеличиваем прозрачность водяного знака
    alpha = 130  # Значение альфа-канала (0-255)
    watermark = watermark.split()
    watermark = Image.merge("RGBA",
                    (watermark[0], watermark[1], watermark[2], watermark[3].point(lambda p: p * alpha / 255)))

    # Определяем позицию для водяного знака
    x, y = (400, 750)

    # Добавляем водяной знак на изображение
    image.paste(watermark, (x, y), watermark)
    return image


async def add_play_button(image_path, button_image_path, output_path):
    async with aiofiles.open(image_path, 'rb') as f:
        image_data = await f.read()

    main_image = Image.open(BytesIO(image_data)).convert("RGBA")

    async with aiofiles.open(button_image_path, 'rb') as f:
        image_data = await f.read()

    button_image = Image.open(BytesIO(image_data)).convert("RGBA")

    main_width, main_height = main_image.size
    button_width, button_height = button_image.size

    button_scale_percentage = 0.5
    new_button_width = int(button_width * button_scale_percentage)
    new_button_height = int(button_height * button_scale_percentage)
    button_image = button_image.resize((new_button_width, new_button_height))

    position = ((main_width - new_button_width) // 2, (main_height - new_button_height) // 2)

    main_image.paste(button_image, position, button_image)
    main_image.save(output_path, format="PNG")


