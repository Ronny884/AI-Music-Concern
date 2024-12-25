import cloudinary
from cloudinary import CloudinaryImage
import cloudinary.uploader
import cloudinary.api
import json
from config.config_reader import settings


def upload_photo_to_cloudinary(image_path):
    try:
        cloudinary.config(
            cloud_name=settings.CLOUDINARY_NAME,
            api_key=settings.CLOUDINARY_API_KEY,
            api_secret=settings.CLOUDINARY_API_SECRET,
        )
        result = cloudinary.uploader.upload(image_path)
        print(result['secure_url'])
        return result['secure_url']
    except Exception as e:
        print(e)

