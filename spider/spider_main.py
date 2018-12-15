'''
Created on Dec 15, 2018
@author: yicj
'''
from spider import url_manager, html_downloader, html_parser,\
    html_outputer

class SpiderMain(object):
    
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            try:
                html_content = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 20:
                    break
                count += 1 
            except Exception as e:
                print("craw index: %d, url:%s failed !" % (count,new_url),e)
            else:
                print("craw index: %d, url: %s success !" % (count,new_url))  
        self.outputer.output_html()

if __name__ == '__main__':
    
    root_url = "https://baike.baidu.com/item/Python/407313" 
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    pass