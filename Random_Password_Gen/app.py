import random
import string


def randpass():
   chars=string.ascii_letters + string.digits +string.hexdigits
   password= "".join(random.choice(chars)) 

   for i in range(length):
       password+=random.choice(chars)
   return password   

print("welcome to password genrator")

length=int(input("Enter the length of password standard is 8 or 16:..   "))
password=randpass()
print(f"your pasword is:",{password})