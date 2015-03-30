# -*- coding: utf-8 -*-

# Scrapy settings for Normandy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'Normandy'

SPIDER_MODULES = ['Normandy.spiders']
NEWSPIDER_MODULE = 'Normandy.spiders'
DEFAULT_ITEM_CLASS = 'Normandy.items.Website'
ITEM_PIPELINES = {'Normandy.pipelines.FilterWordsPipeline' : 1}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Normandy (+http://www.yourdomain.com)'
