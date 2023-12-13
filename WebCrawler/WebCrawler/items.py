import scrapy


# À ajouter au fichier items.py
class ReviewsAllocineItem(scrapy.Item):
    title = scrapy.Field()
    img = scrapy.Field()
    author = scrapy.Field()
    time = scrapy.Field()
    genre = scrapy.Field()
    score = scrapy.Field()
    desc = scrapy.Field()
    release = scrapy.Field()

    def clean_item(self):
        for key, value in self.items():
            if isinstance(value, str):
                self[key] = value.strip().replace('\n', '')
            elif isinstance(value, list):
                self[key] = [item.strip() for item in value]
        return self
