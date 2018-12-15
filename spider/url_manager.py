'''
Created on Dec 15, 2018

@author: yicj
'''


class UrlManager(object):
    
    def __init__(self, *args, **kwargs):
        object.__init__(self, *args, **kwargs)
        self.new_urls = set()
        self.old_urls = set()
        
    
    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and not url in self.old_urls:
            self.new_urls.add(url)
    
    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
    
    
    def has_new_url(self):
        return len(self.new_urls) != 0

    
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url    
    
    
    
    
    
    
    



