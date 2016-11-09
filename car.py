class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
             self.tax = 0.12
        self.display_all()
    def display_all(self):
        print'\nPrice:', str(self.price), "\nSpeed:", self.speed, "\nFuel:", self.fuel, "\nMileage:", self.mileage, "\nTax:", self.tax
#print with () use + and \n to get on sepreate lines
#print without () use comas and \n to get on seprate lines

car1 = Car(2000, "35mph", "Full", "15mpg")
car2 = Car(2000, "5mph", "Not Full", "105mpg")
car3 = Car(2000, "15mph", "Kind of Full", "25mph")
car4 = Car(2000, "25mph", "Full", "25mpg")
car5 = Car(2000, "45mph", "Empty", "25mpg")
car6 = Car(20000000, "35mph", "Empty", "15mpg")
