class Solution:
    def dayOfYear(self, date: str) -> int:
        def isLeap(year):
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                return False
            elif year % 4 == 0:
                return True
            return False
        if isLeap(int(date[:4])):
            days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if date[5:7] == '01':
            return int(date[-2:])
      
        return sum(days_in_month[0:int(date[5:7]) - 1]) + int(date[-2:])