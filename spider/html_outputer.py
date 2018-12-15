'''
Created on Dec 15, 2018

@author: yicj
'''


class HtmlOutputer(object):
    def __init__(self, *args, **kwargs):
        object.__init__(self, *args, **kwargs)
        self.datas = []
    
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self):
        with open('output.txt','w',encoding='utf-8') as fout:
            for data in self.datas:
                title = data['title']
                print('title : ' , title)
                summary = data['summary']
                url = data['url']
                msg = 'title : % s ,url: %s , summary :%s\n' %(title, url,summary)
                fout.write(msg)
            
    
    



