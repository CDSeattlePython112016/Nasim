class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print(self.price, self.max_speed, self.miles)
        return self
    def ride(self):
        self.miles +=10
        print ("Riding")
        return self
    def reverse(self):
        self.miles -=5
        print("Reversing")
        return self

bike1 = Bike(100, "25mph")
bike1.ride().ride().ride().reverse().displayinfo()

bike2 = Bike(200, "35mph" )
bike2.ride().ride().reverse().reverse().displayinfo()

bike3 = Bike(300, "40mph")
bike3.reverse().reverse().reverse().displayinfo()
