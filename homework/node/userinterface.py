
from hw1 import Locomotive,PassengerCar,FuelCar,CarType,CarBase
from hw6 import Train,Car


_train = None
def UserInterface():
    ending = False
    locomotiveManufaturer = input('請輸入火車頭製造商: ')
    locomotiveHandler = input('請輸入列車長姓名: ')
    global _train 
    _train = Train()
    locomotive = Locomotive(locomotiveManufaturer,CarType.LOCOMOTIVE,locomotiveHandler,100)
    _train.createTrain(locomotive)

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

# endModify
def doSernoTwo():
    _train.traversal()
    return False

# endModify
def doSernoThree():
    travelHour = input('請問要行駛多久? ')
    _train.head.car.travel(travelHour)
    return False
# endModify
def doSernoFour():
    pointer = _train.head.next
    while(pointer):
        if pointer.car.cartype == CarType.PASSENGER:
            pointer.car.boarding(input('這節車廂要上來多少人? '))
        pointer = pointer.next
    return False
# endModify
def doSernoFive():
    pointer = _train.head.next
    while(pointer):
        if pointer.car.cartype == CarType.PASSENGER:
            pointer.car.getoff(input('這節車廂要下去多少人? '))
        pointer = pointer.next
    return False
# endModify
def doSernoSix():
    _train.head.car.refuel()
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
