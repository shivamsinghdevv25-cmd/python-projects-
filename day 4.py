numbers=[]
even_count=0
odd_count=0

for x in range (1,6):
    n=int(input(f"Enter a number {x}: "))
    numbers.append(n)

    if n%2==0:
        print(f"{n} is even")
        even_count+=1
    else:
        print(f"{n} is odd")
        odd_count+=1
        
    if n>0:
     print(f'the number {n} is positive')

    elif n<0:
     print(f'the number {n} is negative')
    else:
        print(f'the number {n} is zero')
    
    
print("Total even numbers:",even_count)
print("Total odd numbers:",odd_count)
print("the biggest number is ",max(numbers ))





 

                   

            