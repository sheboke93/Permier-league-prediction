# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 00:49:26 2017

@author: Siyuan Dang
"""

import time
import requests
from bs4 import BeautifulSoup
url = "http://www.squawka.com/match-results?2016"
page='pg'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding':'gzip',
'Connection':'close',
'Referer':'http://www.baidu.com/link?url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;amp;wd=&amp;amp;eqid=c3435a7d00006bd600000003582bfd1f'
}
for i in range(1,13):
     if i == 1:
          i=str(i)
          a=(url+page+"="+i)
          r=requests.get(url=a,headers=headers)
          html=r.content
     else:
          i=str(i)
          a=(url+page+"="+i)
          r=requests.get(url=a,headers=headers)
          html2=r.content
          html = html + html2
     #每次间隔0.5秒
     time.sleep(0.5)
#解析抓取的页面内容
lj=BeautifulSoup(html,'html.parser')      
#提取teamvs
team_vs=lj.find_all('td',attrs={'class':'fleft'})
tp=[]
for d in team_vs:
    team=d.get_text()
    tp.append(team)
#提取matchchannel
match_channel=lj.find_all('td',attrs={'class':'match-channel'})
 
hi=[]
for b in match_channel:
    score=b.get_text()
    hi.append(score)

#提取match-league
match_league=lj.find_all('td',attrs={'class':'match-league'})
 
fi=[]
for c in match_league:
    league=c.get_text()
    fi.append(league)
import pandas as pd
match_1=pd.DataFrame({'fleft':tp})
match_2=pd.DataFrame({'match-channel':hi,'match-league':fi})
print(match_1.head())
print(match_2.head())



