import logging
from parser.constants import GENRE_TO_ID
from parser.utils import (
    convert_country_code,
    convert_duration_to_minutes,
    convert_image_to_base64,
)

from scrapy.exceptions import DropItem


class ParserPipeline:
    def __init__(self):
        self.cache_titles = set()

    def process_item(self, item, spider):
        if item["title"] in self.cache_titles:
            raise DropItem(f"{item['title']}: Обнаружен и удален дубликат!")
        item["release_year"] = int(item["release_year"])
        item["imdb_rating"] = float(item["imdb_rating"])
        item["duration"] = convert_duration_to_minutes(item["duration"])
        item["genres"] = [
            GENRE_TO_ID.get(i)
            for i in item["genres"]
            if GENRE_TO_ID.get(i) is not None
        ]
        item["country"] = convert_country_code(item["country"])
        try:
            base64_image = convert_image_to_base64(item["poster"])
            item["poster"] = base64_image
        except Exception:
            logging.warning(
                "Ошибка конвертации изображения. Изображение не сохранено."
            )
            del item["poster"]
        self.cache_titles.add(item["title"])
        return item
