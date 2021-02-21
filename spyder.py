import urllib.parse
import scrapy
import os

class RetroSpider(scrapy.Spider):
  name = 'retroarch'

  def start_requests(self):
    url = 'http://thumbnails.libretro.com/'
    yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
    consoles = response.xpath('//pre/a/@href').extract()
    consoles.pop(0)
    consoles = consoles[:len(consoles)-4]
    for console in consoles:
      url = response.urljoin(console)
      yield scrapy.Request(url=url, callback=self.parse_type, meta={'console': urllib.parse.unquote(console[:-1])})

  def parse_type(self, response):
    type_art = response.xpath('//pre/a/@href').extract()[1]
    url = response.urljoin(type_art)
    meta = response.meta
    yield scrapy.Request(url=url, callback=self.parse_console, meta=meta)

  def parse_console(self, response):
    console = response.meta['console']
    file_name = 'games_lists/' + console + '.txt'
    open(file_name, 'w')
    names_enconded = response.xpath('//pre/a/@href').extract()
    if names_enconded:
      names_enconded.pop(0)
    for name_encoded in names_enconded:
      full_name = urllib.parse.unquote(name_encoded)
      name, file_extension = os.path.splitext(full_name)
      with open(file_name, 'a') as f:
        f.write(name + '\n')
        f.close()
