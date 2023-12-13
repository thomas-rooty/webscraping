import scrapy
from scrapy import Request
from ..items import ReviewsMyAnimeListItem
from ..pipelines import *
from time import sleep


class MyAnimeListSpider(scrapy.Spider):
    name = 'myanimelist'
    allowed_domains = ['www.myanimelist.net']

    # Liste des pages à collecter
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    start_urls = [f'https://myanimelist.net/manga.php?letter={letter}' for letter in alphabet]
    database = DataBase('myanimelist')

    try:
        database.create_table(
            'myanimelist',
            title=db.String,
            img=db.String,
            desc=db.String,
        )
    except:
        pass

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_anime)

    def parse_anime(self, response):
        liste_anime = response.css('div.js-categories-seasonal table tr')[1:]

        # Boucle qui parcours l'ensemble des éléments de la liste des films
        for anime in liste_anime:
            item = ReviewsMyAnimeListItem()

            # Nom de l'anime
            try:
                item['title'] = anime.css('a strong::text').get()
            except:
                item['title'] = 'None'

            # Image de l'animé
            try:
                item['img'] = anime.css('div.picSurround img::attr(data-src)').get()
            except:
                item['img'] = 'None'

            # Description de l'animé
            try:
                item['desc'] = anime.css('div.pt4::text').get()
            except:
                item['desc'] = 'None'

            # Store data in database
            self.database.add_row('myanimelist', **item)

            yield item
