import scrapy


class MovieItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    release_year = scrapy.Field()
    duration = scrapy.Field()
    country = scrapy.Field()
    genres = scrapy.Field()
    imdb_rating = scrapy.Field()
    poster = scrapy.Field()
