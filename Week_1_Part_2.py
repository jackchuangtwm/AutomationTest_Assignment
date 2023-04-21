##Write a program which creates a class Student, which contains:

##Attributes

##student_name
##mark1
##mark2
##mark3
##total_marks
##Methods:

##calculate_total(): which calculate the total_marks
##display_student_details(): which display the student name and total marks.
##Try to complete the following program.

class Student:
    def __init__(self, student_name, mark1, mark2, mark3):
        self.student_name = student_name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        self.total_marks = 0
        
    def calculate_total(self):
        self.total_marks = self.mark1 + self.mark2 + self.mark3
        
        print(self.total_marks)
        return self.total_marks
        
    def display_student_details(self):       
        print(self.student_name + ': ' + str(self.total_marks))
        
student_a = Student("Mary", 50, 60, 70)
student_a.calculate_total() # should print 180
student_a.display_student_details() # should print "Mary: 180"



##Assignment 2: Object-Oriented Programming (Python)
##Create a class called Animal is designed to model an animal.
##It contains an attribute sound and two methods get_sound() and get_type().
##get_type(): print out "I am animal."
##get_sound(): print out "Hello World"
##Create two subclasses of Animal called Dog and Cat.
##Dog class:
##override the method get_sound(). The Sound of Dog is "Woof! Woof!"
##contains a method catch_cat(): print out "I caught a cat."
##Cat class:
##override the method get_sound(). The sound of cat is "Meow! Meow!"
##contains a method catch_mouse(): print out "I caught a mouse."
##Try to complete the following program.


class Animal:       

    def __init__(self): 
        self.sound = "Hello World"

    def get_type(self):
         print("I am animal.")

    def get_sound(self):
        print(self.sound)
    
class Dog(Animal):
    def get_sound(self):
        self.sound = "Woof! Woof!"
        print(self.sound)
    
    def catch_cat(self):
        print("I caught a cat.")

class Cat(Animal):
    def get_sound(self):
        self.sound = "Meow! Meow!"
        print(self.sound)
    
    def catch_mouse(self):
        print("I caught a mouse.")


dog = Dog()
dog.get_type()  # Print "I am animal"
dog.get_sound() # Print "Woof! Woof!"
dog.catch_cat() # Print "I caught a cat."

cat = Cat()
cat.get_type()  # Print "I am animal" 
cat.get_sound() # Print "Meow! Meow!"
cat.catch_mouse() # Print "I caught a mouse."

animal = Animal()
animal.get_sound() # Print "Hello World"



##Assignment 3: Object-Oriented Programming (Python)
##Create a class named Course that has attributes：
##title
##instructor
##price
##lectures
##users (list type)
##ratings
##avg_rating
##Implement these methods:
##new_user_enrolled()
##received_a_rating()
##show_details()
##From the above class, inherit two classes:
##VideoCourse: contains attribute length_video
##PdfCourse: contains attribute page

class Course:
    def __init__(self, title, instructor, price, lectures):
        self.title = title
        self.instructor = instructor
        self.price = price
        self.lectures = lectures
        self.users = []
        self.ratings = []
        self.avg_rating = 0

    def new_user_enrolled(self, user):
        self.users.append(user)

    def received_a_rating(self, ratings):
        self.ratings.append(ratings)
        self.avg_rating = sum(self.ratings) / len(self.ratings)

    def show_details(self):
        print("Course Title: " + self.title)
        print("Instructor : " + self.instructor)
        print("Price : $" + str(self.price))
        print("Number of Lectures: " + str(self.lectures))
        print("Users: " + str(self.users))
        print("Average rating :  " + str(self.avg_rating))


class VideoCourse(Course):
    def __init__(self, title, instructor, price, lectures, video_length):
        super().__init__(title, instructor, price, lectures)
        self.video_length = video_length
        
    def show_details(self):
        super().show_details() 
        print("Video Length: " +  str(self.video_length))

class PdfCourse(Course):
    def __init__(self, title, instructor, price, lectures, pages):
        super().__init__(title, instructor, price, lectures)
        self.pages = pages
        
    def show_details(self):
        super().show_details() 
        print("Pages: " +  str(self.pages))

  
vc = VideoCourse('Learn C++', 'Miss A', 5000, 30, 1000)
vc.new_user_enrolled('Student A')
vc.new_user_enrolled('Student B')
vc.new_user_enrolled('Student C')
vc.received_a_rating(3)
vc.received_a_rating(5)
vc.received_a_rating(4)
vc.show_details()

pc = PdfCourse('Learn Java', 'Mr B', 8000, 35, 100)
pc.new_user_enrolled('Student X')
pc.new_user_enrolled('Student Y')
pc.new_user_enrolled('Student Z')
pc.received_a_rating(5)
pc.received_a_rating(4)
pc.received_a_rating(4.5)
pc.show_details()



##Assignment 4: Python Basic - Sum of Factorials (Advanced Optional)
##Write a script to find the sum of factorials. (I.e. 1! + 2! + 3! … = ?)

def find_sum_of_factorials(number): 
    sum = 0
    factorials = 1

    for i in range(1, number + 1):
        sum += factorials
        factorials *= i+1

    return sum

print(find_sum_of_factorials(3))  # = 1! + 2! + 3!, =  1 + 1 x 2 + 1 x 2 x 3,  should print 9
print(find_sum_of_factorials(1))  # should print 1
print(find_sum_of_factorials(5))  # should print 153

