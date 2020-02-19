import os
import urllib.request
import scrapy

class MySpider(scrapy.spiders.Spider):
    #���Ϊ��W�r�A�C�Ӫ��Υ��������P���W�r
    name = 'mySpider'
    allowed_domains = ['www.sdibt.edu.cn']
    #�ݪ������_�l�����A�����O�C���A�i�H�]�t�h��url
    start_urls = ['http://www.sdibt.edu.cn/info/1026/11238.htm']

    #�w��C�Ӫ����������A�N�۰ʩI�s�U���o�Ӥ�k
    def parse(self, response):
        self.downloadWebpage(response)
        self.downloadImages(response)

        #�ˬd�������W�s���A���~�򪦨�
        hxs = scrapy.Selector(response)        
        sites = hxs.xpath('//ul/li')
        for site in sites:
            link = site.xpath('a/@href').extract()[0]
            if link == '#':
                continue
            #��۹��}�ഫ�������}
            elif link.startswith('..'):
                next_url = os.path.dirname(response.url)
                next_url += '/'+link
            else:
                next_url = link
            #����Request����A�ë��w�^�I���
            yield scrapy.Request(url=next_url, callback=self.parse_item)

    #�^�I��ơA��_�l�������C�ӶW�s�����@��
    def parse_item(self, response):
        self.downloadWebpage(response)
        self.downloadImages(response)

    #�U���ثe�����Ҧ����Ϥ�
    def downloadImages(self, response):
        hxs = scrapy.Selector(response)
        images = hxs.xpath('//img/@src').extract()
        for image_url in images:
            imageFilename = image_url.split('/')[-1]
            if os.path.exists(imageFilename):
                continue
            #��۹��}�ഫ�������}
            if image_url.startswith('..'):
                image_url = os.path.dirname(response.url)+'/'+image_url
            #�}�Һ����Ϥ�
            fp = urllib.request.urlopen(image_url)
            #�إߥ��a�Ϥ���
            with open(imageFilename,'wb') as f:
                f.write(fp.read())
            fp.close()
            
    #�N�������e�x�s�����a�ɮ�
    def downloadWebpage(self, response):
        filename = response.url.split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)
