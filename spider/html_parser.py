'''
Created on Dec 15, 2018

@author: yicj
'''
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a',href = re.compile(r'/item/*'))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls
    
    
    def _get_new_data(self, page_url, soup):
        ret_data = {'url':page_url}
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find('h1')
        ret_data['title'] = title_node.get_text()
        summary_node = soup.find('div',class_="lemma-summary").find('div',class_="para")
        ret_data['summary'] = summary_node.get_text()
       
        return ret_data
    
    
    def parse(self,page_url,html_content):
        if page_url is None or html_content is None:
            return 
        soup = BeautifulSoup(html_content,'html.parser',from_encoding='utf8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data
    
    



