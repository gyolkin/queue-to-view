import scrapy
from parser.items import MovieItem


class ImdbSpider(scrapy.Spider):
    name = "imdb"
    allowed_domains = ["www.imdb.com"]
    start_urls = ["https://www.imdb.com/search/title/?groups=top_1000"]

    def parse(self, response):
        movie_links = response.css(
            "ul.ipc-metadata-list--base a::attr(href)"
        ).getall()
        for link in movie_links:
            format_link = response.urljoin(link)
            yield scrapy.Request(format_link, callback=self.parse_page)

    def parse_page(self, response):
        title = response.css("span.hero__primary-text::text").get()
        release_year = response.css(
            'ul.ipc-inline-list--show-dividers li a[href*="/releaseinfo"]::text'
        ).get()
        description = response.css('span[data-testid="plot-xl"]::text').get()
        duration = response.css(
            "ul.ipc-inline-list--show-dividers li::text"
        ).get()
        country = response.css(
            'li.ipc-metadata-list__item[data-testid="title-details-origin"] a.ipc-metadata-list-item__list-content-item--link::attr(href)'
        ).get()
        imdb_rating = response.css(
            'div[data-testid="hero-rating-bar__aggregate-rating__score"] span::text'
        ).get()
        genres = response.css(
            "div.ipc-chip-list__scroller .ipc-chip__text::text"
        ).getall()
        poster = response.css(
            "div.ipc-media--poster-27x40 img.ipc-image::attr(src)"
        ).get()
        result = {
            "title": title,
            "release_year": release_year,
            "description": description,
            "duration": duration,
            "country": country,
            "genres": genres,
            "imdb_rating": imdb_rating,
            "poster": poster,
        }
        yield MovieItem(result)
