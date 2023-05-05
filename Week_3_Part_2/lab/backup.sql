-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: assignment
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Old` int NOT NULL,
  `Sex` varchar(1) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Tom1','address1',12,'1'),(2,'Tom1','address1',12,'F'),(3,'Tom2','address2',60,'F'),(4,'Tom3','address3',90,'M'),(5,'Tom1','address1',12,'F'),(6,'Tom2','address2',60,'F'),(7,'Tom3','address3',90,'M'),(8,'Tom1','address1',12,'F'),(9,'Tom2','address2',60,'F'),(10,'Tom3','address3',90,'M'),(11,'Tom1','address1',12,'F'),(12,'Tom2','address2',60,'F'),(13,'Tom3','address3',90,'M');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `customerID` int DEFAULT NULL,
  `customer` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (101,'Alice'),(102,'Bob'),(103,'Charlie');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderm`
--

DROP TABLE IF EXISTS `orderm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orderm` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `amount` varchar(100) NOT NULL,
  `order_date` varchar(100) NOT NULL,
  `Customer_ID` int NOT NULL,
  `Shop_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Customer_ID` (`Customer_ID`),
  KEY `Shop_ID` (`Shop_ID`),
  CONSTRAINT `orderm_ibfk_1` FOREIGN KEY (`Customer_ID`) REFERENCES `customer` (`ID`),
  CONSTRAINT `orderm_ibfk_2` FOREIGN KEY (`Shop_ID`) REFERENCES `shop` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderm`
--

LOCK TABLES `orderm` WRITE;
/*!40000 ALTER TABLE `orderm` DISABLE KEYS */;
INSERT INTO `orderm` VALUES (1,'1000','2023-05-01',1,2),(2,'1000','2023-05-01',1,2),(3,'1000','2023-05-01',1,1),(4,'1000','2023-05-01',2,1),(5,'1000','2023-05-01',4,3),(6,'1000','2023-05-01',2,3),(7,'1000','2023-05-01',3,3),(8,'1000','2023-05-01',2,1),(9,'1200','2023-05-01',2,1),(10,'2000','2023-05-01',2,3),(11,'3000','2023-05-01',3,3),(12,'4000','2023-05-01',2,1),(13,'1200','2023-05-01',2,1),(14,'2000','2023-05-01',2,3),(15,'3000','2023-05-01',3,3),(16,'4000','2023-05-01',2,1);
/*!40000 ALTER TABLE `orderm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `orderID` int DEFAULT NULL,
  `customerID` int DEFAULT NULL,
  `amount` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,101,100),(2,102,200),(3,101,150),(4,103,75);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop`
--

DROP TABLE IF EXISTS `shop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shop` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Phone` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop`
--

LOCK TABLES `shop` WRITE;
/*!40000 ALTER TABLE `shop` DISABLE KEYS */;
INSERT INTO `shop` VALUES (1,'Jack','address','0912345678'),(2,'Jack','address','0912345678'),(3,'Jack1','address1','0900000001'),(4,'Jack2','address2','0900000002'),(5,'Jack3','address3','0900000003'),(6,'jack_1','address_1','0900111222'),(7,'jack_2','address_2','0900333444'),(8,'jack_3','address_3','0900555666'),(9,'jack_1','address_1','0900111222'),(10,'jack_2','address_2','0900333444'),(11,'jack_3','address_3','0900555666'),(12,'jack_1','address_1','0900111222'),(13,'jack_2','address_2','0900333444'),(14,'jack_3','address_3','0900555666'),(15,'jack_1','address_1','0900111222'),(16,'jack_2','address_2','0900333444'),(17,'jack_3','address_3','0900555666'),(18,'jack_1','address_1','0900111222'),(19,'jack_2','address_2','0900333444'),(20,'jack_3','address_3','0900555666');
/*!40000 ALTER TABLE `shop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `studentscore`
--

DROP TABLE IF EXISTS `studentscore`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `studentscore` (
  `id` varchar(20) DEFAULT NULL,
  `name` varchar(20) NOT NULL DEFAULT '',
  `birth` varchar(20) NOT NULL DEFAULT '',
  `sex` varchar(10) NOT NULL DEFAULT '',
  `course` varchar(10) NOT NULL DEFAULT '',
  `score` int NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studentscore`
--

LOCK TABLES `studentscore` WRITE;
/*!40000 ALTER TABLE `studentscore` DISABLE KEYS */;
INSERT INTO `studentscore` VALUES ('01','周雷','1990-01-01','男','Chinese',80),('01','周雷','1990-01-01','男','English',90),('01','周雷','1990-01-01','男','Maths',60),('02','錢電','1990-12-21','男','Chinese',75),('02','錢電','1990-12-21','男','English',75),('02','錢電','1990-12-21','男','Maths',75),('03','孫風','1990-05-20','男','Chinese',50),('03','孫風','1990-05-20','男','English',40),('03','孫風','1990-05-20','男','Maths',60),('04','周雲','1990-08-06','男','Chinese',53),('04','周雲','1990-08-06','男','English',13),('04','周雲','1990-08-06','男','Maths',70),('05','周梅','1991-12-01','女','Chinese',100),('05','周梅','1991-12-01','女','English',90),('05','周梅','1991-12-01','女','Maths',95),('06','吳蘭','1992-03-01','女','Chinese',60),('06','吳蘭','1992-03-01','女','English',60),('06','吳蘭','1992-03-01','女','Maths',30),('07','鄭竹','1989-07-01','女','Chinese',70),('07','鄭竹','1989-07-01','女','English',85),('07','鄭竹','1989-07-01','女','Maths',20),('08','王菊','1990-01-20','女','Chinese',15),('08','王菊','1990-01-20','女','English',35),('08','王菊','1990-01-20','女','Maths',25);
/*!40000 ALTER TABLE `studentscore` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (2,'jack_01@twm.com','a123457'),(4,'jack_01@twm.com','a123457'),(5,'jack2','password'),(7,'jack2','password'),(8,'jack_01@twm.com','a123457'),(9,'jack_01','password'),(10,'jack_02','password'),(11,'jack_04','password'),(12,'jack_09','password'),(13,'jack_11','password'),(14,'jack_11','password'),(15,'jack_11','password'),(16,'jack_11','password'),(17,'jack_11','password'),(18,'jack_11','password'),(19,'jack_11','password'),(20,'jack_11','password'),(21,'jack_11','password'),(22,'jack_11','password'),(23,'jack_11','password'),(24,'jack_11','password'),(25,'jack_11','password'),(26,'jack_11','password'),(27,'jack_11','password'),(28,'jack_11','password');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-05 19:39:51
