import urllib.parse
import scrapy
import os
import re

class RetroSpider(scrapy.Spider):
  name = 'retroarch'

  def start_requests(self):
    url = 'http://thumbnails.libretro.com/'
    open("games_list.txt", 'w')
    yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
    consoles = response.xpath('//pre/a/@href').extract()
    consoles.pop(0)
    consoles = consoles[:len(consoles)-4]
    for console in consoles:
      url = response.urljoin(console)
      yield scrapy.Request(url=url, callback=self.parse_type)

  def parse_type(self, response):
    type_art = response.xpath('//pre/a/@href').extract()[1]
    url = response.urljoin(type_art)
    yield scrapy.Request(url=url, callback=self.parse_console)

  def parse_console(self, response):
    names_enconded = response.xpath('//pre/a/@href').extract()
    if names_enconded:
      names_enconded.pop(0)
    for name_encoded in names_enconded:
      full_name = urllib.parse.unquote(name_encoded)
      name, file_extension = os.path.splitext(full_name)
      with open("games_list.txt", 'a') as f:
        f.write(name + '\n')
        f.close()
