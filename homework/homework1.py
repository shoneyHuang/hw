class Train():
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
    def showManufacturer(self):
        print(self.manufacturer)

class Locomotive(Train):
    def __init__(self,manufacturer,handler,fuel,connectType):
        super().__init__(manufacturer)
        self.handler = handler
        self.fuel = fuel
        self.connectType = connectType
    def showHandler(self):
        print(self.handler)
    def showfuel(self):
        print('剩餘 : ' + str(self.fuel) + '燃料')
    def showConnectType(self):
        print(self.connectType)
    def travel(self, hours):
        if(hours < 0):
            raise ValueError('教授你可以選擇輸入正確數字')
        if(self.fuel < hours * 10):
            print('燃料不足')
        else:
            self.fuel -= hours * 10
            print('行駛了 ' + hours + ' unit,剩餘' + self.fuel + ' 燃料')
    def refuel(self):
        self.fuel = 100
        print('燃料已補充完畢')
        
class PassengerCar(Train):
    def __init__(self,manufacturer,passenger):
        super().__init__(manufacturer)
        self.passenger = passenger
    def showPassenger(self):
        print(self.passenger + '人')
    def boarding(self, units):
        if(units < 0):
            raise ValueError('教授你可以選擇輸入正確數字')
        if(self.passenger + units > 20) :
            print('人數已超過車廂最大上限')
        else :
            self.passenger += units
            print('這節車廂目前上車' + units + '人，共' + self.passenger + '人')
    def getoff(self, units):
        if(units < 0):
            raise ValueError('教授你可以選擇輸入正確數字')
        if(self.passenger - units < 0) :
            print('超過車上有的人數，是在哈囉?')
        else :
            self.passenger -= units
            print('這節車廂目前下車' + units + '人，共' + self.passenger + '人' )

class FuelCar(Train):
    def __init__(self,manufacturer,fuel):
        super().__init__(manufacturer)
        self.fuel = fuel
    def showfuel(self):
        print(self.fuel + '單位燃料')
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