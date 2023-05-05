CREATE TABLE Shop (
    ID int NOT NULL AUTO_INCREMENT,
    Name varchar(100) NOT NULL,
    Address varchar(100) NOT NULL,
    Phone varchar(50) NOT NULL,
    PRIMARY KEY (ID)
);

CREATE TABLE Customer (
    ID int NOT NULL AUTO_INCREMENT,
    Name varchar(100) NOT NULL,
    Address varchar(100) NOT NULL,
	Old int NOT NULL,
    Sex varchar(1) NOT NULL,
    PRIMARY KEY (ID)
);

CREATE TABLE OrderM (
    ID int NOT NULL AUTO_INCREMENT,
    amount varchar(100) NOT NULL,
    order_date varchar(100) NOT NULL,
    Customer_ID int NOT NULL,
    Shop_ID int NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (Customer_ID) REFERENCES Customer(ID),
    FOREIGN KEY (Shop_ID) REFERENCES Shop(ID)
);

      
INSERT INTO Shop(name, address, phone) VALUES('Jack1', 'address1', '0900000001');
INSERT INTO Shop(name, address, phone) VALUES('Jack2', 'address2', '0900000002');
INSERT INTO Shop(name, address, phone) VALUES('Jack3', 'address3', '0900000003');
SELECT * FROM shop;


INSERT INTO Customer(name, Address, old, sex) VALUES('Tom1', 'address1', 12, 'F');
INSERT INTO Customer(name, Address, old, sex) VALUES('Tom2', 'address2', 60, 'F');
INSERT INTO Customer(name, Address, old, sex) VALUES('Tom3', 'address3', 90, 'M');
SELECT * FROM Customer;

INSERT INTO OrderM(amount, order_date, customer_id,Shop_ID) VALUES(1000, '2023-05-01', 1,1);
INSERT INTO OrderM(amount, order_date, customer_idShop_ID) VALUES(1000, '2023-05-01', 2,2);
INSERT INTO OrderM(amount, order_date, customer_id,Shop_ID) VALUES(1000, '2023-05-01', 2,1);
INSERT INTO OrderM(amount, order_date, customer_id,Shop_ID) VALUES(1000, '2023-05-01', 2,3);
INSERT INTO OrderM(amount, order_date, customer_id,Shop_ID) VALUES(1000, '2023-05-01', 3,3);
INSERT INTO OrderM(amount, order_date, customer_id,Shop_ID) VALUES(1000, '2023-05-01', 2,1);
SELECT * FROM OrderM;

SELECT c.id, c.name, c.address, s.name, m.amount, m.order_date 
FROM OrderM m
LEFT JOIN Shop s ON m.shop_id = s.id
LEFT JOIN Customer c ON m.shop_id = c.id;
