import datetime,time
today = datetime.date.today().strftime("%Y-%m-%d")
xtoday = time.strftime("%d")
xc = int(xtoday) + 1
if int(xtoday) + 1 == xc:
    print(123)

tomorrow = today + datetime.timedelta(days=1)
todayFormat = datetime.date.today().strftime("%Y-%m-%d")
energyUseLight = 0
lightData = 0
energyUseHeating = 0
heatingData = 0 
lightDatabase = {}
heatingDatabase = {}
coreDatabase = {}

# def dataRecord():
if today<tomorrow:  
    energyUseLight += lightData
    energyUseHeating += heatingData
    print("ok")
else:
    lightDatabase[today] = energyUseLight
    heatingDatabase[today] = energyUseHeating
    coreDatabase[today] = energyUseLight + energyUseHeating
 

