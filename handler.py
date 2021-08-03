import gsheet
import jiraModule
import slackBot
import settings


def main(event, context):
    for i in settings.jiraDashBoardUrl:
        print(settings.jiraDashBoardUrl[i])
        bugChartList = jiraModule.getJiraList(i)
        gsheet.gspreadModule().setBugChart(bugChartList, i)

    slackBot.setMessage()
    return {}