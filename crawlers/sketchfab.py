from utils.crawler import Crawler
from utils.url_builder import UrlBuilder


class SketchFabCrawler(Crawler):
    BASE_URL = "https://sketchfab.com/3d-models"
    BASE_PARAMS = {
        "features": "downloadable",
        "sort_by": "-likeCount"
    }

    def __init__(self):
        pass

    def start(self):
        url = UrlBuilder(SketchFabCrawler.BASE_URL,
                         SketchFabCrawler.BASE_PARAMS)

        print(url.add_params(cursor="test").build())
        print(url.add_params(curr="test").build())
        print(url.add_params(curr="test").build())
