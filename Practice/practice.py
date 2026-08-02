# students = []
# stud1 = input("Enter student 1:")
# stud2 = input("Enter student 2:")
# stud3 = input("Enter student 3:")

# students.append(stud1)
# students.append(stud2)
# students.append(stud3)

# print(students)


# students = []
# for i in range(3):
#     name = input(f"Enter the student {i+1} : ")
#     students.append(name)
    
# print(students)
 
# fruits = ["Apple", "Banana", "Mango", "Orange"]


# for fruit in fruits:
#     print(fruit)


# numbers = [10, 20, 30, 40, 50]

# for number in numbers:
#     print(f"Number = {number}")

# print(numbers)

# cities = ["Delhi", "Mumbai", "Bengaluru"]

# for city in cities:
#     print(f"I live in {city}")
    
# numbers = [5, 10, 15, 20]

# for number in numbers:
#     if (number%2 == 0):
#         print(number)


# marks = [85, 72, 91, 65, 40]
# for mark in marks :
#     print(f"Student Scored {mark} marks")

# numbers = [25, 10, 45, 18, 90, 32]
# largest = numbers[0]

# for number in numbers:
#     if number > largest:
#         largest = number
        
# print(largest)
# numbers = [10, 15, 22, 33, 40, 55, 60]
# count = 0

# for number in numbers:
#     if(number%2 == 0):
#         count = count+1

# print(f"There are total {count} evens")
        
        
# numbers = [10, 15, 22, 33, 40, 55, 60]

# even = 0

# for number in numbers:
#     if (number % 2 == 0):
#         even = even + number
    
# print(even)

# marks = [85, 42, 91, 67, 30, 76, 95]
# total = 0
# highest = marks[0]
# passed = 0
# fail = 0 
# average = 0

# for mark in marks:
#     total = total + mark
      
#     if (mark>highest):
#         highest = mark
    
#     if(mark<50):
#         fail = fail+1
#     else:
#         passed = passed + 1

# average = total/len(marks)
# print(f"Total Marks = {total}")
# print(f"Highest Marks = {highest}")
# print(f"Students passed = {passed}")
# print(f"Students failed = {fail}")
# print(f"Avergae Marks = {average}")

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