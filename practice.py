# lab exam programs

# 1. Declare a base class to calculate Resistance from voltage and current and extend the class to calculate inductance and capacitance with varying voltage and current values with respect to time.
import math
class resistance1:
    def __init__(self,voltage,current):
        self.voltage= voltage
        self.current= current
    def resistance2(self):
        if self.current!=0:
            return self.voltage/self.current
        else:
            print("invalid values")
class inductance1(resistance1):
    # def __init__(self,voltage,current):  #without these also it's fine
    #     super().__init__(voltage,current)
    def inductance2(self,frequency):
        self.frequency= frequency
        if self.frequency!=0 and self.current!=0:
            return self.voltage/(2*math.pi*self.current*self.frequency)
        else:
            print("invalid values")
class capacitance1(resistance1):
    # def __init__(self,voltage,current):
    #     super().__init__(voltage,current)
    def capacitance2(self,frequecy):
        self.frequency= frequecy
        if self.voltage!=0 and self.frequency!=0:
            return self.current/(2*math.pi*self.frequency*self.voltage)
        else:
            print("invalid values")
# calculating answers
a= resistance1(220,0.1)
a1= a.resistance2()
print(f"value of resistance is {a1} Ohm")
b= inductance1(220,0.1)
b1= b.inductance2(50)
print(f"value of inductance is {b1} Henry")
c= capacitance1(220,0.1)
c1= c.capacitance2(50)
print(f"value of capacitor is {c1} Farads")

# # 2. By using the concept of inheritance compose a program to find the area of triangle, circle and rectangle.  
# import math
# class shape:
#     def __init__(self,shape):
#         self.shape= shape
# class triangle(shape):
#     def triangle1(self,base,height):
#         self.base= base
#         self.height= height
#         print(f"area of {self.shape} is {0.5*self.base*self.height}")
# class circle(shape):
#     def circle1(self,radius):
#         self.radius= radius
#         print(f"area of {self.shape} is {math.pi*self.radius**2}")
# class rectangle(shape):
#     def rectangle1(self,length,breadth):
#         self.lenght= length
#         self.breadth= breadth
#         print(f"area of {self.shape} is {self.lenght*self.breadth}")

# a= triangle("traingle")
# a1= a.triangle1(10,10)
# b= circle("circle")
# b1= b.circle1(10)
# c= rectangle("rectangle")
# c1= c.rectangle1(10,10)

# 3. 
