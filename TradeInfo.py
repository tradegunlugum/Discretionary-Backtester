from datetime import datetime

class TradeInfo:
    def __init__(self, dateInfo, openPrice, highPrice, lowPrice, closePrice):
        self.dateInfo = dateInfo
        self.openPrice = openPrice
        self.highPrice = highPrice
        self.lowPrice = lowPrice
        self.closePrice = closePrice

    def __init__(self, row):
        strs = row.split(',')
        self.dateInfo = datetime.strptime(strs[0] + strs[1], "%Y%m%d%H:%M:%S")
        self.openPrice = float(strs[2])
        self.highPrice = float(strs[3])
        self.lowPrice = float(strs[4])
        self.closePrice = float(strs[5])

    def printInfo(self):
        print("date : " + str(self.dateInfo) + " , opening price = " + str(self.openPrice)  + " highPrice = " + str(self.highPrice)
              + ", low price = " + str(self.lowPrice) + " , close price = " + str(self.closePrice))

