"""
매번 바꾸기 힘든 세팅파일들
"""

# 시트 설정용

spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1gzRJmw0eZ5Xtb5xTIDc1v800yoRudGUmr0QHj2dNnac/edit#gid=418965326'
test2spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1wASLgKSgkC3BFiLDzOQGHNz3CwNl8BngDufwEO2q9wg/edit#gid=1068382649'
testSpreadsheet_url = 'https://docs.google.com/spreadsheets/d/1A0uXs80ygoibFrCPbqtrCRMbUwmThEolHxGYTBLoAlM/edit#gid=1561112605'
json_file_name = 'rentaltestphone-7d11f49b968d.json'

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
]

# slack 설정용
slackToken = 'xoxb-237846854519-874316260450-ws9DokqNGsE08uCYFiXOIKy4'

# jira 설정용

# 버그유형 -> 유입경로 -> 중요도
jiraDashBoardUrl = {
    'bugtype_url': "http://jira.dailyhou.se/rest/gadget/1.0/twodimensionalfilterstats/generate?filterId=filter-11746&xstattype=customfield_11100&ystattype=allVersion&sortDirection=desc&sortBy=natural&numberToShow=1000",
    'realese_url': "http://jira.dailyhou.se/rest/gadget/1.0/twodimensionalfilterstats/generate?filterId=filter-11807&xstattype=customfield_11101&ystattype=allVersion&sortDirection=desc&sortBy=natural&numberToShow=1000",
    'priority_url': "http://jira.dailyhou.se/rest/gadget/1.0/twodimensionalfilterstats/generate?filterId=filter-11746&xstattype=priorities&ystattype=allVersion&sortDirection=desc&sortBy=natural&numberToShow=1000"
    }

