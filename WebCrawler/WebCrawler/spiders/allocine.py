import scrapy
from scrapy import Request
from ..items import ReviewsAllocineItem


class AllocineSpider(scrapy.Spider):
    name = 'allocine'
    allowed_domains = ['www.allocine.fr']

    # Liste des pages à collecter
    start_urls = [f'https://www.allocine.fr/film/meilleurs/?page={n}' for n in range(1, 10)]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_allocine)

    def parse_allocine(self, response):
        liste_film = response.css('li.mdl')

        # Boucle qui parcours l'ensemble des éléments de la liste des films
        for film in liste_film:
            item = ReviewsAllocineItem()

            # Nom du film
            try:
                item['title'] = film.css('a.meta-title-link::text').get()
            except:
                item['title'] = 'None'

            # Lien de l'image du film
            try:
                item['img'] = film.css('img.thumbnail-img').attrib['src']
            except:
                item['img'] = 'None'

            # Auteur du film
            try:
                item['author'] = film.css('a.blue-link::text').get()
            except:
                item['author'] = 'None'

            # Durée du film
            try:
                item['time'] = film.css('div.meta-body-info::text').get()
            except:
                item['time'] = 'None'

            # Genre cinématographique
            try:
                item['genre'] = film.css('div.meta-body-item span::text').getall()
            except:
                item['genre'] = 'None'

            # Score du film
            try:
                item['score'] = film.css('span.stareval-note::text').get()
            except:
                item['score'] = 'None'

            # Description du film
            try:
                item['desc'] = film.css('div.synopsis div.content-txt::text').get()
            except:
                item['desc'] = 'None'

            # Date de sortie
            try:
                item['release'] = film.css('span.date::text').get()
            except:
                item['release'] = 'None'

            yield item.clean_item()
