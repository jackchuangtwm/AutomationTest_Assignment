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
     def insert_shop(self, name, address, phone):
        try:
            conn = pymysql.connect(**self.db_info)
            with conn.cursor() as cursor:              
                command = "INSERT INTO Shop(name, address, phone) VALUES('" + name + "', '" + address + "', '" + phone + "');"
      
                i = cursor.execute(command)
                
                if i == 1:
                    print('insert success')
                else:
                    print('insert failed')         
             
                conn.commit()    
                conn.close()

        except Exception as ex:
            print(ex)

     def insert_customer(self, name, address, old, sex):
        try:
            conn = pymysql.connect(**self.db_info)
            with conn.cursor() as cursor:              
                command = "INSERT INTO Customer(name, Address, old, sex) VALUES('" + name + "', '" + address + "', " + str(old) + ", '" +  sex + "');"
                
                i = cursor.execute(command)
                
                if i == 1:
                    print('insert success')
                else:
                    print('insert failed')         
             
                conn.commit()    
                conn.close()

        except Exception as ex:
            print(ex)

     def insert_orderm(self, amount, order_date, customer_id,shop_id):
        try:
            conn = pymysql.connect(**self.db_info)
            with conn.cursor() as cursor:              
                command = "INSERT INTO OrderM(amount, order_date, customer_id,shop_id) VALUES('" + str(amount) + "', '" + order_date + "', " + str(customer_id) + ", '" +  str(shop_id) + "');"
              
                i = cursor.execute(command)
                
                if i == 1:
                    print('insert success')
                else:
                    print('insert failed')         
             
                conn.commit()    
                conn.close()

        except Exception as ex:
            print(ex)
    

class SelectModel(DbSetting):
   def select_all_orderm_info(self):
         try:
             conn = pymysql.connect(**self.db_info)

             with conn.cursor(cursor=DictCursor) as cursor:
                         
                 command = "SELECT c.id as customer_id, \
                                  c.name as customer_name, \
                                  c.address as customer_address, \
                                  s.name as shop_naem, \
                                  m.amount as orderm_amout, \
                                  m.order_date as orderm_date \
                           FROM OrderM m \
                           LEFT JOIN Shop s ON m.shop_id = s.id \
                           LEFT JOIN Customer c ON m.shop_id = c.id;"
                       
                 cursor.execute(command)      
                 result = cursor.fetchall()
                 data = list(result) 

                 for item in data:
                     customer_id = item['customer_id']
                     customer_name = item['customer_name']
                     customer_address = item['customer_address']
                     shop_naem = item['shop_naem']
                     orderm_amout = item['orderm_amout']
                     orderm_date = item['orderm_date']
             
                     print(f"{customer_id} - {customer_name} - {customer_address} - {shop_naem} - {orderm_amout} - {orderm_date}")  

         except Exception as ex:
             print(ex)


ins = InsertModel()
ins.insert_shop('jack_1', 'address_1', '0900111222')
ins.insert_shop('jack_2', 'address_2', '0900333444')
ins.insert_shop('jack_3', 'address_3', '0900555666')

ins.insert_customer('Tom1', 'address1', 12, 'F')
ins.insert_customer('Tom2', 'address2', 60, 'F')
ins.insert_customer('Tom3', 'address3', 90, 'M')

ins.insert_orderm(1200, '2023-05-01', 2,1)
ins.insert_orderm(2000, '2023-05-01', 2,3)
ins.insert_orderm(3000, '2023-05-01', 3,3)
ins.insert_orderm(4000, '2023-05-01', 2,1)

select = SelectModel()
select.select_all_orderm_info()



