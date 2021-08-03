from slacker import Slacker
import datetime
import settings

token = settings.slackToken
slack = Slacker(token)


def setErrorMessage():
    slack.chat.post_message(channel='#x_테스트', text=('갱신 알림 오류 (대시보드 input 확인 필요)'))


def setMessage():
    now = datetime.datetime.now()
    dateAndTime = now.strftime('%Y-%m-%d %H:%M:%S')

    slack.chat.post_message(channel='#prd_qa_members', text=(dateAndTime + ' 갱신 완료'))
