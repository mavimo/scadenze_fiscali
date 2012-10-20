from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from scadenze_fiscali.items import ScadenzeFiscaliItem
from urlparse import urljoin
from scrapy import log


class ScadenzeFiscaliSpider(BaseSpider):
    name = "scadenze_fiscali"
    allowed_domains = ["agenziaentrate.gov.it"]
    year = 2012
    start_urls = [
        "http://www1.agenziaentrate.gov.it/documentazione/scadenzefiscali/index.htm?selezionetemporale=mese&mese=%02d-%d" % (n, year) for n in range(1, 12)
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        deadlines = hxs.select("//div[@id='lista_scad_fisc']/ul")
        items = []

        next_page = hxs.select("//div[@id='contenuti_una_colonna']/p[2]/a[last()]/@href").extract()

        if not not next_page:
            yield Request(urljoin(response.url, next_page[0]), self.parse)

        for deadline in deadlines:
            item = ScadenzeFiscaliItem()
            item['when'] = self.html_string(deadline, 'li[1]/text()')
            item['who'] = self.html_string(deadline, 'li[2]/text()')
            item['what'] = self.html_string(deadline, 'li[3]/text()')
            item['how'] = self.html_string(deadline, 'li[4]/text()')
            item['code'] = self.html_string(deadline, 'li[5]/text()')
            item['type'] = self.html_string(deadline, 'li[6]/text()')
            item['category'] = self.html_string(deadline, 'li[7]//a/text()')
            items.append(item)

        for item in items:
            yield item

    def html_string(self, item, xpath):
        res = []
        for i in item.select(xpath).extract():
            res.append(i.strip())

        return res
