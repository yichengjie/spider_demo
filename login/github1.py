'''
Created on Dec 16, 2018

@author: yicj
'''
import requests
from bs4 import BeautifulSoup
from twisted.spread.pb import respond



class LoginGithub(object):
    def __init__(self, *args, **kwargs):
        object.__init__(self, *args, **kwargs)
        self.login_url = 'https://github.com/session'
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"  
        }
    
    def get_token_cookies(self):
        login_url = 'https://github.com/login' 
        r1 = requests.get(login_url)
        soup = BeautifulSoup(r1.text,features='lxml')
        token = soup.find(name='input', attrs={'name':'authenticity_token'}).get('value') 
        cookies = r1.cookies.get_dict()
        return token ,cookies
    
    def login(self):
        token, cookies = self.get_token_cookies()
        payload = {
            'commit':'Sigin in',
            'utf8':'%E2%9C%93',
            'authenticity_token':token,
            'login':'626659321@qq.com',
            'password':''
        }
        resp = requests.post(self.login_url,
           data=payload,cookies=cookies
        )
        #print(resp.content)
        with open('login.html','w',encoding='utf-8') as fout:
            fout.write(resp.text)
        return resp.cookies.get_dict()
        
    def chk_myinfo(self):
        login_cookies = self.login()
        print(login_cookies)
        url = 'https://github.com/yichengjie'
        resp = requests.get(url,cookies=login_cookies)
        
        with open('myinfo.html','w',encoding='utf-8') as fout:
            fout.write(resp.text)
        
        #print(resp.text)


if __name__ == '__main__':
    LoginGithub().login()
