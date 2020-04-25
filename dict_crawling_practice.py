import requests
from bs4 import BeautifulSoup

#str(soup)
#
def C_search(w):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = 'https://dic.daum.net/search.do?q='+w+'&dic=ch'
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    div_word = soup.find("div", attrs ={'data-target': 'word'})
    if 'tit_cleansch' in str(soup):
        box_word_bold = div_word.select_one('div.search_box > div.cleanword_type > div.search_cleanword > strong.tit_cleansch > a')
        href = box_word_bold.get('href')
        if 'kcw' in href:
            a = href.find('kcw')
            first_num = href[a+3:a+12]
            b = href.find('kcu')
            second_num = href[b + 3:b + 12]
            definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=kcw' + first_num + '&supid=kcu' + second_num + '&suptype=KOREA_CK'
            print(definition_url)
        else:
            a = href.find('ckw')
            first_num = href[a + 3: a + 12]
            b = href.find('cku')
            second_num = href[b + 3:b + 12]
            definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=ckw' + first_num + '&supid=cku' + second_num + '&suptype=KOREA_CK'
            print(definition_url)
    else:
        box_word = div_word.select_one('div.search_box > div.search_type > div.search_word > strong.tit_searchword > a')
        href = box_word.get('href')
        if 'kcw' in href:
            a = href.find('kcw')
            first_num = href[a+3:a+12]
            b = href.find('kcu')
            second_num = href[b + 3:b + 12]
            definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=kcw' + first_num + '&supid=kcu' + second_num + '&suptype=KOREA_CK'
            print(definition_url)
        else:
            a = href.find('ckw')
            first_num = href[a + 3: a + 12]
            b = href.find('cku')
            second_num = href[b + 3:b + 12]
            definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=ckw' + first_num + '&supid=cku' + second_num + '&suptype=KOREA_CK'
            print(definition_url)

def J_search(w):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = 'https://dic.daum.net/search.do?q='+w+'&dic=jp'
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    div_word = soup.find("div", attrs={'class' : 'card_word'})
    if 'tit_cleansch' in str(soup):
        box_word_bold = div_word.select_one('div.search_box > div.cleanword_type > div.search_cleanword > strong.tit_cleansch > a')
        href = box_word_bold.get('href')
        if 'kjw' in href:
            a = href.find('kjw')
            first_num = href[a+3:a+12]
            b = href.find('kju')
            second_num = href[b + 3:b + 12]
            definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=kjw' + first_num + '&supid=kju' + second_num + '&suptype=KUMSUNG_KJ'
            print(definition_url)
        else:
            a = href.find('jkw')
            first_num = href[a + 3: a + 12]
            b = href.find('jku')
            second_num = href[b + 3:b + 12]
            definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=jkw' + first_num + '&supid=jku' + second_num + '&suptype=KUMSUNG_KJ'
            print(definition_url)
    else:
        box_word = div_word.select_one('div.search_box > div.search_type > div.search_word > strong.tit_searchword > a')
        href = box_word.get('href')
        if 'kjw' in href:
            a = href.find('kjw')
            first_num = href[a+3:a+12]
            b = href.find('kju')
            second_num = href[b + 3:b + 12]
            definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=kjw' + first_num + '&supid=kju' + second_num + '&suptype=KUMSUNG_KJ'
            print(definition_url)
        else:
            a = href.find('jkw')
            first_num = href[a + 3: a + 12]
            b = href.find('jku')
            second_num = href[b + 3:b + 12]
            definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=jkw' + first_num + '&supid=jku' + second_num + '&suptype=KUMSUNG_KJ'
            print(definition_url)




def K_search(w):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = 'https://dic.daum.net/search.do?q='+w+'&dic=hanja'
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    div_meaning= soup.find("div", attrs={'data-target': 'word'})
    a_link=div_meaning.select_one('div.search_box > div.search_type > div.search_word > strong.tit_searchword >a')
    href = a_link.get('href')
    a = href.find('kkw')
    first_num = href[a+3:a+12]
    b = href.find('kku')
    second_num=href[b+3:b+12]
    defintion_url = 'https://dic.daum.net/word/view_supword.do?wordid=kkw'+first_num+'&supid=kku'+second_num+'&suptype=KOREA_KK'
    print(defintion_url)