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
    def checkCar(self,specificNum):
        pointer = self.head
        while (pointer):
            if pointer.carnum == specificNum:
                return True
        return False

    def addCar(self,specificNum,data):
        if self.head is None:
            print("Please init Locomotive first")
        else:
            pointer = self.head
            index = 1
            # get specific number exists in linked list or not
            while pointer is not None:
                index += 1
                if pointer.carnum == specificNum:
                    break
                pointer = pointer.next

        
            if pointer is None:
                print("car not in the train")
            else:
                #set new car : previos = pointer and next = pointer.next
                newCar = Car(data,index)
                newCar.previous = pointer
                newCar.next = pointer.next
                #if pointer next car is not null, set next car's previous = new car
                if pointer.next is not None:
                    pointer.next.previous =  newCar
                #and set pointer.next = new car, then renumbering
                pointer.next = newCar

                pointer = pointer.next.next
                while(pointer):
                    index += 1
                    pointer.carnum = index
                    pointer = pointer.next

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
