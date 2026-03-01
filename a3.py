import random
import time
def getRandomDate(startDate, endDate):
    print("Printing random date between", startDate, "and", endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'
    Sdate = time.mktime(time.strptime(startDate, dateFormat))
    Edate = time.mktime(time.strptime(endDate, dateFormat))
    randomTime = Sdate + randomGenerator * (Edate - Sdate)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print("Random Date =", getRandomDate("01/01/2026" , "12/01/2026"))