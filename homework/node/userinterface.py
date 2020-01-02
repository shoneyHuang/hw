
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
        print('2. 刪除指定列車')
        print('3. 更換火車頭')
        print('4. 顯示列車狀態')
        print('5. 行駛列車')
        print('6. 乘客上車')
        print('7. 乘客下車')
        print('8. 火車頭燃料補充')
        print('Other. 結束')
        print('==================')
        ending = switch_userDoing(input('請輸入: '))

        

def doSernoOne():
    insertIndex = int(input("請問要插到第幾節車廂後?"))
    # whether car num exists or not
    if _train.checkCar(insertIndex):
        car = None
        carType = int(input('請問需要哪種車廂? 1.燃料 2.乘客: '))
        createType = CarType.FUEL if carType == 1 else CarType.PASSENGER
        carmanufaturer = input('請問製造商? ')
        #if cartype is fuel car
        if carType == 1:
            fuelCount = int(input('請問燃料數量? '))
            if(fuelCount > 500 or fuelCount < 0):
                print('燃料車廂要給正確的燃料')
            else:
                car =   FuelCar(carmanufaturer,createType,fuelCount)
        #or passenger car
        else:
            car = PassengerCar(carmanufaturer,createType,0)

        _train.addCar(insertIndex,car)

    else:
        print("車廂不存在!")
    return False
def doSernoTwo():
    return False
def doSernoThree():
    return False
# endModify
def doSernoFour():
    _train.traversal()
    return False
# endModify
def doSernoFive():
    travelHour = input('請問要行駛多久? ')
    _train.head.car.travel(travelHour)
    return False
# endModify
def doSernoSix():
    pointer = _train.head.next
    while(pointer):
        if pointer.car.cartype == CarType.PASSENGER:
            pointer.car.boarding(input('這節車廂要上來多少人? '))
        pointer = pointer.next
    return False
# endModify
def doSernoSeven():
    pointer = _train.head.next
    while(pointer):
        if pointer.car.cartype == CarType.PASSENGER:
            pointer.car.getoff(input('這節車廂要下去多少人? '))
        pointer = pointer.next
    return False
# endModify
def doSernoEight():
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
        '6': doSernoSix,
        '7': doSernoSeven,
        '8': doSernoEight
    }
    return switcher.get(argument,doEnd)()
