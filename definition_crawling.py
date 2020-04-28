import requests
from bs4 import BeautifulSoup

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
            for i in defs:
                if len(i) > 0:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    C_def = "".join(b)
            for i in exams:
                d = i.text.replace("듣기", "").strip()
                e = list(d)
                C_exam = "".join(e)
            C_doc = {'C_Word_Class':C_word_class, 'C_Def': C_def, 'C_Exam': C_exam}
            return C_doc
        else:
            for i in defs:
                if len(i) > 0:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    C_def = "".join(b)
            for i in exams:
                d = i.text.replace("듣기", "").strip()
                e = list(d)
                C_exam = "".join(e)
            C_doc = {'C_Def': C_def, 'C_Exam': C_exam}
            return C_doc
    else:
        if "strong" in str(soup):
            C_word_class = soup.find("strong", attrs={'class': 'tit_ex'}).text
            for i in defs:
                if len(i) > 0:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    C_def = "".join(b)
            for i in exams:
                d = i.text.replace("듣기", "").strip()
                e = list(d)
                C_exam = "".join(e)
            C_doc = {'C_Word_Class': C_word_class, 'C_Def': C_def, 'C_Exam': C_exam}
            return C_doc
        else:
            for i in defs:
                if len(i) > 0:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    C_def = "".join(b)
            for i in exams:
                d = i.text.replace("듣기", "").strip()
                e = list(d)
                C_exam = "".join(e)
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
            for i in defs:
                if len(i) > 0:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    J_def = "".join(b)
            for i in exams:
                a = i.text.replace("듣기", "").strip()
                b = list(a)
                J_exam = "".join(b)
            J_doc = {'J_Word_Class': J_word_class, 'J_Def': J_def, 'J_Exam': J_exam}
            return J_doc
        else:
            for i in defs:
                if len(i) > 0:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    J_def = "".join(b)
            for i in exams:
                a = i.text.replace("듣기", "").strip()
                b = list(a)
                J_exam = "".join(b)
            J_doc = {'J_Def': J_def, 'J_Exam': J_exam}
            return J_doc

    else:
        if "strong" in str(soup):
            J_word_class = soup.find("strong", attrs={'class': 'tit_ex'}).text
            for i in defs:
                if len(i) > 0:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    J_def = "".join(b)
            for i in exams:
                a = i.text.replace("듣기", "").strip()
                b = list(a)
                J_exam = "".join(b)
            J_doc = {'J_Word_Class': J_word_class, 'J_Def': J_def, 'J_Exam': J_exam}
            return J_doc
        else:
            for i in defs:
                if len(i) > 0:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    J_def = "".join(b)
            for i in exams:
                a = i.text.replace("듣기", "").strip()
                b = list(a)
                J_exam = "".join(b)
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
            for i in defs:
                if len(i) > 0:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    K_def = "".join(b)
            for i in exams:
                a = i.text.replace("듣기", "").strip()
                b = list(a)
                K_exam = "".join(b)
            K_doc = {'K_Word_Class': K_word_class, 'K_Def': K_def, 'K_Exam': K_exam}
            return K_doc
        else:
            for i in defs:
                if len(i) > 0:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    K_def = "".join(b)
            for i in exams:
                a = i.text.replace("듣기", "").strip()
                b = list(a)
                K_exam = "".join(b)
            K_doc = {'K_Def': K_def, 'K_Exam': K_exam}
            return K_doc

    else:
        if "strong" in str(soup):
            K_word_class = soup.find("strong", attrs={'class': 'tit_ex'}).text
            for i in defs:
                if len(i) > 0:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    K_def = "".join(b)
            for i in exams:
                a = i.text.replace("듣기", "").strip()
                b = list(a)
                K_exam = "".join(b)
            K_doc = {'K_Word_Class': K_word_class, 'K_Def': K_def, 'K_Exam': K_exam}
            return K_doc
        else:
            for i in defs:
                if len(i) > 0:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    K_def = "".join(b)
            for i in exams:
                a = i.text.replace("듣기", "").strip()
                b = list(a)
                K_exam = "".join(b)
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
            for i in defs:
                if len(i) > 0:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    E_def = "".join(b)
            for i in exams:
                a = i.text.replace("듣기", "").strip()
                b = list(a)
                E_exam = "".join(b)
            E_doc = {'E_Word_Class': E_word_class, 'E_Def': E_def, 'E_Exam': E_exam}
            return E_doc
        else:
            for i in defs:
                if len(i) > 0:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    E_def = "".join(b)
            for i in exams:
                a = i.text.replace("듣기", "").strip()
                b = list(a)
                E_exam = "".join(b)
            E_doc = {'E_Def': E_def, 'E_Exam': E_exam}
            return E_doc
    else:
        if "strong" in str(soup):
            E_word_class = soup.find("strong", attrs={'class': 'tit_ex'}).text
            for i in defs:
                if len(i) > 0:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    E_def = "".join(b)
            for i in exams:
                a = i.text.replace("듣기", "").strip()
                b = list(a)
                E_exam = "".join(b)
            E_doc = {'E_Word_Class': E_word_class, 'E_Def': E_def, 'E_Exam': E_exam}
            return E_doc
        else:
            for i in defs:
                if len(i) > 0:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    E_def = "".join(b)
            for i in exams:
                a = i.text.replace("듣기", "").strip()
                b = list(a)
                E_exam = "".join(b)
            E_doc = {'E_Def': E_def, 'E_Exam': E_exam}
            return E_doc



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://dic.daum.net/word/view_supword.do?wordid=kew000036642&supid=keu000247380&suptype=KUMSUNG_KE'
data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
defs = soup.find_all("p", attrs={'class':'desc_item'})
exams = soup.find_all("p", attrs={'class':'desc_ex'})
if 'tit_ex' in str(soup):
    a = soup.find("strong", attrs={'class': 'tit_ex'}).text
    word_class = {'E_Word_Class': a}
    print(word_class)
    for i in defs:
        if len(i) > 0:
            a = i.text.replace("듣기", "").strip()
            b = list(a)
            c = "".join(b)
            d = {'E_def': c}
            print(d)
    for i in exams:
        a = i.text.replace("듣기", "").strip()
        b = list(a)
        c = "".join(b)
        d = {'E_exam': c}
        print(d)
else:
    for i in defs:
        if len(i) > 0:
            a = i.text.replace("듣기", "").strip()
            b = list(a)
            c = "".join(b)
            d = {'E_def': c}
            print(d)
    for i in exams:
        a = i.text.replace("듣기", "").strip()
        b = list(a)
        c = "".join(b)
        d = {'E_exam': c}
        print(d)
