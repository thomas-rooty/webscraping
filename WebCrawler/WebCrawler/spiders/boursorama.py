import scrapy
from scrapy import Request
from ..items import ReviewsBoursoramaItem
from time import gmtime, strftime


class BoursoramaSpider(scrapy.Spider):
    name = 'boursorama'
    allowed_domains = ['finance.yahoo.com']
    start_urls = [f'https://www.boursorama.com/bourse/actions/palmares/france/page-{n}?france_filter%5Bmarket%5D=1rPCAC'
                  for n in range(1, 10)]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_boursorama)

    def parse_boursorama(self, response):
        liste_indices = response.css('tr.c-table__row')[3:]

        for indices in liste_indices:
            item = ReviewsBoursoramaItem()

            #indice boursier
            try:
                item['nomIndice'] = indices.css('a::text').get()
            except:
                item['nomIndice'] = 'None'

            #indice cours de l'action
            try:
                item['coursAction'] = indices.css('span.c-instrument--last::text').get()
            except:
                item['coursAction'] = 'None'

            #Variation de l'action
            try:
                item['variationAction'] = indices.css('span.c-instrument--instant-variation::text').get()
            except:
                item['variationAction'] = 'None'

            #Valeur la plus haute
            try:
                item['ath'] = indices.css('span.c-instrument--high::text').get()
            except:
                item['ath'] = 'None'

            #Valeur la plus basse
            try:
                item['atl'] = indices.css('span.c-instrument--low::text').get()
            except:
                item['atl'] = 'None'

            #Valeur d'ouverture
            try:
                item['valeurOuverture'] = indices.css('span.c-instrument--open::text').get()
            except:
                item['valeurOuverture'] = 'None'

            #Date de la collecte
            try:
                item['collectDatetime'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            except:
                item['collectDatetime'] = 'None'

            yield item
