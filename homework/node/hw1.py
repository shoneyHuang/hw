from enum import Enum
class CarType(Enum):
    LOCOMOTIVE = 'Locomotive'
    FUEL = 'Fuel'
    PASSENGER = 'Passenger'

class CarBase():
    def __init__(self, manufacturer,cartype: CarType):
        self.manufacturer = manufacturer
        self.cartype = cartype
    def showmanufacturer(self):
        print('車廂製造商:' + self.manufacturer)

class Locomotive(CarBase):
    # ,connectType = []
    def __init__(self,manufacturer,cartype,handler,fuel:int):
        super().__init__(manufacturer,cartype)
        self.handler = handler
        self.fuel = fuel
        # self.connectType = connectType
    def showHandler(self):
        print('列車長姓名:' + self.handler)
    def showfuel(self):
        print('剩餘 : ' + str(self.fuel) + '燃料')
    # def showConnectType(self):
    #     passengerCount = sum(x.cartype == CarType.PASSENGER for x in self.connectType)
    #     fuelCount = sum(x.cartype == CarType.FUEL for x in self.connectType)
    #     print('共有' + str(passengerCount) + '節乘客車廂，共有' + str(fuelCount) + '節燃料車廂' )
    def travel(self, hours: int):
        if(int(hours) < 0):
            raise ValueError('教授你可以選擇輸入正確數字')
        if(self.fuel < int(hours) * 10):
            print('燃料不足')
        else:
            self.fuel -= int(hours) * 10
            print('行駛了 ' + str(hours) + ' unit,剩餘' + str(self.fuel) + ' 燃料')
    def refuel(self):
        self.fuel = 100
        print('燃料已補充完畢')
        
class PassengerCar(CarBase):
    def __init__(self,manufacturer,cartype,passenger:int):
        super().__init__(manufacturer,cartype)
        self.passenger = passenger
    def showPassenger(self):
        print('車廂總人數' + str(self.passenger) + '/20人')
    def boarding(self, units):
        if(int(units) < 0):
            raise ValueError('教授你可以選擇輸入正確數字')
        if(self.passenger + int(units) > 20) :
            print('人數已超過車廂最大上限')
        else :
            self.passenger += int(units)
            print('這節車廂目前上車' + units + '人，共' + str(self.passenger) + '人')
    def getoff(self, units):
        if(int(units) < 0):
            raise ValueError('教授你可以選擇輸入正確數字')
        if(self.passenger - int(units) < 0) :
            print('超過車上有的人數，是在哈囉?')
        else :
            self.passenger -= int(units)
            print('這節車廂目前下車' + units + '人，共' + str(self.passenger) + '人' )

class FuelCar(CarBase):
    def __init__(self,manufacturer,cartype,fuel: int):
        super().__init__(manufacturer,cartype)
        self.fuel = fuel
    def showfuel(self):
        print('剩餘' + str(self.fuel) + '/500單位燃料')
    def refuel(self, units):
        if(units < 0):
            raise ValueError('教授你可以選擇輸入正確數字')
        if(self.fuel + units > 500) :
            print('這節車廂共補充' + units + '單位燃料，超過上限燃料已被移除:' + (500 - self.fuel - units))
        else :
            self.fuel += units
            print('這節車廂共補充' + units + '單位燃料')
    def unload(self, units):
        if(units < 0):
            raise ValueError('教授你可以選擇輸入正確數字')
        if(self.fuel - units < 0):
            self.fuel = 0
            print('已卸除全部燃料。')
        else :
            self.fuel -= units
            print('這節車廂共卸除' + units + '單位燃料')

class Car(CarBase):
    def __init__(self,car):
        self.car = car
        self.next = None
        self.pref = None
        return

class Train:
    def __init__(self):
        self.head = None
    def insertLocomotive(self,locomotive):
        if self.head is None:
            locom = Car(locomotive)
            self.head = locom
        else:
            print('Locomotive exists')

    def addCar(self,item):
        if not isinstance(item, Car):
            item = Car(item)
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        return
    def showHead(self):
        self.head.car.showHandler()
