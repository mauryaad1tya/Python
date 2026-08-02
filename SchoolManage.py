numbers = [25, 18, 90, 12, 75, 81, 64]

largest = numbers[0]
smallest = numbers[0]
sum = 0
even = 0
odd = 0
num = 0

for number in numbers:
    num +=1
    if number>largest:
        largest = number
    
    if number<smallest:
        smallest = number
    
    sum +=number
    
    if number % 2 == 0:
        even +=1
    else:
      odd +=1

average = sum/num

print(num)
print(f"Largest Number = {largest}")
print(f"Smallest Number = {smallest}")
print(f"Sum = {sum}")
print(f"Average = {average}")
print(f"Even Numbers = {even}")
print(f"Odd Numbers = {odd}")