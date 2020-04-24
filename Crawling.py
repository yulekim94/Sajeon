import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://dic.daum.net/word/view.do?wordid=ckw000022656&q=%E5%A4%A7%E5%AD%A6&supid=cku000022931',
                    headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
print(soup.select('#mArticle'))
# Cdict = soup.select('div.inner_top > ul.list_mean > li > span.txt_mean')
#
# title_word = soup.select_one('div.clean_word > h3.tit_cleanword > span.txt_cleanword').text
#
#
#
#
# def search():
#     num = 0
#     print (title_word)
#     for i in Cdict:
#         num +=1
#         Cdef = i.text
#         print(num, Cdef)


