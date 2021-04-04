# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 00:07:21 2021

@author: Irenel
"""
import re
import sys
import getopt
import fileinput
from pprint import pprint
from bs4 import BeautifulSoup
import requests
import json
#import scrapy

#url='http://pagfam.geneall.net/3418/'
#url ='http://pagfam.geneall.net/3418/pessoas.php?id=1076124'


 #url = f'http://pagfam.geneall.net/3418/pessoas_search.php?start={i}&orderby=&sort=&idx=0&search=' for i in range(0,146,30)]
#for a in range(0,146,30):
url = 'http://pagfam.geneall.net/3418/pessoas_search.php?start={}&orderby=&sort=&idx=0&search='

t_cadastro=[]
for er in range(0,146,30):
    req= requests.get(url.format(er))
#req= requests.get(url)
    req.encoding='utf-8'
  #pprint(req.text, indent=3)
#soup= BeautifulSoup(req.text,'html.parser')
    familia= re.findall(r'<title>(.*?)<\/title>', req.text)
    caso= re.findall(r'<A\s+href=(.*?id=(\d+)"?)>(.*?)<\/A>', req.text)
#casor= re.findall(r'<NOBR>((.*?)?)<\/NOBR>', req.text, flags=re.I)
    print(familia)   
    for end, id, nomes in caso:
        #print(id, nomes)
        t_cadastro.append({'Identificador':id, 'Nome':nomes})
        pprint(t_cadastro)
with open('cadastrar.json', 'w') as json_ficheiro:
    json.dump(t_cadastro, json_ficheiro, indent=3, ensure_ascii=False)
        
        
        
        
        
        
#------------------------------------------------------------------------------------------------        
#for terc, data  in casor:
#        print(data)
        #pprint(nomes.next_element)
#caso= re.findall(r'<li>(<A\s+href="(.*?id=(\d+)"?)>(.*?)<\/A><NOBR>(.*?)<\/NOBR>)<\/li>', req.text)

#fads= soup.find_all(class_='head1')
#fad= soup.find_all(class_='txt2')
#fadi= soup.find('script', text=caso)
#fadi= soup.find_all('a')
#for car in fad:
#    pprint(car)
#for ca in fads:
#      pprint(ca.next_element)
    #pprint(fad)