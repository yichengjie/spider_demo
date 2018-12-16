'''
Created on Dec 16, 2018

@author: yicj
'''
import re

str1 = 'imooc python'

pa = re.compile(r'imooc')

ma = pa.match('imooc hello world')

info = ma.group()

print(info)


