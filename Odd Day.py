#Write a python program to count the numbers of even and odd numbers from a series of numbers
numbers=(3,5,8,6,3,1)
count_odd = 0
count_even = 0
for x in numbers:
        if x%2==1:
            count_even+=1
        else:
            count_odd+=1
print("No. of even numbers :",count_even)
print("No. of odd numbers :",count_odd)