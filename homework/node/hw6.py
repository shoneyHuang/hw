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

    #get count of cars in train
    def getCarCount(self):
        temp = self.head
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count

    #show all cars in train
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

    #check index exists in train
    def checkCar(self,index):
        pointer = self.head
        while (pointer):
            if pointer.carnum == index:
                return True
            pointer = pointer.next
        return False

    # can ignore showing error msg when car not exist 
    def addCar(self,index,data):
        if self.head is None:
            print("Please init Locomotive first")
        else:
            pointer = self.head
            # get specific number exists in linked list or not
            while pointer is not None:
                if pointer.carnum == index:
                    index += 1
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

    # can ignore showing error msg when car not exist 
    def deleteCar(self,index):
        if self.head is None:
            print("Please init Locomotive first")
            return
        else:
            pointer = self.head
            # if no other car 
            if pointer.next is None:
                if index == 1:
                    print("火車頭刪屁刪喔？")
                else:
                    print("目前只剩火車頭")
                return
            #get delete target
            pointer = pointer.next
            while(pointer):
                if pointer.carnum == index:
                    break
                pointer = pointer.next
            #if target next exists, connect previous and next then renumbering
            if pointer.next is not None:
                pointer.previous.next = pointer.next
                pointer.next.previous = pointer.previous
                pointer.next.carnum = index

                pointer = pointer.next.next
                while(pointer):
                    index+=1
                    pointer.carnum = index
                    pointer = pointer.next
            #else clean previous car's next
            else:
                if pointer.carnum == index:
                    pointer.previous.next = None
                else :
                    print("車廂不存在")

    # chang locomotive
    def changeLocomotive(self,locomotive):
        if self.head is None:
            self.head = Car(locomotive,self.getCarCount()+1)
        else:
            self.head.car = locomotive
