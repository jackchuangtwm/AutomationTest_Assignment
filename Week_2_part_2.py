# Part 2: Write a Python script to CRUD (Create, Read, Update, Delete) user data.
# Connecting to MySQL server
# Create a user data with email and password
# Get user id by selecting user data by email
# Update user password and select the user data to check if password has been changed.
# Delete user by user id and select the user data to check if the user has been deleted.
# Reminder: In this assignment, you should hand in an additional data file in SQL format by mysqldump tool.

class DbSetting():
    def __init__(self):
        self.db_info = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "a123456",
        "db": "assignment",
        "charset": "utf8"
    }

import pymysql
from pymysql.cursors import DictCursor

class InsertModel(DbSetting):

    def insert_user(self, email, password):
        try:
            # 建立Connection物件
            conn = pymysql.connect(**self.db_info)
            
            # 建立Cursor物件
            with conn.cursor() as cursor:
                #資料表相關操作，新增資料SQL語法                
                command = "INSERT INTO user (email, password) VALUES('" + email + "', '" + password + "');"
                    
                #執行指令
                i = cursor.execute(command)
                
                if i == 1:
                    print('insert success')
                else:
                    print('insert failed')         
                #儲存變更
                conn.commit()
                #關閉DB連線
                conn.close()

        except Exception as ex:
            print(ex)

class SelectModel(DbSetting):

    def select_all_user(self):
        try:
            conn = pymysql.connect(**self.db_info)

            with conn.cursor() as cursor:
                         
                command = "SELECT * FROM user;"       
                cursor.execute(command)      
                #取得所有資料
                result = cursor.fetchall()
                conn.commit()
                conn.close()

                print(result)

        except Exception as ex:
            print(ex)

    def select_user_id_by_email(self, email):
        try:
            conn = pymysql.connect(**self.db_info)

            with conn.cursor() as cursor:
                         
                command = "SELECT id FROM user WHERE email='" + email + "';"       
                i = cursor.execute(command)      
                
                if i <= 0:
                    print('no data')
                else:
                    #取得所有資料
                    result = cursor.fetchall()
                    return result
                
                conn.commit()
                conn.close()                

        except Exception as ex:
            print(ex)

    def select_user_email_by_id(self, id):
        try:
            conn = pymysql.connect(**self.db_info)

            with conn.cursor() as cursor:
                         
                command = "SELECT * FROM user WHERE id='" + str(id) + "';"       
                i = cursor.execute(command)      
                
                if i <= 0:
                    print('id = ' + str(id) + ' is not exist')
                else:
                    #取得所有資料
                    result = cursor.fetchall()
                    print(result)
                
                conn.commit()
                conn.close()                

        except Exception as ex:
            print(ex)

class UpdateModel(DbSetting):
    def update_user_password_by_email(self, email, old_password, new_password):

        if new_password == old_password:
            print("old and new passwords are the same, password nochange")
        else:   
            try:
                conn = pymysql.connect(**self.db_info)

                with conn.cursor() as cursor:

                    #取得所有符合的資料
                    command = "SELECT id FROM user WHERE email='" + email + "' AND password='" + old_password + "';" 
                    i = cursor.execute(command)               
                   
                    if i <= 0:
                        print('no match data')
                    else:
                        result = cursor.fetchall()
                        data = list(result)

                        #更改密碼
                        for (id,) in data:
                             command = "UPDATE user SET password='" + new_password + "' WHERE id='" + str(id) + "';"
                             cursor.execute(command) 
                             print(f'updated id={id} to new password: {new_password}')

                        conn.commit()
                        conn.close()

            except Exception as ex:
                print(ex)
    
class DeleteModel(DbSetting):
    def delete_user_by_id(self, id):
        try:
            conn = pymysql.connect(**self.db_info)
            
            with conn.cursor() as cursor:
               
                command = "DELETE FROM user WHERE id='" + str(id) + "';" 
                i = cursor.execute(command)  

                if i<=0:
                    print('no data was deleted')
                
                else:
                    print(f'id = {id} is deleted')
                    check_id = SelectModel()
                    check_id.select_user_email_by_id(id)

                conn.commit()
                conn.close()          

        except Exception as ex:
            print(ex)       


# ins = InsertModel()
# ins.insert_user('jack_11', 'password')

# select = SelectModel()
# select.select_all_user()
# select.select_user_id_by_email("jac77k_01@twm.com")
# select.select_user_email_by_id(7)

# update = UpdateModel()
# update.update_user_password_by_email('jack_01@twm.com', 'a123456', 'a123457')

# delete = DeleteModel()
# delete.delete_user_by_id(6)


# Assignment 2: SQL Statement Practice
# Copy SQL queries from material/Week2Part2_student_score.sql and execute in MySQL.
# Write a Python script to complete following questions:
# List out the score record of Chinese course for all students.
# List out the score record of English course for all students in descending order.
# List out all the student name.
# Get the average score of Chinese course.
# Get the minimum score of English course.
# Get the maximum score of Maths course.
# Get the number of student whose English score higher or equal to 60.
# List out the score records for male student whose surname are '周'

class SelectModel2(DbSetting):
   def studen_sql_lab(self):
        try:
            conn = pymysql.connect(**self.db_info)

            with conn.cursor(cursor=DictCursor) as cursor:

                #List out the score record of Chinese course for all students.                         
                command = "SELECT name, score FROM studentscore WHERE course='Chinese';"       
                cursor.execute(command)      
                result = cursor.fetchall()
                data = list(result) 
                print('List out the score record of Chinese course for all students.')
                for item in data:
                    name = item['name']
                    score = item['score']
                    print(f"{name}: {score}")   

                # List out the score record of English course for all students in descending order.
                command = "SELECT name, score FROM studentscore WHERE course='English' ORDER BY score DESC;"       
                cursor.execute(command)      
                result = cursor.fetchall()
                data = list(result) 
                print('List out the score record of English course for all students in descending order.')
                for item in data:
                    name = item['name']
                    score = item['score']
                    print(f"{name}: {score}")   
                
                # List out all the student name.
                command = "SELECT DISTINCT(name) FROM studentscore;"       
                cursor.execute(command)      
                result = cursor.fetchall()
                print('List out all the student name.')
                
                for item in data:
                    name = item["name"]
                    print(f'name: {name}') 

                # Get the average score of Chinese course.
                command = "SELECT AVG(score) AS avg_chinese FROM studentscore WHERE course = 'Chinese';"
                cursor.execute(command)      
                result = cursor.fetchall() #輸出chinese avg is: ((Decimal('62.8750'),),)，觀察後取[0][0]
                print('Get the average score of Chinese course.')
                for r in result:
                    print(f'chinese avg is: {r["avg_chinese"]}')

                # Get the minimum score of English course.
                command = "SELECT MIN(score) AS min_english FROM studentscore WHERE course = 'English';"
                cursor.execute(command)      
                result = cursor.fetchall() 
                print('Get the minimum score of English course.')
                for r in result:
                    print (f'minimum: {r["min_english"]}')

                # Get the maximum score of Maths course.
                command = "SELECT MAX(score) AS max_english FROM studentscore WHERE course = 'Maths';"
                cursor.execute(command)      
                result = cursor.fetchall() 
                print('Get the maximum score of Maths course.')
                for r in result:
                    print (f'maximum: {r["max_english"]}')
               
                # Get the number of student whose English score higher or equal to 60.
                command = "SELECT COUNT(1) AS count FROM studentscore WHERE course = 'English' AND score >= 60;"
                cursor.execute(command)      
                result = cursor.fetchall() 
                print('Get the number of student whose English score higher or equal to 60.')
                for r in result:
                    print (f'number: {r["count"]}')

                # List out the score records for male student whose surname are '周'
                command = "SELECT * FROM studentscore WHERE NAME LIKE '周%' AND sex = '男';"
                cursor.execute(command)      
                result = cursor.fetchall() 
                #data = list(result) 
                print("List out the score records for male student whose surname are '周'")
                for r in result:
                    print(f'{r["name"]} - {r["birth"]} - {r["sex"]} - {r["course"]} - {r["score"]}')  
          
                
                conn.commit()
                conn.close()  

        except Exception as ex:
            print(ex)


select2 = SelectModel2()
select2.studen_sql_lab()


# Assignment 3: JOIN Table SQL Statement Practice
# There are 2 Tables (Order, Customers):
# Orders
# orderID	customerID	amount
# 1	101	100
# 2	102	200
# 3	101	150
# 4	103	75
# Customers
# customerID	customer
# 101	Alice
# 102	Bob
# 103	Charlie
# Create these 2 tables in MySQL, and write a python script to display the name of each customer and their total order amount.

class JoinLab(DbSetting):
     def total_order_amount(self):
        
        conn = pymysql.connect(**self.db_info)

        with conn.cursor() as cursor:
            
            command = "SELECT c.customer, sum(o.amount) FROM Orders o \
                       LEFT JOIN Customers c ON o.customerID = c.customerID \
                       GROUP BY c.customer;"
            
            cursor.execute(command)  
            result = cursor.fetchall()                         
            conn.commit()
            conn.close()    

        data = list(result) 

        for item in data:
            name = item[0]
            amount = item[1]
            print(f"{name}: ${amount}")

join_lab = JoinLab()
join_lab.total_order_amount();


# Assignment 5: Pagination (Advance Optional)
# Using pagination, long list of results are shown on multiple pages. The subset of results is shown in a single page with links to next and previous results.
# To use pagination we will insert around 50 records. So copy SQL queries from material/Week2Part2_users.sql and execute in MySQL.
# Try to complete the following program.
# pagination(): return the user first name and last name, according to current page number (current_page) and numbers of record per page (no_of_record).
# no_of_record 是指每頁要幾筆
# current_page 第幾頁

def pagination(current_page, no_of_record):
    
    db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "a123456",
    "db": "pagination",
    "charset": "utf8"
    }   

    try:
        conn = pymysql.connect(**db_settings)
        
        with conn.cursor() as cursor:

            command = f'SELECT first_name, last_name FROM users LIMIT {(no_of_record)} OFFSET {(current_page - 1) * no_of_record};'
            cursor.execute(command) 
            result = cursor.fetchall() 
            new_list = [{'first_name': first, 'last_name': last} for first, last in result]

            conn.commit()
            conn.close() 

            if len(new_list) == 0:
                return (f'{new_list}, No records found')
            else:
                return(new_list)         

    except Exception as ex:
            print(ex)       


print(pagination(1, 10))
# [{'first_name': 'Tyler', 'last_name': 'Spradley'}, 
# {'first_name': 'David', 'last_name': 'Desmarais'}, 
# {'first_name': 'Miles', 'last_name': 'Harlow'}, 
# {'first_name': 'Becca', 'last_name': 'Kingman'}, 
# {'first_name': 'Rotana', 'last_name': 'Greger'}, 
# {'first_name': 'Cinzia', 'last_name': 'Derige'}, 
# {'first_name': 'Karen', 'last_name': 'Boyce'}, 
# {'first_name': 'Don', 'last_name': 'Ringer'}, 
# {'first_name': 'Dane', 'last_name': 'Schuette'}, 
# {'first_name': 'Melessa', 'last_name': 'Steinhauer'}]

print(pagination(6, 9))
# Remain Five Record in the last page
# [{'first_name': 'Muhammed', 'last_name': 'Knotts'}, 
# {'first_name': 'Allyson', 'last_name': 'Kjelstad'}, 
# {'first_name': 'Tara', 'last_name': 'Wigmanich'}, 
# {'first_name': 'Patrick', 'last_name': 'Baillargeon'}, 
# {'first_name': 'Louise', 'last_name': 'Sublewski'}]

print(pagination(6, 10))
# [], No records found