from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

@app.route('/')
def home():
    return render_template('sajeon_index.html')

@app.route('/search', methods = ['POST'])
def search():
    search_receive= request.form['search_give']
    C_search(search_receive)
    J_search(search_receive)
    K_search(search_receive)

    return jsonify({'result': 'success', 'msg' :'Post가 완료'})

@app.route('/definition', methods=['GET'])
def definition():
    search_receive = request.form['search_give']
    print(search_receive)
    return jsonify({'result': 'success', 'msg': 'Get이 완료'})

def C_search(a):
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

def J_search(a):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = 'https://dic.daum.net/search.do?q='+a+'&dic=jp'
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    div_meaning = soup.find("div", attrs={'data-target' : 'mean'})
    a_link= div_meaning.select_one('div.search_box > div.search_type > div.search_word > strong.tit_searchword >a')
    href = a_link.get('href')
    a = href.find('jkw')
    first_num = href[a+3: a+12]
    b = href.find('jku')
    second_num = href[b+3: b+12]
    definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=jkw'+first_num+'&supid=jku'+second_num+'&suptype=KUMSUNG_JK'
    print(definition_url)

def K_search(a):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = 'https://dic.daum.net/search.do?q='+a+'&dic=hanja'
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



if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)