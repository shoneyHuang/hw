from homework1 import Train,Locomotive,PassengerCar,FuelCar,CarType
from homework2 import traversal,addNodeAtEnd

_locomotive = None

def userinterface():
    ending = False
    locomotiveManufaturer = input('請輸入火車頭製造商: ')
    locomotiveHandler = input('請輸入列車長姓名: ')
    global _locomotive 
    _locomotive = Locomotive(locomotiveManufaturer,CarType.LOCOMOTIVE,locomotiveHandler,100)
    while(not ending):
        print('==================')
        print('請問接下來要做什麼?')
        print('==================')
        print('1. 加車廂')
        print('2. 顯示列車狀態')
        print('3. 行駛列車')
        print('4. 乘客上車')
        print('5. 乘客下車')
        print('6. 火車頭燃料補充')
        print('7. 結束')
        print('==================')
        ending = switch_userDoing(input('請輸入: '))

        

def doSernoOne():
    fuelCount = 0
    carType = input('請問需要哪種車廂? 1.燃料 2.乘客: ')
    createType = CarType.FUEL if int(carType) == 1 else CarType.PASSENGER
    carmanufaturer = input('請問製造商? ')
    if int(carType) == 1:
        fuelCount = input('請問燃料數量? ')

    addNodeAtEnd(_locomotive,carmanufaturer,createType,fuelCount)
    return False

def doSernoTwo():
    traversal(_locomotive)
    return False

def doSernoThree():
    travelHour = input('請問要行駛多久? ')
    _locomotive.travel(travelHour)
    return False

def doSernoFour():
    for x in _locomotive.connectType:
        if x.cartype == CarType.PASSENGER:
            x.boarding(input('這節車廂要上來多少人? '))
    return False

def doSernoFive():
    for x in _locomotive.connectType:
        if x.cartype == CarType.PASSENGER:
            x.getoff(input('這節車廂要下去多少人? '))
    return False

def doSernoSix():
    _locomotive.refuel()
    return False

def doEnd():
    return True

def switch_userDoing(argument):
    print()
    switcher = {
        '1': doSernoOne,
        '2': doSernoTwo,
        '3': doSernoThree,
        '4': doSernoFour,
        '5': doSernoFive,
        '6': doSernoSix
    }
    return switcher.get(argument,doEnd)()