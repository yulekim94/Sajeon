import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://dic.daum.net/word/view_supword.do?wordid=kkw000063427&supid=kku000080607&suptype=KOREA_KK'
data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
contents = soup.find_all('p')
defs = soup.find_all("p", attrs={'class':'desc_item'})
exams = soup.find_all("p", attrs={'class':'desc_ex'})
n=0

if 'tit_ex' in str(soup):
    for i in defs:
        if len(i)>0:
            n+=1
            d=i.text.replace("듣기", "").strip()
            print(n,d)
            print('--------------------------------')
    for i in exams:
        e=i.text.replace("듣기", "").strip()
        print(e)
else:
    for i in defs:
        if len(i)>0:
            n+=1
            d=i.text.replace("듣기", "").strip()
            print(n,d)
            print('--------------------------------')
    for i in exams:
        e=i.text.replace("듣기", "").strip()
        print(e)


#
# if 'tit_ex' in str(soup):
#     def_t=soup.find("strong", attrs={'class':'tit_ex'}).text
#     print(def_t)
#     for i in contents:
#         a= i.text.replace("듣기", "").strip()
#         print(a)
# else:
#     for i in contents:
#         a= i.text.replace("듣기", "").strip()
#         print(a)