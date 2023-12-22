# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import base64
import requests
import logging
import re

def convert_image_to_base64(image_url):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            return base64.b64encode(response.content).decode('utf-8')
        else:
            logging.error(f"Не удалось загрузить изображение, код состояния: {response.status_code}")
            return None
    except Exception as e:
        logging.error(f"Ошибка преобразования изображения в base64: {e}")
        return None

class ParserPipeline:
    def process_item(self, item, spider):
        if 'release_year' in item and item['release_year'].isdigit():
            item['release_year'] = int(item['release_year'])
            
        if 'duration' in item:
            item['duration'] = self.convert_duration_to_minutes(item['duration'])
            
        if 'poster' in item:
            base64_image = convert_image_to_base64(item['poster'])
            if base64_image:
                # Заменяем URL постера на его строку base64
                item['poster'] = base64_image
            else:
                logging.warning(f"Base64 conversion failed for: {item['poster']}")
                # Если преобразование не удалось, удаляем поле 'poster'
                del item['poster']
        return item
    
    def convert_duration_to_minutes(self, duration_str):
        # Регулярное выражение для поиска часов и минут
        match = re.search(r'(?:(\d+)h)?\s*(?:(\d+)m)?', duration_str)
        if match:
            # Преобразование найденных значений в минуты
            hours = int(match.group(1)) if match.group(1) else 0
            minutes = int(match.group(2)) if match.group(2) else 0
            return hours * 60 + minutes
        return 0


# class JsonWriterPipeline(object):

#     def open_spider(self, spider):
#         self.file = open('parser/result.json', 'w')

#     def close_spider(self, spider):
#         self.file.close()

#     def process_item(self, item, spider):
#         line = json.dumps(dict(item), ensure_ascii=False) + "\n"
#         self.file.write(line)
#         return item

