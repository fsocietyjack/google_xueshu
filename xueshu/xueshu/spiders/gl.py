import scrapy
import time


class GlSpider(scrapy.Spider):
    name = 'gl'
    allowed_domains = ['lanfanshu.cn']
    start_urls = [
        'https://scholar.lanfanshu.cn/scholar?start=550&hl=zh-CN&as_sdt=2005&sciodt=0,5&cites=8493427109448629428&scipsc=']
        # https://scholar.lanfanshu.cn/scholar?start=0&hl=zh-TW&as_sdt=2005&sciodt=0,5&cites=8493427109448629428

    def parse(self, response):
        if response.status == 200:
            links = response.xpath(
                '//*[@id="gs_res_ccl_mid"]/div/div[@class="gs_ggs gs_fl"]//a/span[contains(text(), "PDF")]/../@href').extract()
            # print(len(links), links)

            yield {'url': [[i] for i in links]}
            # for link in links:

            #  下一页
            next_page = response.xpath('//*[@id="gs_n"]/center/table//tr/td[12]/a/@href').extract_first()
            if next_page:
                # time.sleep(2)
                url = "https://scholar.lanfanshu.cn" + next_page
                yield scrapy.Request(url=url, callback=self.parse)
            # 被引用的
            next_linsk = response.xpath('//*[@id="gs_res_ccl_mid"]/div//div[@class="gs_fl"]/a[3]/@href').extract()
            # print(len(next_linsk), next_linsk)
            for link in next_linsk:
                # time.sleep()
                url = "https://scholar.lanfanshu.cn" + link
                yield scrapy.Request(url=url, callback=self.parse)
