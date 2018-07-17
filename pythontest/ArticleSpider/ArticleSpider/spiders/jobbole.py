"""
非结构性的数据组织成一种结构性的数据
爬虫程序的入口
资料：https://scrapy-chs.readthedocs.io/zh_CN/1.0/intro/tutorial.html
爬取网站：
http://blog.jobbole.com/112038/
慕课网学习笔记
"""
import scrapy
import re
import datetime
from scrapy.http import Request
from urllib import parse
from ArticleSpider.items import JoBBoleArticleItem
from ArticleSpider.utils.common import get_md5

"""
继承scrapy的Spider类
"""


class JobboleSpider(scrapy.Spider):
    ####用于区别Spider，必须是唯一的
    name = "jobbole"
    """
    allowed_domain:代表可爬取的域名列表，当爬取的url不属于该域名下时，将不再爬取
    可选项，不一定要必须设置，但是如果设置了，如果爬取的url不属于该域名将被过滤
    """
    allowed_domains = ["blog.jobbole.com"]
    ###单个文章
    # start_urls = ["http://blog.jobbole.com/112038/"]
    """
    初始爬取的URl
    """
    start_urls = ["http://blog.jobbole.com/all-posts/"]
    """
    单个文章如何抓取
    """
    ####爬虫启动后会将爬取网页的内容通过response返回
    # def parse(self, response):
    #     ###获取xpath对象
    #     ####可以在网页的调试模式下 选中元素 使用右键copy xpath
    #     title_selector = response.xpath('//*[@id="post-112038"]/div[1]/h1')
    #     title = title_selector.extract()[0]
    #     time_selector = response.xpath('//*[@id="post-112038"]/div[2]/p/text()[1]')
    #     time = time_selector.extract()[0].strip().replace(".","")
    #     ####1.首先使用浏览器copy path，然后修改
    #     good=response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()').extract()[0]
    #     ####2.使用css选择器来提取元素
    #     ####按照clss开头需要使用.开头，取其下的子元素 需要用空格做分隔
    #     ####选择属性 需要用::
    #     title_css=response.css('.entry-header h1::text').extract()
    #     pass
    """
    Scrapy的方法，负责将爬取的页面数据包装成response
    Scrapy方法会为start_url中的所有地址执行一遍
    Scrapy具有网页追踪机制，当我们在parse提供一个yield的请求后将会不断请求传入的url，并执行回调函数进行解析
    1.获取文章中的所有url并交给解析器进行下载（使用scrapy的request类）
    2.能够获取到下一个url 交给scrapy
    3.Request的meta参数，可以将传递参数，它将参数保存到Response中，并且交给callback
    """

    def parse(self, response):
        """
        爬取初始页面所有符合条件的url
        包装成Request，并且不断执行parse_detail方法保存数据
        """
        # 返回一个selector
        # post_urls = response.css("#archive .floated-thumb .post-thumb a::attr(href)").extract()
        post_nodes = response.css("#archive .floated-thumb .post-thumb a")
        for post_node in post_nodes:
            image_url = post_node.css("img::attr(src)").extract_first("")
            # request会下载指定文章的详情页
            # 通常情况下获取到的不是完整的url，需要和域名拼接，形成完整的url
            post_url = post_node.css("::attr(href)").extract_first("")
            print("post url is :" + parse.urljoin(response.url, post_url))
            #meta配置一些参数，传递给reponse
            yield Request(url=parse.urljoin(response.url, post_url), meta={"front_image_url": image_url},
                          callback=self. parse_detail)
            # 通过两个class标签定位一个标签
        """
        reponse.css和.xPath会构建一个selector对象，Selector对象负责从网页中提取元素
        selector的extract（）方法负责提取数据
        """
        ###查找初始页面的下一页数据，继续执行parse请求，完成递归
        next_url = response.css(".next.page-numbers::attr(href)").extract_first("")
        print(next_url)
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    """
    使用浏览器生成xpath会因为选择提取的class其他页不存在而出现问题，不要提取带id的xpath
    例如//*[@id="post-112038"]
    
    将爬取到的数据保存成为Item
    """

    def parse_detail(self, response):
        article_item = JoBBoleArticleItem()

        # 通过css选择器提取字段
        ##meta字段是单独配置的
        front_image_url = response.meta.get("front_image_url", "")  # 文章封面图
        title = response.css(".entry-header h1::text").extract()[0]
        create_date = response.css("p.entry-meta-hide-on-mobile::text").extract()[0].strip().replace("·", "").strip()
        praise_nums = response.css(".vote-post-up h10::text").extract()[0]
        fav_nums = response.css(".bookmark-btn::text").extract()[0]
        match_re = re.match(".*?(\d+).*", fav_nums)
        if match_re:
            fav_nums = int(match_re.group(1))
        else:
            fav_nums = 0

        comment_nums = response.css("a[href='#article-comment'] span::text").extract()[0]
        match_re = re.match(".*?(\d+).*", comment_nums)
        if match_re:
            comment_nums = int(match_re.group(1))
        else:
            comment_nums = 0

        content = response.css("div.entry").extract()[0]

        tag_list = response.css("p.entry-meta-hide-on-mobile a::text").extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ",".join(tag_list)


        try:
            create_date = datetime.datetime.strptime(create_date, "%Y/%m/%d").date()
        except Exception as e:
            create_date = datetime.datetime.now().date()

        # ###获取xpath对象
        # ####可以在网页的调试模式下 选中元素 使用右键copy xpath
        # front_url_img=response.meta.get('front_image_url','')
        # print("front img :  " + front_url_img)
        # title = response.xpath('//div[@class="entry-header"]/h1/text()').extract_first("")
        # print("title is : "+title)
        # time_selector = response.xpath('//*[@id="post-112038"]/div[2]/p/text()[1]')
        # create_date = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().replace("·",
        #                                                                                                             "").strip()
        # ####1.首先使用浏览器copy path，然后修改
        # good = response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()').extract()[0]
        # ####2.使用css选择器来提取元素
        # ####按照clss开头需要使用.开头，取其下的子元素 需要用空格做分隔
        # ####选择属性 需要用::
        # title_css = response.css('.entry-header h1::text').extract()

        # 将数据保存到Item中

        article_item["url"] = response.url
        article_item['url_md5_id'] = get_md5(response.url)
        article_item['title'] = title
        article_item['create_date'] = create_date
        #在爬去图片时，如果配置了ImagePiple，那么会将图片地址当作数组来处理，所以需要将字符放入到数组中
        article_item['front_img_url'] = [front_image_url]
        article_item['praise_nums'] = praise_nums
        article_item['commment_nums'] = comment_nums
        # article_item['content'] = content
        # 一定要返回yield对象，数据会传入到pipline
        yield article_item
