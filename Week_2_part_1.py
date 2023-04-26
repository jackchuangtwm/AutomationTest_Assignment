#Assignment 1: Excel Application
#Part 1
#There is a score table of the English students.
#Student	Reading	Listening	Speaking	Writing
#Student A	80	75	88	80
#Student B	88	86	90	95
#Student C	92	85	92	98
#Student D	81	88	80	82
#Student E	75	80	78	80
#Generate a spreadsheet for the score table using Python.

import ast
import pandas as pd

score_record = pd.DataFrame({'Student': {0: 'Student A', 1: 'Student B', 2: 'Student C',
                                         3: 'Student D', 4: 'Student E'},
                              'Reading': {0: 80, 1: 88, 2: 92, 3: 81, 4: 75},
                              'Listening': {0: 75, 1: 86, 2: 85, 3: 88, 4: 80},
                              'Speaking': {0: 88, 1: 90, 2: 92, 3: 80, 4: 78},
                              'Writing': {0: 80, 1: 95, 2: 98, 3: 82, 4: 80}})

file_name = 'score.xlsx'
score_record.to_excel(file_name, index=False)



#Part 2
#The below table presents the weights of different section of the score.
#Section	Weight
#Reading	20%
#Listening	25%
#Speaking	30%
#Writing	25%
#Write a Python script to read the value from spreadsheet, and calculate the Weighted Average for each student.

#Expected Output:
#student: Student A, score: 81.15
#student: Student B, score: 89.85
#student: Student C, score: 91.75
#student: Student D, score: 82.7
#student: Student E, score: 78.4

import pandas as pd

Weight = {'Reading': 0.2, 'Listening': 0.25, 'Speaking': 0.3, 'Writing': 0.25}

excelPath = r'score.xlsx'  # read file
xls = pd.ExcelFile(excelPath)
sheet_names = xls.sheet_names

for sheet_name in sheet_names:
    df = pd.read_excel(excelPath, sheet_name=sheet_name)

    print(f"Sheet: {sheet_name}")

    for index, row in df.iterrows():
        weighted_sum = 0
        student_name = row['Student']

        for key, value in Weight.items():
            weighted_sum += row[key] * value

        print(f"  student: {student_name}, score: {weighted_sum}")  



#Assignment 2: Exception Handling
#Complete the following functions by Python

#division(): print the result of division.
#Throw ZeroDivisionError if y is 0.
#Throw TypeError if y is not an integer.
#Whether an exception occurs or not, it will Print "---Finish---"

def division(x, y):
    try:
        if type(y) is not int:
          raise TypeError()
        
        num = x/y
        print(num)
    
    except ZeroDivisionError as msg:
        print("y cannot be 0")

    except TypeError as msg:
         print("y should be integer")
    
    except:
        print("Error")

    finally:
        print("---Finish---")


division(100, 10)   # Should print 10.0 and "---Finish---"
division(100, 0)    # Should Throw ZeroDivisionError, print "y cannot be 0" and "---Finish---"
division(100, "a")  # Should Throw TypeError, print "y should be integer" and "---Finish---"



# Assignment 3: Algorithm Practice (Advanced Optional)
# Given an array nums.
# We define a running sum of an array as running_sum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

def running_sum(nums):  

    for i in range(1, len(nums)):
       nums[i] += nums[i - 1]

    return nums


print(running_sum([1, 2, 3, 4])) # Should be [1, 3, 6, 10] because [1, 1+2, 1+2+3, 1+2+3+4]
print(running_sum([1, 1, 1, 1, 1])) # Should be [1, 2, 3, 4, 5]
print(running_sum([3, 1, 2, 10, 1])) # Should be [3, 4, 6, 16, 17]