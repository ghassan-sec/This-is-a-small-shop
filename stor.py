print("="*20)
print("Welcom TO The Golden Shoes")
print("="*20)

name_custmor = input("Enter your name custmor : ")

with open("golden.txt" ,"a") as G :
     G.write("\n" + name_custmor)

shoes_type = input("what type of shose do you want (sports/formal/sandals) : ")
if shoes_type == "sport":
     price = 50
elif shoes_type == "formal":
     price = 70
elif shoes_type == "sandals":
     price = 30
else:
     price = 0          
size = input("Enter your size : ")
color = input("Enter color (black/white/brown) : ")


if color == "black":
     print("The shoes is available")
else:
     print("We will order it for you")

print("\n------Invoice------")

print("Name Customer", name_custmor)  
print("Type Shose", shoes_type)
print("price", price , "$")
print("Size ", size)
print("color", color)

print("Thank you for shopping with US !")
