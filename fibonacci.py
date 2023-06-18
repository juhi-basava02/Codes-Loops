#write a python program to get the fibonacci series between 0 to 50
num_fib = int(input("enter the range number: "))
first_val = 0
second_val = 1
for n in range(0,num_fib) :
        if(n <= 1) :
         next = n
        else:
        next = first_val + second_val
        first_val = second_val
        second_val = next
        print(next)  
