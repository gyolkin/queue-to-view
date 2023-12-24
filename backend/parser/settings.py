BOT_NAME = "parser"

SPIDER_MODULES = ["parser.spiders"]
NEWSPIDER_MODULE = "parser.spiders"

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
DEFAULT_REQUEST_HEADERS = {
    "Accept-Language": "ru-RU,ru;q=0.9",
}

ITEM_PIPELINES = {
    "parser.pipelines.ParserPipeline": 300,
}

FEEDS = {
    "result/movies.json": {"format": "json", "overwrite": True},
}

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

LOG_LEVEL = "INFO"
LOG_FORMAT = "%(levelname)s: %(message)s"
LOG_FILE = "logs/past_parse_log.txt"
LOG_FILE_APPEND = False

DOWNLOAD_DELAY = 3
ROBOTSTXT_OBEY = False
