class Position:

    def __init__(self, isLong , dateInfo, stopDistance, riskReward):
        self.isLong = isLong
        self.dateInfo = dateInfo
        self.stopDistance = stopDistance
        self.riskReward = riskReward

        self.calculatePosition()


    def calculatePosition(self):

        self.entryPrice = self.dateInfo.closePrice

        if self.isLong:
            self.stopLoss = self.entryPrice - self.stopDistance
        else:
            self.stopLoss = self.entryPrice + self.stopDistance

        if self.isLong:
            self.takeProfit = self.entryPrice + self.stopDistance * self.riskReward
        else:
            self.takeProfit = self.entryPrice - self.stopDistance * self.riskReward


    def printInfo(self):
        print("entry price : " + str(self.entryPrice) + " , take profit : " + str(self.takeProfit) + "  , stop loss : " + str(self.stopLoss))