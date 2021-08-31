from datetime import datetime

from Position import Position
from PositionManager import PositionManager
from TradeInfo import TradeInfo
from TradeInfoManager import TradeInfoManager


dateInfo = datetime.strptime("2020010203:50:00", "%Y%m%d%H:%M:%S")
manager = TradeInfoManager("EURUSD_5min_sample.txt")

posManager = PositionManager()
date1 = datetime.strptime("2020010202:00:00", "%Y%m%d%H:%M:%S")
date2 = datetime.strptime("2020011301:05:00", "%Y%m%d%H:%M:%S")

infoIndex = manager.getIndex(date1)
info = manager.tradeInfos[infoIndex]

pos1 = Position(True, info, 0.00005, 2)
pos1.printInfo()

#manager.startTrade()

# posManager.addPosition(Position(date1, 1.12142, 1.11992))
# posManager.addPosition(Position(date2, 1.11206 , 1.11356))

manager.startTrades(posManager.positions)









