# lab exam programs

# # 1. Declare a base class to calculate Resistance from voltage and current and extend the class to calculate inductance and capacitance with varying voltage and current values with respect to time.
# import math
# class resistance1:
#     def __init__(self,voltage,current):
#         self.voltage= voltage
#         self.current= current
#     def resistance2(self):
#         if self.current!=0:
#             return self.voltage/self.current
#         else:
#             print("invalid values")
# class inductance1(resistance1):
#     # def __init__(self,voltage,current):  #without these also it's fine
#     #     super().__init__(voltage,current)
#     def inductance2(self,frequency):
#         self.frequency= frequency
#         if self.frequency!=0 and self.current!=0:
#             return self.voltage/(2*math.pi*self.current*self.frequency)
#         else:
#             print("invalid values")
# class capacitance1(resistance1):
#     # def __init__(self,voltage,current):
#     #     super().__init__(voltage,current)
#     def capacitance2(self,frequecy):
#         self.frequency= frequecy
#         if self.voltage!=0 and self.frequency!=0:
#             return self.current/(2*math.pi*self.frequency*self.voltage)
#         else:
#             print("invalid values")

# # calculating answers
# a= resistance1(220,0.1)
# a1= a.resistance2()
# print(f"value of resistance is {a1} Ohm")
# b= inductance1(220,0.1)
# b1= b.inductance2(50)
# print(f"value of inductance is {b1} Henry")
# c= capacitance1(220,0.1)
# c1= c.capacitance2(50)
# print(f"value of capacitor is {c1} Farads")



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



# # 3. Program to find the best of two test average marks out of three test’s marks accepted from the user.
# a= int(input("enter marks in test1: "))
# b= int(input("enter marks in test2: "))
# c= int(input("enter marks in test3: "))
# if a<b and a<c:
#     print(f"average of best 2 test is: {(c+b)/2}")
# elif b<c and b<a:
#     print(f"average of best 2 test is: {(a+c)/2}")
# elif c<b and c<a:
#     print(f"average of best 2 test is: {(a+b)/2}")


# # 4. Program to generate a Fibonacci sequence up to a specified length.  
# a= 0
# b= 1
# l=6
# print(f"fibonocci sequence is {a},{b}",end="")
# for i in range(l-2):
#     c=a+b
#     print(f",{c}",end="")
#     a=b
#     b=c


# # 5.Develop a program to check whether a given number is Palindrome or not.
# a= input("enter a string: ")
# b=a[::-1]
# if (a)==(b):
#     print("yes it is  palindromes")
# else: 
#     print("no, it is not palindrome")

# #6.develop a program to convert
# # a. Binary to Decimal
# a= input("enter a binary number: ")
# b= a[::-1]
# l= len(a)
# ans=0
# for i in range (l):
#     ans+= (2**i)*int(b[i])
# print(f"decimal equivalent of {a} is {ans}")

# #b. decimal to binary
# a= int(input("enter a decimal number: "))
# binary=""
# if a==0:
#     print("binary equivalent is 0")
# else:
#     while(a>0):
#         remainder= a%2
#         binary= str(remainder)+binary
#         print(f"stage1:{binary}")
#         a= a//2
#         print(a,"....")
# print(f"binary equivalent of {a} is {binary}")

# #c. Decimal to Octal
# a= int(input("enter a decimal number: "))
# octal=""
# if a==0:
#     print("octal equivalent is 0")
# else:
#     while(a>0):
#         remainder= a%8
#         octal= str(remainder)+octal
#         a= a//8
# print(f"octal equivalent of {a} is {octal}")

# # d. octal to decimal
# a= input("enter a octal number: ")
# b= a[::-1]
# l= len(a)
# ans=0
# for i in range (l):
#     ans+= (8**i)*int(b[i])
# print(f"decimla equivalent of {a} is {ans}")

# # e. hexadecimal to decimal
# a= input("enter hexadecimal number: ") 
# b= a[::-1]
# l= len(a)
# ans=0
# map= "0123456789ABCDEF"
# for i in range (l):
#     ans+= (16**i)*map.index(b[i])
# print(f"decimal equivalent of {a} is {ans}")

# f. decimal to hexadecimal
a= int(input("enter decimal value: "))
map= "0123456789ABCDEF"
hexadecimal= ""
if a==0:
    print("0")
else:
    while(a>0):
        remainder= a%16
        hexadecimal= map[remainder] + hexadecimal
        a= a//16
print(f"hexadecimal equivalent is {hexadecimal}")

    

