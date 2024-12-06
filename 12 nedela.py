
import random
n=5
lielaka_summa=0
for i in range(n):
    a=random.randint(1, 6)
    b=random.randint(1, 6)
    print (a,b, a+b)
   
    if (a+b)>lielaka_summa:
        lielaka_summa= a+b
        print()
        
    if(a+b)> lielaka_summa:
        lielaka_summa =(a+b)
    
    
print(f"Lielākā summas vērtība: {lielaka_summa}")
print(f"summa{a}")



        
        
        
import random

computer_number = random.randint(1, 100)

attempts = 0

print("Uzmini skaitli no 1 līdz 100")

while True:
    user_guess = int(input("Tavs minējums: "))
    attempts += 1

    if user_guess < computer_number:
         print("Lielāks")
    elif user_guess > computer_number:
        print("Mazāks")
    else:
        print("Uzminēts! Skaitlis bija .")
        print("Minēšanas reižu skaits")
        break
       
