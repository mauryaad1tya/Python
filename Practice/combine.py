numbers = [10, 25, 30, 45, 50, 60, 75]
even = []
odd = []
totalEven = 0
totalOdd = 0
sumEven = 0
sumOdd = 0


for number in numbers:
    if number%2 == 0:
        totalEven+=1
        sumEven+=number
        
        even.append(number)
        

    elif number%2 != 0:
        totalOdd+=1
        sumOdd+=number
        odd.append(number)
    
print(f"Even Numbers :{even}")
print(f"Odd Numbers :{odd}")
print(f"Total Even = {totalEven}")
print(f"Total Odd = {totalOdd}")
print(f"Sum of even :{sumEven}")
print(f"Sum of odd :{sumOdd}")
