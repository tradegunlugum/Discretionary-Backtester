from TradeInfo import TradeInfo


class TradeInfoManager:

    tradeInfoIndexes = {}
    tradeInfos = []

    def __init__(self, fileName):

        self.file = open(fileName, "r")
        self.lines = self.file.readlines()

        for i in range(len(self.lines)):
            info = TradeInfo(self.lines[i])
            self.tradeInfoIndexes[info.dateInfo] = i
            self.tradeInfos.append(info)

        #self.printTradeInfos()


    def printTradeInfos(self):
        for info in self.tradeInfos:
            info.printInfo()

    def getIndex(self, date):
        index = self.tradeInfoIndexes[date]
        return index

    def startTrades(self, positions):
        for position in positions:
            self.startTrade(position)

    def startTrade(self, date, stopLoss, takeProfit):

        startIndex = self.getIndex(date)
        currentDate = self.tradeInfos[startIndex]

        if currentDate.closePrice < stopLoss:
            print("opening short position")
            self.startTradeShort(startIndex, stopLoss, takeProfit)
        elif currentDate.closePrice > stopLoss:
            print("opening long position")
            self.startTradeLong(startIndex, stopLoss, takeProfit)

    # open long trade
    def startTrade(self, position):

        startIndex = self.getIndex(position.dateInfo)
        currentDate = self.tradeInfos[startIndex]

        if currentDate.closePrice < position.stopLoss:
            print("opening short position")
            self.startTradeShort(startIndex, position)
        elif currentDate.closePrice > position.stopLoss:
            print("opening long position")
            self.startTradeLong(startIndex, position)


    # def startTradeLong(self, startIndex, stopLoss, takeProfit):
    #     startIndex += 1
    #     while (startIndex < len(self.tradeInfoIndexes)):
    #         tradeInfo = self.tradeInfos[startIndex]
    #         if tradeInfo.lowPrice < stopLoss:
    #             print("stop loss")
    #             tradeInfo.printInfo()
    #             break
    #         elif tradeInfo.highPrice > takeProfit:
    #             print("take profit")
    #             tradeInfo.printInfo()
    #             break
    #
    #         startIndex += 1

    def startTradeLong(self, startIndex, position):
        startIndex += 1
        while (startIndex < len(self.tradeInfoIndexes)):
            tradeInfo = self.tradeInfos[startIndex]
            if tradeInfo.lowPrice < position.stopLoss:
                print("stop loss")
                tradeInfo.printInfo()
                break
            elif tradeInfo.highPrice > position.takeProfit:
                print("take profit")
                tradeInfo.printInfo()
                break

            startIndex += 1

    def startTradeShort(self, startIndex, position):
        startIndex += 1
        while (startIndex < len(self.tradeInfoIndexes)):
            tradeInfo = self.tradeInfos[startIndex]
            if tradeInfo.lowPrice < position.takeProfit:
                print("take profit")
                tradeInfo.printInfo()
                break
            elif tradeInfo.highPrice > position.stopLoss:
                print("stop loss")
                tradeInfo.printInfo()
                break

            startIndex += 1

    # def startTradeShort(self, startIndex, stopLoss, takeProfit):
    #     startIndex += 1
    #     while (startIndex < len(self.tradeInfoIndexes)):
    #         tradeInfo = self.tradeInfos[startIndex]
    #         if tradeInfo.lowPrice > stopLoss:
    #             print("stop loss")
    #             tradeInfo.printInfo()
    #             break
    #         elif tradeInfo.highPrice < takeProfit:
    #             print("take profit")
    #             tradeInfo.printInfo()
    #             break
    #
    #         startIndex += 1