##Assignment 1
##Write a script to complete the following function

##check_bmi(): calculate the BMI value, and return True if BMI between 18.5 and 24. Otherwise, return False
##Formula: BMI = Weight(kg) / height2 (m)

def check_bmi(height, weight):

    bmi = weight / (height * height);

    if bmi >= 18.5 and bmi <= 24:
        return True;
    else:
        return False;


print(check_bmi(1.6, 60));   # print True
print(check_bmi(1.6, 40));   # print False
print(check_bmi(1.6, 100));  # print False





##Assignment 2
##Assuming your monthly salary is $25,000, and the salary is adjusted by 3% every year. 
##Write a Python script to calculate how many years it takes for your salary to double?

salary = 25000;
count = 0;

while salary <= 50000:
    salary *= 1.03;
    count += 1;

print (count);





##Assignment 3
##We wrote a function which can find the position of the target number inside a list of numbers. Actually, if the list was Sorted already, there is a beautiful algorithm called Binary Search which can do this job efficiently.
##You can try to look up these keywords and learn the concept behind this algorithm and write the code by yourself. For simplicity, you can assume that there are no duplicate numbers in the given array. It could be a bit of a challenge if you haven’t learned any algorithm.

#def binary_search_position(numbers, target): 
    # your code here 

#print(binary_search_position([1, 2, 5, 6, 7], 1)) # should print 0 
#print(binary_search_position([1, 2, 5, 6, 7], 6)) # should print 3

def binary_search_position(data, key):
    low = 0;
    upper = len(data) - 1;
       
    while low <= upper:
        mid = int((low + upper) / 2);

        if key > data[mid]:
            low = mid + 1;
        elif key < data[mid]:
            upper = mid - 1;
        else:
            #data[mid] = key
            return ("Index: " + str(mid));

    return ("找不到數值");

print(binary_search_position([1, 2, 5, 6, 7], 1));
print(binary_search_position([1, 2, 5, 6, 7], 6));



##Assignment 4 (Advanced Optional)
##Complete the Python script to print a pyramid of relative levels according to the parameters.


def draw_pyramid(number): 
    for i in range(number):
        for j in range(number - i -1):
            print(" ", end = "");
        for k in range((2 * i) + 1):
            print("*", end = "");
        print();


draw_pyramid(3);
draw_pyramid(5);

