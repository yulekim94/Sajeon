import requests
from bs4 import BeautifulSoup

def definition(u):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = 'https://dic.daum.net/word/view_supword.do?wordid=kkw000063427&supid=kku000080607&suptype=KOREA_KK'
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    defs = soup.find_all("p", attrs={'class':'desc_item'})
    exams = soup.find_all("p", attrs={'class':'desc_ex'})
    if 'tit_ex' in str(soup):
        a = soup.find("strong", attrs={'class': 'tit_ex'}).text
        word_class = {'C_Word_Class': a}
        print(word_class)
        for i in defs:
            if len(i) > 0:
                a = i.text.replace("듣기", "").strip()
                b = list(a)
                c = "".join(b)
                d = {'C_def': c}
                print(d)
        for i in exams:
            a = i.text.replace("듣기", "").strip()
            b = list(a)
            c = "".join(b)
            d = {'C_exam': c}
            print(d)
    else:
        for i in defs:
            if len(i) > 0:
                a = i.text.replace("듣기", "").strip()
                b = list(a)
                c = "".join(b)
                d = {'C_def': c}
                print(d)
        for i in exams:
            a = i.text.replace("듣기", "").strip()
            b = list(a)
            c = "".join(b)
            d = {'C_exam': c}
            print(d)

#
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# url = 'https://dic.daum.net/word/view_supword.do?wordid=kkw000063427&supid=kku000080607&suptype=KOREA_KK'
# data = requests.get(url, headers=headers)
# soup = BeautifulSoup(data.text, 'html.parser')
# defs = soup.find_all("p", attrs={'class':'desc_item'})
# exams = soup.find_all("p", attrs={'class':'desc_ex'})
# #print(defs)
#
# for i in defs:
#     if len(i)>0:
#         a=i.text.replace("듣기", "").strip()
#         b= list(a)
#         c="".join(b)
#         d= {'C_def':c}
#         print(d)
# for i in exams:
#     a=i.text.replace("듣기", "").strip()
#     b=list(a)
#     c = "".join(b)
#     d = {'C_exam': c}
#     print(d)
#
