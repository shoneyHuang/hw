from hw1 import Locomotive,PassengerCar,FuelCar,CarType,CarBase

class Car(CarBase):
    def __init__(self,car,carnum):
        self.car = car
        self.next = None
        self.previous = None
        self.carnum = carnum
        return

class Train:
    def __init__(self):
        self.head = None
    def createTrain(self,locomotive):
        if self.head is None:
            self.head = Car(locomotive,self.getCarCount()+1)
        else:
            print('Locomotive exists')
    def getCarCount(self):
        temp = self.head
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count
    def traversal(self):
        pointer = self.head
        print("這是火車頭")
        pointer.car.showmanufacturer()
        pointer.car.showHandler()
        pointer.car.showfuel()

        if pointer.next is not None:
            print("aaaaaaaaa")
            pointer = pointer.next
            while(pointer):
                typeTrans = '燃料' if pointer.car.cartype == CarType.FUEL else '乘客'
                if(pointer.car.cartype == CarType.FUEL):
                    print('這是第' + str(pointer.carnum) + '節' + typeTrans + '車廂')
                    pointer.car.showmanufacturer()
                    pointer.car.showfuel()
                else:
                    print('這是第' + str(pointer.carnum) + '節' + typeTrans + '車廂')
                    pointer.car.showmanufacturer()
                    pointer.car.showPassenger()
                pointer = pointer.next

    def addCar(self,x,data):
        if self.head is None:
            print("Please init Locomotive first")
        else:
            n = self.head
            while n is not None:
                if n.car == x:
                    break
                n = n.nref
            if n is None:
                print("car not in the train")
            else:
                newCar = Car(data,self.getCarCount())
                newCar.previous = n
                newCar.next = n.next
                if n.next is not None:
                    n.next.previous =  newCar
                n.next = newCar
    def deleteCar(self,x):
        if self.head is None:
            print("The train has no element to delete")
            return
        if self.head.next is None:
            if self.head.car == x:
                self.head = None
            else:
                print("Car not found")
            return
        if self.head.car == x:
            self.head = self.head.next
            self.head.previous = None
            return
        
        n = self.head
        while n.next is not None:
            if n.car == x:
                break
            n = n.next
        if n.next is not None:
            n.previous.next = n.next
            n.next.previous = n.previous
        else:
            if n.car == x:
                n.previous.next = None
            else :
                print("Car not found")
    def showHead(self):
        self.head.car.showHandler()
