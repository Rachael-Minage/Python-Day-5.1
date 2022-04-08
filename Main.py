#For loop
fruits = ["Apples","Guavas","Pears","Mangoes","Watermelons"]
for fruit in fruits:
    print(fruit)
    print(fruit +" pie")
    print(fruits)

#Calculate average height using for loop

student_heights= input("Enter the list of student's heights\n").split()
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
total_height=0
for height in student_heights:
    total_height= total_height+height
print(total_height)  

number_of_students = 0
for student in student_heights:
    number_of_students = number_of_students+1
print(number_of_students)

average_height =round(total_height/number_of_students)
print(f"The average height is:{average_height}")

#Highest score
Student_scores= input("Enter student scores:\n").split()
for n in range(0,len(Student_scores)):
    Student_scores[n]= int(Student_scores[n])
print(Student_scores)

highest_score =0
for score in Student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score is:{highest_score}")

#For loop in range
from unicodedata import digit


for number in range(1,10):
    print(number)

sum_of_numbers = 0
for number in range(0,101):
    sum_of_numbers=sum_of_numbers+number 
print(sum_of_numbers) 
#Calculate the sum of even numbers between 1 and 100
numbers=0
for number in range(1,101):
    if number%2==0:
        numbers= numbers+number
print(numbers)

#FizzBuzz game
print("Welcome to fizzbuzz game")
totals=0
for total in range(1,101):
    if total%3==0 and total%5==0:
        print("FizzBuzz")
    elif total%5==0:
        print("Buzz")
    elif total%3 ==0:
        print("Fizz")
    else:
        print(f"{total}")
            
  



