class Car():
    def __init__(self,year,brand,color):
        self.year = year
        self.brand = brand
        self.color = color
        self.miles = 0
 
    def get_name(self): # 印出名字
        print(str(self.year) +" "+ self.brand)

    def get_mile(self): # 存取公里數
        print("Your "+self.brand+" has "+str(self.miles)+" miles on it")
        
    def update_mile(self,mileage): # 更新公里數
        self.miles = mileage
        
    def add_mile(self,kilometer): # 增加公里數
        self.miles += kilometer
        
    def fill_gas(self): # 車子加油
        print("This car need a gas tank")