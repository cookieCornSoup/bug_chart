import gsheet
import jiraModule
import slackBot
import settings

if __name__ == "__main__":

    for i in settings.jiraDashBoardUrl:
        print(settings.jiraDashBoardUrl[i])
        bugChartList = jiraModule.getJiraList(i)
        gsheet.gspreadModule().setBugChart(bugChartList, i)

    # slackBot.setMessage()
