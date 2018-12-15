'''
Created on Dec 15, 2018
@author: yicj
'''
import urllib.request


class HtmlDownloader(object):
    
    
    def download(self,url):
        if url is None:
            return None
        #urllib.request.urlopen(
        resp = urllib.request.urlopen(url)
        if resp.getcode() != 200:
            return None
        return resp.read()    
    



