import cv2
import numpy as np


def remove_watermark(video_path, output_path, mask_path):
    # Загрузка видео и маски
    cap = cv2.VideoCapture(video_path)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

    # Получение параметров видео
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Применение inpainting для удаления водяного знака
        frame = cv2.inpaint(frame, mask, 3, cv2.INPAINT_TELEA)

        # Запись обработанного кадра
        out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Пример вызова функции
remove_watermark('input_video.mp4', 'output_video.mp4', 'mask.png')
