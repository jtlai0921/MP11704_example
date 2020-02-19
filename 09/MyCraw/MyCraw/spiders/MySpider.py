import os
import urllib.request
import scrapy

class MySpider(scrapy.spiders.Spider):
    #爬蟲的名字，每個爬蟲必須有不同的名字
    name = 'mySpider'
    allowed_domains = ['www.sdibt.edu.cn']
    #待爬取的起始頁面，必須是列穰，可以包含多個url
    start_urls = ['http://www.sdibt.edu.cn/info/1026/11238.htm']

    #針對每個爬取的頁面，將自動呼叫下面這個方法
    def parse(self, response):
        self.downloadWebpage(response)
        self.downloadImages(response)

        #檢查頁面的超連結，並繼續爬取
        hxs = scrapy.Selector(response)        
        sites = hxs.xpath('//ul/li')
        for site in sites:
            link = site.xpath('a/@href').extract()[0]
            if link == '#':
                continue
            #把相對位址轉換成絕對位址
            elif link.startswith('..'):
                next_url = os.path.dirname(response.url)
                next_url += '/'+link
            else:
                next_url = link
            #產生Request物件，並指定回呼函數
            yield scrapy.Request(url=next_url, callback=self.parse_item)

    #回呼函數，對起始頁面的每個超連結有作用
    def parse_item(self, response):
        self.downloadWebpage(response)
        self.downloadImages(response)

    #下載目前頁面所有的圖片
    def downloadImages(self, response):
        hxs = scrapy.Selector(response)
        images = hxs.xpath('//img/@src').extract()
        for image_url in images:
            imageFilename = image_url.split('/')[-1]
            if os.path.exists(imageFilename):
                continue
            #把相對位址轉換成絕對位址
            if image_url.startswith('..'):
                image_url = os.path.dirname(response.url)+'/'+image_url
            #開啟網頁圖片
            fp = urllib.request.urlopen(image_url)
            #建立本地圖片檔
            with open(imageFilename,'wb') as f:
                f.write(fp.read())
            fp.close()
            
    #將網頁內容儲存為本地檔案
    def downloadWebpage(self, response):
        filename = response.url.split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)
