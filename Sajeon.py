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
    result = list()
    c_result = C_search(search_receive)
    print(c_result)
    result.append(c_result)
    j_result = J_search(search_receive)
    result.append(j_result)
    print(j_result)
    k_result = K_search(search_receive)
    result.append(k_result)
    print(k_result)
    e_result = E_search(search_receive)
    result.append(e_result)
    print(e_result)
    return jsonify({'result': 'success', 'msg' :'Post가 완료', 'data': result})

@app.route('/definition', methods=['GET'])
def definition():
    search_receive = request.form['search_give']
    print(search_receive)
    return jsonify({'result': 'success', 'msg': 'Get이 완료'})


def C_search(w):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = 'https://dic.daum.net/search.do?q='+w+'&dic=ch'
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    div_word = soup.find("div", attrs ={'data-target': 'word'})
    if 'data-target' not in str(soup):
        No_C ='無 in 中'
        return No_C
    else:
        if 'tit_cleansch' in str(soup):
            box_word_bold = div_word.select_one('div.search_box > div.cleanword_type > div.search_cleanword > strong.tit_cleansch > a')
            href = box_word_bold.get('href')
            if 'kcw' in href:
                a = href.find('kcw')
                first_num = href[a+3:a+12]
                b = href.find('kcu')
                second_num = href[b + 3:b + 12]
                definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=kcw' + first_num + '&supid=kcu' + second_num + '&suptype=KOREA_CK'
                return C_def_results(definition_url)
            else:
                a = href.find('ckw')
                first_num = href[a + 3: a + 12]
                b = href.find('cku')
                second_num = href[b + 3:b + 12]
                definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=ckw' + first_num + '&supid=cku' + second_num + '&suptype=KOREA_CK'
                return C_def_results(definition_url)
        else:
            box_word = div_word.select_one('div.search_box > div.search_type > div.search_word > strong.tit_searchword > a')
            href = box_word.get('href')
            if 'kcw' in href:
                a = href.find('kcw')
                first_num = href[a+3:a+12]
                b = href.find('kcu')
                second_num = href[b + 3:b + 12]
                definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=kcw' + first_num + '&supid=kcu' + second_num + '&suptype=KOREA_CK'
                return C_def_results(definition_url)
            else:
                a = href.find('ckw')
                first_num = href[a + 3: a + 12]
                b = href.find('cku')
                second_num = href[b + 3:b + 12]
                definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=ckw' + first_num + '&supid=cku' + second_num + '&suptype=KOREA_CK'
                return C_def_results(definition_url)


def J_search(w):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = 'https://dic.daum.net/search.do?q='+w+'&dic=jp'
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    div_word = soup.find("div", attrs={'class' : 'card_word'})
    if 'card_word' in str(soup):
        if 'tit_cleansch' in str(soup):
            box_word_bold = div_word.select_one('div.search_box > div.cleanword_type > div.search_cleanword > strong.tit_cleansch > a')
            href = box_word_bold.get('href')
            if 'kjw' in href:
                a = href.find('kjw')
                first_num = href[a+3:a+12]
                b = href.find('kju')
                second_num = href[b + 3:b + 12]
                definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=kjw' + first_num + '&supid=kju' + second_num + '&suptype=KUMSUNG_KJ'
                return J_def_results(definition_url)
            else:
                a = href.find('jkw')
                first_num = href[a + 3: a + 12]
                b = href.find('jku')
                second_num = href[b + 3:b + 12]
                definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=jkw' + first_num + '&supid=jku' + second_num + '&suptype=KUMSUNG_KJ'
                return J_def_results(definition_url)
        else:
            if 'search_box' in str(soup):
                box_word = div_word.select_one('div.search_box > div.search_type > div.search_word > strong.tit_searchword > a')
                href = box_word.get('href')
                if 'kjw' in href:
                    a = href.find('kjw')
                    first_num = href[a+3:a+12]
                    b = href.find('kju')
                    second_num = href[b + 3:b + 12]
                    definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=kjw' + first_num + '&supid=kju' + second_num + '&suptype=KUMSUNG_KJ'
                    return J_def_results(definition_url)
                else:
                    a = href.find('jkw')
                    first_num = href[a + 3: a + 12]
                    b = href.find('jku')
                    second_num = href[b + 3:b + 12]
                    definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=jkw' + first_num + '&supid=jku' + second_num + '&suptype=KUMSUNG_KJ'
                    return J_def_results(definition_url)
            else:
                a = url.find('kjw')
                first_num = url[a + 3:a + 12]
                second_num = soup.find("div", attrs={'class': 'box_word'}).get('data-supid')[3:12]
                definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=kjw' + first_num + '&supid=kju' + second_num + '&suptype=KUMSUNG_KJ'
                return J_def_results(definition_url)
    else:
        if 'PUBLIC' in str(soup):
            if 'PUBLIC' in str(soup):
                a = str(soup.select('meta')[3].get('content'))
                b = a.find('kjw')
                first_num = a[b + 3:b + 12]
                c = a.find('kju')
                second_num = a[c + 3:c + 12]
                definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=kjw' + first_num + '&supid=kju' + second_num + '&suptype=KUMSUNG_KJ'
                return J_def_results(definition_url)
            else:
                No_J = '無 in 日'
                return No_J

def K_search(w):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = 'https://dic.daum.net/search.do?q='+w+'&dic=hanja'
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    div_word= soup.find("div", attrs={'data-target': 'word'})
    if 'data-target' not in str(soup):
        No_K = '無 in 韓'
        return No_K
    else:
        a=div_word.select_one('div.search_box > div.search_type > div.search_word > strong.tit_searchword >a')
        href = a.get('href')
        a = href.find('kkw')
        first_num = href[a+3:a+12]
        b = href.find('kku')
        second_num=href[b+3:b+12]
        definition_url = 'https://dic.daum.net/word/view_supword.do?wordid=kkw'+first_num+'&supid=kku'+second_num+'&suptype=KOREA_KK'
        return K_def_results(definition_url)

def E_search(w):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = 'https://dic.daum.net/search.do?q='+w
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    div_eng = soup.find("div", attrs ={'data-tiara-layer':'word eng'})
    if 'word eng' not in str(soup):
        No_E = '無 in 英'
        return No_E
    else:
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
            return E_def_results(definition_url)
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
            return E_def_results(definition_url)

def C_def_results(u):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = u
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    defs = soup.find_all("p", attrs={'class':'desc_item'})
    exams = soup.find_all("p", attrs={'class':'desc_ex'})
    if 'tit_ex' in str(soup):
        if "strong" in str(soup):
            C_word_class = soup.find("strong", attrs={'class': 'tit_ex'}).text
            if defs is not None:
                for i in defs:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    C_def = "".join(b)
            else:
                C_def =''
            if exams is not None:
                for i in exams:
                    d = i.text.replace("듣기", "").strip()
                    e = list(d)
                    C_exam = "".join(e)
            else:
                C_exam =''
            C_doc = {'C_Word_Class':C_word_class, 'C_Def': C_def, 'C_Exam': C_exam}
            return C_doc
        else:
            if defs is not None:
                for i in defs:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    C_def = "".join(b)
            else:
                C_def =''
            if exams is not None:
                for i in exams:
                    d = i.text.replace("듣기", "").strip()
                    e = list(d)
                    C_exam = "".join(e)
            else:
                C_exam =''
            C_doc = {'C_Def': C_def, 'C_Exam': C_exam}
            return C_doc
    else:
        if "strong" in str(soup):
            C_word_class = soup.find("strong", attrs={'class': 'tit_ex'}).text
            if defs is not None:
                for i in defs:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    C_def = "".join(b)
            else:
                C_def =''
            if exams is not None:
                for i in exams:
                    d = i.text.replace("듣기", "").strip()
                    e = list(d)
                    C_exam = "".join(e)
            else:
                C_exam=''
            C_doc = {'C_Word_Class': C_word_class, 'C_Def': C_def, 'C_Exam': C_exam}
            return C_doc
        else:
            if defs is not None:
                for i in defs:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    C_def = "".join(b)
            else:
                C_def =''
            if exams is not None:
                for i in exams:
                    d = i.text.replace("듣기", "").strip()
                    e = list(d)
                    C_exam = "".join(e)
            else:
                C_exam=''
            C_doc = {'C_Def': C_def, 'C_Exam': C_exam}
            return C_doc



def J_def_results(u):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = u
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    defs = soup.find_all("p", attrs={'class':'desc_item'})
    exams = soup.find_all("p", attrs={'class':'desc_ex'})
    if 'tit_ex' in str(soup):
        if "strong" in str(soup):
            J_word_class = soup.find("strong", attrs={'class': 'tit_ex'}).text
            if defs is not None:
                for i in defs:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    J_def = "".join(b)
            else:
                J_def =''
            if exams is not None:
                for i in exams:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    J_exam = "".join(b)
            else:
                J_exam =''
            J_doc = {'J_Word_Class': J_word_class, 'J_Def': J_def, 'J_Exam': J_exam}
            return J_doc
        else:
            if defs is not None:
                for i in defs:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    J_def = "".join(b)
            else:
                J_def =''
            if exams is not None:
                for i in exams:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    J_exam = "".join(b)
            else:
                J_exam =''
            J_doc = {'J_Def': J_def, 'J_Exam': J_exam}
            return J_doc

    else:
        if "strong" in str(soup):
            J_word_class = soup.find("strong", attrs={'class': 'tit_ex'}).text
            if defs is not None:
                for i in defs:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    J_def = "".join(b)
            else:
                J_def =''
            if exams is not None:
                for i in exams:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    J_exam = "".join(b)
            else:
                J_exam =''
            J_doc = {'J_Word_Class': J_word_class, 'J_Def': J_def, 'J_Exam': J_exam}
            return J_doc
        else:
            if defs is not None:
                for i in defs:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    J_def = "".join(b)
            else:
                J_def =''
            if exams is not None:
                for i in exams:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    J_exam = "".join(b)
            else:
                J_exam =''
            J_doc = {'J_Def': J_def, 'J_Exam': J_exam}
            return J_doc


def K_def_results(u):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = u
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    defs = soup.find_all("p", attrs={'class':'desc_item'})
    exams = soup.find_all("p", attrs={'class':'desc_ex'})
    if 'tit_ex' in str(soup):
        if "strong" in str(soup):
            K_word_class = soup.find("strong", attrs={'class': 'tit_ex'}).text
            if defs is not None:
                for i in defs:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    K_def = "".join(b)
            else:
                K_def =''
            if exams is not None:
                for i in exams:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    K_exam = "".join(b)
            else:
                K_exam =''
            K_doc = {'K_Word_Class': K_word_class, 'K_Def': K_def, 'K_Exam': K_exam}
            return K_doc
        else:
            if defs is not None:
                for i in defs:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    K_def = "".join(b)
            else:
                K_def =''
            if exams is not None:
                for i in exams:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    K_exam = "".join(b)
            else:
                K_exam =''
            K_doc = {'K_Def': K_def, 'K_Exam': K_exam}
            return K_doc
    else:
        if "strong" in str(soup):
            K_word_class = soup.find("strong", attrs={'class': 'tit_ex'}).text
            if defs is not None:
                for i in defs:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    K_def = "".join(b)
            else:
                K_def =''
            if exams is not None:
                for i in exams:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    K_exam = "".join(b)
            else:
                K_exam=''
            K_doc = {'K_Word_Class': K_word_class, 'K_Def': K_def, 'K_Exam': K_exam}
            return K_doc
        else:
            if defs is not None:
                for i in defs:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    K_def = "".join(b)
            else:
                K_def =''
            if exams is not None:
                for i in exams:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    K_exam = "".join(b)
            else:
                K_exam =''
            K_doc = {'K_Def': K_def, 'K_Exam': K_exam}
            return K_doc

def E_def_results(u):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = u
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    defs = soup.find_all("p", attrs={'class':'desc_item'})
    exams = soup.find_all("p", attrs={'class':'desc_ex'})
    if 'tit_ex' in str(soup):
        if "strong" in str(soup):
            E_word_class = soup.find("strong", attrs={'class': 'tit_ex'}).text
            if defs is not None:
                for i in defs:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    E_def = "".join(b)
            else: E_def =''
            if exams is not None:
                for i in exams:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    E_exam = "".join(b)
            else: E_exam =''
            E_doc = {'E_Word_Class': E_word_class, 'E_Def': E_def, 'E_Exam': E_exam}
            return E_doc
        else:
            if defs is not None:
                for i in defs:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    E_def = "".join(b)
            else: E_def =''
            if exams is not None:
                for i in exams:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    E_exam = "".join(b)
            else: E_exams =''
            E_doc = {'E_Def': E_def, 'E_Exam': E_exam}
            return E_doc
    else:
        if "strong" in str(soup):
            E_word_class = soup.find("strong", attrs={'class': 'tit_ex'}).text
            if defs is not None:
                for i in defs:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    E_def = "".join(b)
            else: E_def =''
            if exams is not None:
                for i in exams:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    E_exam = "".join(b)
            else: E_exam =''
            E_doc = {'E_Word_Class': E_word_class, 'E_Def': E_def, 'E_Exam': E_exam}
            return E_doc
        else:
            if defs is not None:
                for i in defs:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    E_def = "".join(b)
            else:
                E_def = ''
            for i in exams:
                a = i.text.replace("듣기", "").strip()
                b = list(a)
                E_exam = "".join(b)
            else:
                E_def = ''
            E_doc = {'E_Def': E_def, 'E_Exam': E_exam}
            return E_doc

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)