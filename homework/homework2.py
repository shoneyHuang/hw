from homework1 import Train,Locomotive,PassengerCar,FuelCar,CarType
def traversal(locomotive : Locomotive):
    print('這是火車頭')
    locomotive.showmanufacturer()
    locomotive.showHandler()
    locomotive.showfuel()
    locomotive.showConnectType()
    print('-----------------')

    count = 2
    for x in locomotive.connectType:
        typeTrans = '燃料' if x.cartype == CarType.FUEL else '乘客'
        if(x.cartype == CarType.FUEL):
            print('這是第' + str(count) + '節' + typeTrans + '車廂')
            x.showmanufacturer()
            x.showfuel()
        else:
            print('這是第' + str(count) + '節' + typeTrans + '車廂')
            x.showmanufacturer()
            x.showPassenger()
        count += 1
        print('-----------------')

def addNodeAtEnd(locomotive : Locomotive,manufacturer,addType: CarType,fuel = 0):
    if(addType == CarType.PASSENGER):
        locomotive.connectType.append(PassengerCar(manufacturer,addType,0))
    if(addType == CarType.FUEL):
        if(int(fuel) > 500 or int(fuel) < 0):
            print('燃料車廂要給正確的燃料')
        else:
            locomotive.connectType.append(FuelCar(manufacturer,addType,fuel))
