import requests
from bs4 import BeautifulSoup

def search_word(a):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = 'https://dic.daum.net/search.do?q='+ a +'&dic=ch'
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    div_meaning = soup.find("div", attrs ={'data-target' : 'mean'})
    a_link = div_meaning.select_one('div.search_box > div.search_type > div.search_word > strong.tit_searchword >a')
    href = a_link.get('href')
    a = href.find('ckw')
    first_num = href[a+3: a+12]
    b = href.find('cku')
    second_num = href[b+3:b+12]
    definition_url =  'https://dic.daum.net/word/view_supword.do?wordid=ckw'+first_num+'&supid=cku'+second_num+'&suptype=KOREA_CK'
    print(definition_url)



         