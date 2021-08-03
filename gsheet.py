import gspread
from oauth2client.service_account import ServiceAccountCredentials
import settings
import slackBot


class gspreadModule:

    def convertAlphaToNumber(self, value):

        """
        # "1010"
        #  8421  10
        #  1 0 1 0
        #  8 4 2 1
        #  8 0 2 0 -> 10
        # 1 1 + 1
        # 0 2
        # 1 4 + 1
        # 0 10

        # "fa"
        #  15 10
        #  16 1
        #  15*16 + 10*1


        :param value:
        :return:
        """

        num = 0

        for letter in value:
            letterNum = ord(letter) - ord('A') + 1  # 1 - 26
            num *= 26
            num += letterNum

        return num

    def setBugChart(self, bugList, BugCharttype):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(settings.json_file_name, settings.scope)
        gc = gspread.authorize(credentials)
        doc = gc.open_by_url(settings.spreadsheet_url)

        # 오류유형 M5
        # 우선순위 G3
        # 유입경로 I3

        if BugCharttype == "bugtype_url":
            firstRow = 5
            firstCol = self.convertAlphaToNumber('M')
            worksheet = doc.worksheet('오류유형')

        elif BugCharttype == "priority_url":
            firstRow = 3
            firstCol = self.convertAlphaToNumber('G')
            worksheet = doc.worksheet('우선순위')

        elif BugCharttype == "realese_url":
            firstRow = 3
            firstCol = self.convertAlphaToNumber('I')
            worksheet = doc.worksheet('유입경로')

        else:

            return slackBot.setErrorMessage()

        lastRow = firstRow + len(bugList) - 1
        lastCol = firstCol + len(bugList[0]) - 1

        gsheetRange = worksheet.range(firstRow, firstCol, lastRow, lastCol)

        for cell in gsheetRange:
            cell.value = bugList[cell.row - firstRow][cell.col - firstCol]

        worksheet.update_cells(gsheetRange, 'USER_ENTERED')
