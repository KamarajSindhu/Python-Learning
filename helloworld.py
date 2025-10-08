'''a ="hello"
b= "world"
c= a+b
print(c)'''

N=input("Name:")
C=input("Class: ") 
T= int(input("Tamil: "))
E = int(input("English: "))
M = int(input("Maths: "))
SC = int(input("Science: "))
S = int(input("Social: "))
T= T+E+M+SC+S
AVG = T/5
print ("Total:",T)
print ("Average:",AVG)
if T<250:
    print("GRADE C")
elif(T<400):
    print("GRADE B")
else:
    print("GRADE A")






