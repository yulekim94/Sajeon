import requests
from bs4 import BeautifulSoup

# def C_search(w):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     url = 'https://dic.daum.net/search.do?q='+w+'&dic=ch'
#     data = requests.get(url, headers=headers)
#     soup = BeautifulSoup(data.text, 'html.parser')
#     div_word = soup.find("div", attrs ={'data-target': 'word'})
#     if 'tit_cleansch' in str(soup):
#         box_word_bold = div_word.select_one('div.search_box > div.cleanword_type > div.search_cleanword > strong.tit_cleansch > a')
#         href = box_word_bold.get('href')
#         if 'kcw' in href:
#             a = href.find('kcw')
#             first_num = href[a+3:a+12]
#             b = href.find('kcu')
#             second_num = href[b + 3:b + 12]
#             definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=kcw' + first_num + '&supid=kcu' + second_num + '&suptype=KOREA_CK'
#             print(definition_url)
#         else:
#             a = href.find('ckw')
#             first_num = href[a + 3: a + 12]
#             b = href.find('cku')
#             second_num = href[b + 3:b + 12]
#             definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=ckw' + first_num + '&supid=cku' + second_num + '&suptype=KOREA_CK'
#             print(definition_url)
#     else:
#         box_word = div_word.select_one('div.search_box > div.search_type > div.search_word > strong.tit_searchword > a')
#         href = box_word.get('href')
#         if 'kcw' in href:
#             a = href.find('kcw')
#             first_num = href[a+3:a+12]
#             b = href.find('kcu')
#             second_num = href[b + 3:b + 12]
#             definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=kcw' + first_num + '&supid=kcu' + second_num + '&suptype=KOREA_CK'
#             print(definition_url)
#         else:
#             a = href.find('ckw')
#             first_num = href[a + 3: a + 12]
#             b = href.find('cku')
#             second_num = href[b + 3:b + 12]
#             definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=ckw' + first_num + '&supid=cku' + second_num + '&suptype=KOREA_CK'
#             print(definition_url)

# def J_search(w):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     url = 'https://dic.daum.net/search.do?q='+w+'&dic=jp'
#     data = requests.get(url, headers=headers)
#     soup = BeautifulSoup(data.text, 'html.parser')
#     div_word = soup.find("div", attrs={'class' : 'card_word'})
#     if 'card_word' in str(soup):
#         if 'tit_cleansch' in str(soup):
#             box_word_bold = div_word.select_one('div.search_box > div.cleanword_type > div.search_cleanword > strong.tit_cleansch > a')
#             href = box_word_bold.get('href')
#             if 'kjw' in href:
#                 a = href.find('kjw')
#                 first_num = href[a+3:a+12]
#                 b = href.find('kju')
#                 second_num = href[b + 3:b + 12]
#                 definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=kjw' + first_num + '&supid=kju' + second_num + '&suptype=KUMSUNG_KJ'
#                 print (definition_url)
#             else:
#                 a = href.find('jkw')
#                 first_num = href[a + 3: a + 12]
#                 b = href.find('jku')
#                 second_num = href[b + 3:b + 12]
#                 definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=jkw' + first_num + '&supid=jku' + second_num + '&suptype=KUMSUNG_KJ'
#                 print (definition_url)
#         else:
#             if 'search_box' in str(soup):
#                 box_word = div_word.select_one('div.search_box > div.search_type > div.search_word > strong.tit_searchword > a')
#                 href = box_word.get('href')
#                 if 'kjw' in href:
#                     a = href.find('kjw')
#                     first_num = href[a+3:a+12]
#                     b = href.find('kju')
#                     second_num = href[b + 3:b + 12]
#                     definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=kjw' + first_num + '&supid=kju' + second_num + '&suptype=KUMSUNG_KJ'
#                     print(definition_url)
#                 else:
#                     a = href.find('jkw')
#                     first_num = href[a + 3: a + 12]
#                     b = href.find('jku')
#                     second_num = href[b + 3:b + 12]
#                     definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=jkw' + first_num + '&supid=jku' + second_num + '&suptype=KUMSUNG_KJ'
#                     print(definition_url)
#             else:
#                 a = url.find('kjw')
#                 first_num = url[a + 3:a + 12]
#                 second_num = soup.find("div", attrs={'class': 'box_word'}).get('data-supid')[3:12]
#                 definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=kjw' + first_num + '&supid=kju' + second_num + '&suptype=KUMSUNG_KJ'
#                 print(definition_url)
#     else:
#         if 'PUBLIC' in str(soup):
#             a = str(soup.select('meta')[3].get('content'))
#             b = a.find('kjw')
#             first_num = a[b + 3:b + 12]
#             c = a.find('kju')
#             second_num = a[c + 3:c + 12]
#             definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=kjw' + first_num + '&supid=kju' + second_num + '&suptype=KUMSUNG_KJ'
#             print(definition_url)
#         else:
#             No_J = '無 in 日'
#             return No_J




# def K_search(w):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     url = 'https://dic.daum.net/search.do?q='+w+'&dic=hanja'
#     data = requests.get(url, headers=headers)
#     soup = BeautifulSoup(data.text, 'html.parser')
#     div_word= soup.find("div", attrs={'data-target': 'word'})
#     a=div_word.select_one('div.search_box > div.search_type > div.search_word > strong.tit_searchword >a')
#     href = a.get('href')
#     a = href.find('kkw')
#     first_num = href[a+3:a+12]
#     b = href.find('kku')
#     second_num=href[b+3:b+12]
#     defintion_url = 'https://dic.daum.net/word/view_supword.do?wordid=kkw'+first_num+'&supid=kku'+second_num+'&suptype=KOREA_KK'
#     print(defintion_url)



# def E_search(w):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     url = 'https://dic.daum.net/search.do?q='+w
#     data = requests.get(url, headers=headers)
#     soup = BeautifulSoup(data.text, 'html.parser')
#     div_eng = soup.find("div", attrs ={'data-tiara-layer':'word eng'})
#     if 'word eng' not in str(soup):
#         No_E = '無 in 英'
#         return No_E
#     else:
#         if 'txt_cleansch' in str(div_eng):
#             box_eng_bold=soup.find("a", attrs={'class': 'txt_cleansch'})
#             href = box_eng_bold.get('href')
#             url2 = 'https://dic.daum.net/'+href
#             data2 = requests.get(url2, headers=headers)
#             soup2 = BeautifulSoup(data2.text, 'html.parser')
#             a = url2.find('ekw')
#             first_num = url2[a+3:a+12]
#             b= soup2.select_one('div.detail_cont > div.cont_left > div.card_word > div.box_word')
#             c = b.get('data-supid')
#             second_num = c[3:15]
#             definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=ekw'+first_num+'&supid=eku'+second_num+'&suptype=KUMSUNG_KE'
#             return E_def_results(definition_url)
#         else:
#             box_eng = div_eng.select_one('div.search_box > div.search_type > div.search_word > strong.tit_searchword >a')
#             href = box_eng.get('href')
#             url2 = 'https://dic.daum.net/'+href
#             data2 = requests.get(url2, headers=headers)
#             soup2 = BeautifulSoup(data2.text, 'html.parser')
#             a = url2.find('kew')
#             first_num = url2[a+3:a+12]
#             b= soup2.select_one('div.detail_cont > div.cont_left > div.card_word > div.box_word')
#             c = b.get('data-supid')
#             second_num = c[3:15]
#             definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=kew'+first_num+'&supid=keu'+second_num+'&suptype=KUMSUNG_KE'
#             return E_def_results(definition_url)
#

def E_search(w):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = 'https://dic.daum.net/search.do?q='+w
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    div_eng = soup.find("div", attrs ={'data-tiara-layer':'word eng'})
    if 'word eng' in str(soup):
        if 'txt_cleansch' in str(div_eng):
            box_eng_bold=soup.find("a", attrs={'class': 'txt_cleansch'})
            href = box_eng_bold.get('href')
            url2 = 'https://dic.daum.net/'+href
            data2 = requests.get(url2, headers=headers)
            soup2 = BeautifulSoup(data2.text, 'html.parser')
            a = url2.find('ekw')
            first_num = url2[a+3:a+12]
            b= soup2.select_one('div.detail_cont > div.cont_left > div.card_word > div.box_word')
            c = b.get('data-supid')
            second_num = c[3:15]
            definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=ekw'+first_num+'&supid=eku'+second_num+'&suptype=KUMSUNG_KE'
            print (definition_url)
        else:
            box_eng = div_eng.select_one('div.search_box > div.search_type > div.search_word > strong.tit_searchword >a')
            href = box_eng.get('href')
            url2 = 'https://dic.daum.net/'+href
            data2 = requests.get(url2, headers=headers)
            soup2 = BeautifulSoup(data2.text, 'html.parser')
            a = url2.find('kew')
            first_num = url2[a+3:a+12]
            b= soup2.select_one('div.detail_cont > div.cont_left > div.card_word > div.box_word')
            c = b.get('data-supid')
            second_num = c[3:15]
            definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=kew'+first_num+'&supid=keu'+second_num+'&suptype=KUMSUNG_KE'
            print (definition_url)
    else:
        No_E = '無 in 英'
        print (No_E)
w = '사전'
E_search(w)