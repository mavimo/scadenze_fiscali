# Scrapy settings for scadenze_fiscali project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'scadenze_fiscali'

SPIDER_MODULES = ['scadenze_fiscali.spiders']
NEWSPIDER_MODULE = 'scadenze_fiscali.spiders'

DEFAULT_ITEM_CLASS = 'scadenze_fiscali.items.ScadenzeFiscaliItem'

USER_AGENT = 'Scrapy (http://www.scrapy.org)'

# Logging settings
LOG_ENABLED = True
LOG_LEVEL = 'DEBUG'
LOG_ENCODING = 'utf-8'
LOG_FILE = 'result/scraping.log'
