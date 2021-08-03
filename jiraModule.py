# jira 연결
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
import requests
import json
import re
import settings

"""
    made by 도니, 모카
"""


# 모든버그 가젯주소
def getJiraList(jiraPage):
    jira_page = settings.jiraDashBoardUrl[jiraPage]
    auth = HTTPBasicAuth('soup', 'tony0513')  # jira id, pwd 넣기!
    r = requests.get(url=jira_page, auth=auth)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    dict = json.loads(html)
    # 버전갯수+total (세로길이)
    vernum = len(dict['rows'])
    # print(vernum)
    # 버그종류갯수 +total (가로길이)
    bugcount = len(dict['rows'][0]['cells'])
    # print(bugcount)
    # 버전명리스트
    vername_list = []
    for i in range(0, vernum, 1):
        vername_list.append(dict['rows'][i]['cells'][0]['markup'])
    print("버전종류리스트" + str(vername_list))
    # 갯수리스트 (total 포함)
    total_list = []
    for a in range(0, vernum, 1):  # 버전갯수만큼 반복문
        count_list = []
        for i in range(0, bugcount, 1):  # 각버전의 버그리스트 반복문
            count = dict['rows'][a]['cells'][i]['markup']
            change_fronturl = re.sub(re.compile('<a href=\''), '=HYPERLINK("',
                                     count)  # 앞부분 변경 : <a href=    >>   =HYPERLINK("
            change_middleurl = re.sub(re.compile('\'>'), '",value("', change_fronturl)  # 가운데 변경: '>  >>  ",value("
            change_end = re.sub(re.compile('</a>'), '"))', change_middleurl)  # 끝부분 변경: </a>  >>  "))
            count_list.append(change_end)
        total_list.append(count_list)

    return total_list


# 세로길이(행)
def getRow():
    return len(getJiraList())


# 가로길이(열)
def getCol():
    return len(getJiraList())
