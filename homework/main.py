from homework1 import Train,Locomotive,PassengerCar,FuelCar,CarType
from homework2 import traversal,addNodeAtEnd
from homework3 import userinterface

car = []
car.append(FuelCar('B Manufactor',CarType.FUEL,100))
car.append(FuelCar('B Manufactor',CarType.FUEL,150))
car.append(FuelCar('A Manufactor',CarType.FUEL,200))
car.append(PassengerCar('C Manufactor',CarType.PASSENGER,10))
car.append(PassengerCar('A Manufactor',CarType.PASSENGER,15))
car.append(PassengerCar('B Manufactor',CarType.PASSENGER,7))
car.append(FuelCar('A Manufactor',CarType.FUEL,250))
car.append(FuelCar('C Manufactor',CarType.FUEL,300))
car.append(FuelCar('C Manufactor',CarType.FUEL,447))

x = Locomotive('A Manufactor',CarType.LOCOMOTIVE,'shoney huang',10,car)
addNodeAtEnd(x,'D Manufactor',CarType.FUEL,70)
addNodeAtEnd(x,'D Manufactor',CarType.PASSENGER)

traversal(x)


userinterface()