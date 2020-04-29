import requests
from bs4 import BeautifulSoup

#
# def C_def_results(u):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     url = u
#     data = requests.get(url, headers=headers)
#     soup = BeautifulSoup(data.text, 'html.parser')
#     defs = soup.find_all("p", attrs={'class':'desc_item'})
#     exams = soup.find_all("p", attrs={'class':'desc_ex'})
#     C_Doc =[]
#     if 'tit_ex' in str(soup):
#         if "strong" in str(soup):
#             C_word_class = soup.find("strong", attrs={'class': 'tit_ex'}).text
#             C_Word_Class = {'C_Word_Class': C_word_class}
#             C_Doc.append(C_Word_Class)
#             if defs is not None:
#                 for i in defs:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     C_def = "".join(b)
#                     if len(C_def)>0:
#                         C_Def = {'C_Def': C_def}
#                         C_Doc.append(C_Def)
#             else:
#                 C_Def ={'C_Def': ''}
#                 C_Doc.append(C_Def)
#             if exams is not None:
#                 for i in exams:
#                     d = i.text.replace("듣기", "").strip()
#                     e = list(d)
#                     C_exam = "".join(e)
#                     C_Exam = {'C_Exam': C_exam}
#                     C_Doc.append(C_Exam)
#             else:
#                 C_Exam ={'C_Exam':''}
#                 C_Doc.append(C_Exam)
#             print (C_Doc)
#         else:
#             if defs is not None:
#                 for i in defs:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     C_def = "".join(b)
#                     if len(C_def) > 0:
#                         C_Def = {'C_Def': C_def}
#                         C_Doc.append(C_Def)
#             else:
#                 C_Def ={'C_Def': ''}
#                 C_Doc.append(C_Def)
#             if exams is not None:
#                 for i in exams:
#                     d = i.text.replace("듣기", "").strip()
#                     e = list(d)
#                     C_exam = "".join(e)
#                     C_Exam = {'C_Exam': C_exam}
#                     C_Doc.append(C_Exam)
#             else:
#                 C_Exam ={'C_Exam':''}
#                 C_Doc.append(C_Exam)
#             print (C_Doc)
#     else:
#         if "strong" in str(soup):
#             C_word_class = soup.find("strong", attrs={'class': 'tit_ex'}).text
#             C_Word_Class = {'C_Word_Class': C_word_class}
#             C_Doc.append(C_Word_Class)
#             if defs is not None:
#                 for i in defs:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     C_def = "".join(b)
#                     if len(C_def) > 0:
#                         C_Def = {'C_Def': C_def}
#                         C_Doc.append(C_Def)
#             else:
#                 C_Def ={'C_Def':''}
#                 C_Doc.append(C_Def)
#             if exams is not None:
#                 for i in exams:
#                     d = i.text.replace("듣기", "").strip()
#                     e = list(d)
#                     C_exam = "".join(e)
#                     C_Exam = {'C_Exam': C_exam}
#                     C_Doc.append(C_Exam)
#             else:
#                 C_Exam={'C_Exam':''}
#                 C_Doc.append(C_Exam)
#             print (C_Doc)
#         else:
#             if defs is not None:
#                 for i in defs:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     C_def = "".join(b)
#                     if len(C_def) > 0:
#                         C_Def = {'C_Def': C_def}
#                         C_Doc.append(C_Def)
#             else:
#                 C_Def ={'C_Def':''}
#                 C_Doc.append(C_Def)
#             if exams is not None:
#                 for i in exams:
#                     d = i.text.replace("듣기", "").strip()
#                     e = list(d)
#                     C_exam = "".join(e)
#                     C_Exam = {'C_Exam': C_exam}
#                     C_Doc.append(C_Exam)
#             else:
#                 C_Exam={'C_Exam': ''}
#                 C_Doc.append(C_Exam)
#             print(C_Doc)
#
#
# def J_def_results(u):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     url = u
#     data = requests.get(url, headers=headers)
#     soup = BeautifulSoup(data.text, 'html.parser')
#     defs = soup.find_all("p", attrs={'class':'desc_item'})
#     exams = soup.find_all("p", attrs={'class':'desc_ex'})
#     J_Doc =[]
#     if 'tit_ex' in str(soup):
#         if "strong" in str(soup):
#             J_word_class = soup.find("strong", attrs={'class': 'tit_ex'}).text
#             J_Word_Class = {'J_Word_Class' : J_word_class}
#             J_Doc.append(J_Word_Class)
#             if defs is not None:
#                 for i in defs:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     J_def = "".join(b)
#                     if len(J_def)>0:
#                         J_Def = {'J_Def': J_def}
#                         J_Doc.append(J_Def)
#             else:
#                 J_Def = {'J_Def': ''}
#                 J_Doc.append(J_Def)
#             if exams is not None:
#                 for i in exams:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     J_exam = "".join(b)
#                     J_Exam = {'J_Exam': J_exam}
#                     J_Doc.append(J_Exam)
#             else:
#                 J_Exam = {'J_Exam': ''}
#                 J_Doc.append(J_Exam)
#             print (J_Doc)
#         else:
#             if defs is not None:
#                 for i in defs:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     J_def = "".join(b)
#                     if len(J_def) > 0:
#                         J_Def = {'J_Def': J_def}
#                         J_Doc.append(J_Def)
#             else:
#                 J_Def = {'J_Def': ''}
#                 J_Doc.append(J_Def)
#             if exams is not None:
#                 for i in exams:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     J_exam = "".join(b)
#                     J_Exam = {'J_Exam': J_exam}
#                     J_Doc.append(J_Exam)
#             else:
#                 J_Exam = {'J_Exam': ''}
#                 J_Doc.append(J_Exam)
#             print(J_Doc)
#     else:
#         if "strong" in str(soup):
#             J_word_class = soup.find("strong", attrs={'class': 'tit_ex'}).text
#             J_Word_Class = {'J_Word_Class': J_word_class}
#             J_Doc.append(J_Word_Class)
#             if defs is not None:
#                 for i in defs:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     J_def = "".join(b)
#                     if len(J_def) > 0:
#                         J_Def = {'J_Def': J_def}
#                         J_Doc.append(J_Def)
#             else:
#                 J_Def = {'J_Def': ''}
#                 J_Doc.append(J_Def)
#             if exams is not None:
#                 for i in exams:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     J_exam = "".join(b)
#                     J_Exam = {'J_Exam': J_exam}
#                     J_Doc.append(J_Exam)
#             else:
#                 J_Exam = {'J_Exam': ''}
#                 J_Doc.append(J_Exam)
#                 print(J_Doc)
#         else:
#             if defs is not None:
#                 for i in defs:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     J_def = "".join(b)
#                     if len(J_def) > 0:
#                         J_Def = {'J_Def': J_def}
#                         J_Doc.append(J_Def)
#             else:
#                 J_Def = {'J_Def': ''}
#                 J_Doc.append(J_Def)
#             if exams is not None:
#                 for i in exams:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     J_exam = "".join(b)
#                     J_Exam = {'J_Exam': J_exam}
#                     J_Doc.append(J_Exam)
#             else:
#                 J_Exam = {'J_Exam': ''}
#                 J_Doc.append(J_Exam)
#                 print(J_Doc)
#
#
# def K_def_results(u):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     url = u
#     data = requests.get(url, headers=headers)
#     soup = BeautifulSoup(data.text, 'html.parser')
#     defs = soup.find_all("p", attrs={'class':'desc_item'})
#     exams = soup.find_all("p", attrs={'class':'desc_ex'})
#     K_Doc = []
#     if 'tit_ex' in str(soup):
#         if "strong" in str(soup):
#             K_word_class = soup.find("strong", attrs={'class': 'tit_ex'}).text
#             K_Word_Class = {'K_Word_Class' : K_word_class}
#             K_Doc.append(K_Word_Class)
#             if defs is not None:
#                 for i in defs:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     K_def = "".join(b)
#                     if len(K_def)>0:
#                         K_Def = {'K_Def': K_def}
#                         K_Doc.append(K_Def)
#             else:
#                 K_Def ={'K_Def',''}
#                 K_Doc.append(K_Def)
#             if exams is not None:
#                 for i in exams:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     K_exam = "".join(b)
#                     K_Exam = {'K_Exam': K_exam}
#                     K_Doc.append(K_Exam)
#             else:
#                 K_Exam = {'K_Exam':''}
#                 K_Doc.append(K_Exam)
#             print (K_Doc)
#         else:
#             if defs is not None:
#                 for i in defs:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     K_def = "".join(b)
#                     if len(K_def) > 0:
#                         K_Def = {'K_Def': K_def}
#                         K_Doc.append(K_Def)
#             else:
#                 K_Def = {'K_Def', ''}
#                 K_Doc.append(K_Def)
#             if exams is not None:
#                 for i in exams:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     K_exam = "".join(b)
#                     K_Exam = {'K_Exam': K_exam}
#                     K_Doc.append(K_Exam)
#             else:
#                 K_Exam = {'K_Exam': ''}
#                 K_Doc.append(K_Exam)
#             print(K_Doc)
#     else:
#         if "strong" in str(soup):
#             K_word_class = soup.find("strong", attrs={'class': 'tit_ex'}).text
#             K_Word_Class = {'K_Word_Class': K_word_class}
#             K_Doc.append(K_Word_Class)
#             if defs is not None:
#                 for i in defs:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     K_def = "".join(b)
#                     if len(K_def) > 0:
#                         K_Def = {'K_Def': K_def}
#                         K_Doc.append(K_Def)
#             else:
#                 K_Def = {'K_Def', ''}
#                 K_Doc.append(K_Def)
#             if exams is not None:
#                 for i in exams:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     K_exam = "".join(b)
#                     K_Exam = {'K_Exam': K_exam}
#                     K_Doc.append(K_Exam)
#             else:
#                 K_Exam = {'K_Exam': ''}
#                 K_Doc.append(K_Exam)
#             print(K_Doc)
#         else:
#             if defs is not None:
#                 for i in defs:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     K_def = "".join(b)
#                     if len(K_def) > 0:
#                         K_Def = {'K_Def': K_def}
#                         K_Doc.append(K_Def)
#             else:
#                 K_Def = {'K_Def', ''}
#                 K_Doc.append(K_Def)
#             if exams is not None:
#                 for i in exams:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     K_exam = "".join(b)
#                     K_Exam = {'K_Exam': K_exam}
#                     K_Doc.append(K_Exam)
#             else:
#                 K_Exam = {'K_Exam': ''}
#                 K_Doc.append(K_Exam)
#             print(K_Doc)
#
#
# def E_def_results(u):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     url = u
#     data = requests.get(url, headers=headers)
#     soup = BeautifulSoup(data.text, 'html.parser')
#     defs = soup.find_all("p", attrs={'class':'desc_item'})
#     exams = soup.find_all("p", attrs={'class':'desc_ex'})
#     E_Doc =[]
#     if 'tit_ex' in str(soup):
#         if "strong" in str(soup):
#             E_word_class = soup.find("strong", attrs={'class': 'tit_ex'}).text
#             E_Word_Class = {'E_Word_Class' : E_word_class }
#             E_Doc.append(E_Word_Class)
#             if defs is not None:
#                 for i in defs:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     E_def = "".join(b)
#                     if len(E_def)>0:
#                         E_Def = {'E_Def': E_def}
#                         E_Doc.append(E_Def)
#             else:
#                 E_Def = {'E_def': ''}
#                 E_Doc.append(E_Def)
#             if exams is not None:
#                 for i in exams:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     E_exam = "".join(b)
#                     E_Exam = {'E_Exam': E_exam}
#                     E_Doc.append(E_Exam)
#             else:
#                 E_Exam = {'E_Exam': ''}
#                 E_Doc.append(E_Exam)
#             print (E_Doc)
#         else:
#             if defs is not None:
#                 for i in defs:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     E_def = "".join(b)
#                     if len(E_def) > 0:
#                         E_Def = {'E_Def': E_def}
#                         E_Doc.append(E_Def)
#             else:
#                 E_Def = {'E_Def': ''}
#                 E_Doc.append(E_Def)
#             if exams is not None:
#                 for i in exams:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     E_exam = "".join(b)
#                     E_Exam = {'E_Exam': E_exam}
#                     E_Doc.append(E_Exam)
#             else:
#                 E_Exam ={'E_Exam': ''}
#                 E_Doc.append(E_Exam)
#             print (E_Doc)
#     else:
#         if "strong" in str(soup):
#             E_word_class = soup.find("strong", attrs={'class': 'tit_ex'}).text
#             E_Word_Class = {'E_Word_Class': E_word_class}
#             E_Doc.append(E_Word_Class)
#             if defs is not None:
#                 for i in defs:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     E_def = "".join(b)
#                     if len(E_def) > 0:
#                         E_Def = {'E_Def': E_def}
#                         E_Doc.append(E_Def)
#             else:
#                 E_Def = {'E_Def' :''}
#                 E_Doc.append(E_Def)
#             if exams is not None:
#                 for i in exams:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     E_exam = "".join(b)
#                     E_Exam ={'E_Exam': E_exam}
#                     E_Doc.append(E_Exam)
#             else:
#                 E_Exam ={'E_Exam' :''}
#                 E_Doc.append(E_Exam)
#             print (E_Doc)
#         else:
#             if defs is not None:
#                 for i in defs:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     E_def = "".join(b)
#                     if len(E_def) > 0:
#                         E_Def = {'E_Def': E_def}
#                         E_Doc.append(E_Def)
#             else:
#                 E_Def = {'E_Def': ''}
#                 E_Doc.append(E_Def)
#             if exams is not None:
#                 for i in exams:
#                     a = i.text.replace("듣기", "").strip()
#                     b = list(a)
#                     E_exam = "".join(b)
#                     E_Exam = {'E_Exam' : E_exam}
#                     E_Doc.append(E_Exam)
#             else:
#                 E_Exam ={'E_Exam': ''}
#                 E_Doc.append(E_Exam)
#             print (E_Doc)


def C_def_results(u):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = u
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    defs = soup.find_all("p", attrs={'class':'desc_item'})
    exams = soup.find_all("p", attrs={'class':'desc_ex'})
    C_Doc =[]
    if 'tit_ex' in str(soup):
        if "strong" in str(soup):
            C_word_class = soup.find("strong", attrs={'class': 'tit_ex'}).text
            C_Word_Class = {'C_Word_Class': C_word_class}
            C_Doc.append(C_Word_Class)
            if defs is not None:
                for i in defs:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    C_def = "".join(b)
                    if len(C_def)>0:
                        C_Def = {'C_Def': C_def}
                        C_Doc.append(C_Def)
            else:
                C_Def ={'C_Def': ''}
                C_Doc.append(C_Def)
            if exams is not None:
                for i in exams:
                    d = i.text.replace("듣기", "").strip()
                    e = list(d)
                    C_exam = "".join(e)
                    C_Exam = {'C_Exam': C_exam}
                    C_Doc.append(C_Exam)
            else:
                C_Exam ={'C_Exam':''}
                C_Doc.append(C_Exam)
            print (C_Doc)
        else:
            if defs is not None:
                for i in defs:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    C_def = "".join(b)
                    if len(C_def) > 0:
                        C_Def = {'C_Def': C_def}
                        C_Doc.append(C_Def)
            else:
                C_Def ={'C_Def': ''}
                C_Doc.append(C_Def)
            if exams is not None:
                for i in exams:
                    d = i.text.replace("듣기", "").strip()
                    e = list(d)
                    C_exam = "".join(e)
                    C_Exam = {'C_Exam': C_exam}
                    C_Doc.append(C_Exam)
            else:
                C_Exam ={'C_Exam':''}
                C_Doc.append(C_Exam)
            print (C_Doc)
    else:
        if "strong" in str(soup):
            C_word_class = soup.find("strong", attrs={'class': 'tit_ex'}).text
            C_Word_Class = {'C_Word_Class': C_word_class}
            C_Doc.append(C_Word_Class)
            if defs is not None:
                for i in defs:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    C_def = "".join(b)
                    if len(C_def) > 0:
                        C_Def = {'C_Def': C_def}
                        C_Doc.append(C_Def)
            else:
                C_Def ={'C_Def':''}
                C_Doc.append(C_Def)
            if exams is not None:
                for i in exams:
                    d = i.text.replace("듣기", "").strip()
                    e = list(d)
                    C_exam = "".join(e)
                    C_Exam = {'C_Exam': C_exam}
                    C_Doc.append(C_Exam)
            else:
                C_Exam={'C_Exam':''}
                C_Doc.append(C_Exam)
            print (C_Doc)
        else:
            if defs is not None:
                for i in defs:
                    a = i.text.replace("듣기", "").strip()
                    b = list(a)
                    C_def = "".join(b)
                    if len(C_def) > 0:
                        C_Def = {'C_Def': C_def}
                        C_Doc.append(C_Def)
            else:
                C_Def ={'C_Def':''}
                C_Doc.append(C_Def)
            if exams is not None:
                for i in exams:
                    d = i.text.replace("듣기", "").strip()
                    e = list(d)
                    C_exam = "".join(e)
                    C_Exam = {'C_Exam': C_exam}
                    C_Doc.append(C_Exam)
            else:
                C_Exam={'C_Exam': ''}
                C_Doc.append(C_Exam)
            print(C_Doc)
u='https://dic.daum.net/word/view_supword.do?wordid=kcw000040297&supid=kcu000045156&suptype=KOREA_KC'

C_def_results(u)





# list1=[1,2,3]
# list2=[4,5,6]
# data=[]
# data1 = data.extend(list1)
# print(data1)
#
#
# search():
#     search_receive= request.form['search_give']
#     result = list()
#     c_result = C_search(search_receive)
#     print(c_result)
#     result.append(c_result)
#     j_result = J_search(search_receive)
#     result.append(j_result)
#     print(j_result)
#     k_result = K_search(search_receive)
#     result.append(k_result)
#     print(k_result)
#     e_result = E_search(search_receive)
#     result.append(e_result)
#     print(e_result)
#     return jsonify({'result': 'success', 'msg' :'Post가 완료', 'data': result})