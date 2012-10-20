# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class ScadenzeFiscaliItem(Item):
    # define the fields for your item here like:
    when = Field()
    who = Field()
    what = Field()
    how = Field()
    code = Field()
    type = Field()
    category = Field()
    pass
