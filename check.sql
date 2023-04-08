-- MySQL dump 10.13  Distrib 8.0.15, for macos10.14 (x86_64)
--
-- Host: localhost    Database: bdms
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `BloodBank`
--

DROP TABLE IF EXISTS `BloodBank`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `BloodBank` (
  `BB_Id` int(11) NOT NULL,
  `BB_Name` varchar(50) DEFAULT NULL,
  `BB_Add` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`BB_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BloodBank`
--

LOCK TABLES `BloodBank` WRITE;
/*!40000 ALTER TABLE `BloodBank` DISABLE KEYS */;
INSERT INTO `BloodBank` VALUES (67,'Duke Raleigh Hospital','Silverton'),(1111,'Castleview Hospital','Montrose'),(1234,'CHI Health St Francis','florida'),(4590,'Abbeville General Hospital','kansas'),(5329,'AHN Grove City','grove city');
/*!40000 ALTER TABLE `BloodBank` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bloodDelivery`
--

DROP TABLE IF EXISTS `bloodDelivery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `bloodDelivery` (
  `BB_Id` int(11) DEFAULT NULL,
  `PaID` int(11) NOT NULL,
  `BD_Date` date NOT NULL,
  PRIMARY KEY (`BD_Date`,`PaID`),
  KEY `BB_Id` (`BB_Id`),
  KEY `PaID` (`PaID`),
  CONSTRAINT `blooddelivery_ibfk_1` FOREIGN KEY (`BB_Id`) REFERENCES `bloodbank` (`BB_Id`),
  CONSTRAINT `blooddelivery_ibfk_2` FOREIGN KEY (`PaID`) REFERENCES `patient` (`PaId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bloodDelivery`
--

LOCK TABLES `bloodDelivery` WRITE;
/*!40000 ALTER TABLE `bloodDelivery` DISABLE KEYS */;
INSERT INTO `bloodDelivery` VALUES (67,4,'2017-01-08'),(67,6,'2020-06-27'),(1111,3,'2015-12-25'),(1234,2,'2018-02-10'),(1234,7,'2023-04-08'),(4590,1,'2019-03-02'),(4590,9,'2023-04-08'),(5329,3,'2021-07-16'),(5329,8,'2023-04-08');
/*!40000 ALTER TABLE `bloodDelivery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Doctor`
--

DROP TABLE IF EXISTS `Doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Doctor` (
  `DocId` int(11) NOT NULL AUTO_INCREMENT,
  `DocName` varchar(25) DEFAULT NULL,
  `DocAdd` varchar(25) DEFAULT NULL,
  `DocPhno` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`DocId`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Doctor`
--

LOCK TABLES `Doctor` WRITE;
/*!40000 ALTER TABLE `Doctor` DISABLE KEYS */;
INSERT INTO `Doctor` VALUES (1,'Sue','Texas',1238364578),(2,'Doug','London',4444235654),(3,'Tom','Ottawa',5409677645),(4,'Sam','Newark',9807605402),(5,'Ted','Paris',1234312342),(6,'Max','Spain',6548341894);
/*!40000 ALTER TABLE `Doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Donor`
--

DROP TABLE IF EXISTS `Donor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Donor` (
  `DonId` int(11) NOT NULL AUTO_INCREMENT,
  `DonName` varchar(25) DEFAULT NULL,
  `DonBloodType` varchar(5) NOT NULL,
  `DonGender` varchar(1) DEFAULT NULL,
  `DonAdd` varchar(25) DEFAULT NULL,
  `DonPhno` bigint(20) DEFAULT NULL,
  `DonAge` int(11) DEFAULT NULL,
  PRIMARY KEY (`DonId`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Donor`
--

LOCK TABLES `Donor` WRITE;
/*!40000 ALTER TABLE `Donor` DISABLE KEYS */;
INSERT INTO `Donor` VALUES (1,'Dwayne','A+','m','auburn',7498109999,30),(2,'Luis','A+','m','yuma',64788675616,40),(3,'Meg','B-','f','Irvine',1238567899,50),(4,'Sarah','AB+','f','Norwich',9345378730,55),(5,'John','O+','M','New York',7788993322,50);
/*!40000 ALTER TABLE `Donor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ExamineAndStore`
--

DROP TABLE IF EXISTS `ExamineAndStore`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `ExamineAndStore` (
  `DocId` int(11) DEFAULT NULL,
  `DonId` int(11) NOT NULL,
  `BB_Id` int(11) DEFAULT NULL,
  `eventDate` date NOT NULL,
  PRIMARY KEY (`DonId`,`eventDate`),
  KEY `DocId` (`DocId`),
  KEY `BB_Id` (`BB_Id`),
  CONSTRAINT `examineandstore_ibfk_1` FOREIGN KEY (`DocId`) REFERENCES `doctor` (`DocId`),
  CONSTRAINT `examineandstore_ibfk_2` FOREIGN KEY (`DonId`) REFERENCES `donor` (`DonId`),
  CONSTRAINT `examineandstore_ibfk_3` FOREIGN KEY (`BB_Id`) REFERENCES `bloodbank` (`BB_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ExamineAndStore`
--

LOCK TABLES `ExamineAndStore` WRITE;
/*!40000 ALTER TABLE `ExamineAndStore` DISABLE KEYS */;
INSERT INTO `ExamineAndStore` VALUES (1,1,1234,'2015-07-27'),(2,2,67,'2019-01-01'),(2,3,1111,'2019-01-01'),(5,3,4590,'2022-01-30'),(6,4,5329,'2018-12-04'),(5,5,1234,'2023-04-08');
/*!40000 ALTER TABLE `ExamineAndStore` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Patient`
--

DROP TABLE IF EXISTS `Patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Patient` (
  `PaId` int(11) NOT NULL AUTO_INCREMENT,
  `PaName` varchar(25) DEFAULT NULL,
  `PaPhno` bigint(20) DEFAULT NULL,
  `PaAdd` varchar(25) DEFAULT NULL,
  `PaBloodType` varchar(5) NOT NULL,
  PRIMARY KEY (`PaId`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Patient`
--

LOCK TABLES `Patient` WRITE;
/*!40000 ALTER TABLE `Patient` DISABLE KEYS */;
INSERT INTO `Patient` VALUES (1,'Daves',1356748958,'Truro','A+'),(2,'Ronald',4563773899,'Columbia','A+'),(3,'Homer',3454354354,'Ironwood','AB+'),(4,'Godfrey',1122112233,'Manistee','O-'),(5,'Adkins',7589487332,'Jackson','B+'),(6,'Ronald',9008889876,'Watertown','B+'),(7,'Marquies',9098098754,'Sacre-cour','AB+'),(8,'Mathew',2274335684,'Hells Kitchen','A+'),(9,'Antonio',8443787777,'Rome','A+');
/*!40000 ALTER TABLE `Patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storage`
--

DROP TABLE IF EXISTS `storage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `storage` (
  `Apos` int(11) DEFAULT NULL,
  `Aneg` int(11) DEFAULT NULL,
  `Bpos` int(11) DEFAULT NULL,
  `Bneg` int(11) DEFAULT NULL,
  `ABpos` int(11) DEFAULT NULL,
  `ABneg` int(11) DEFAULT NULL,
  `Opos` int(11) DEFAULT NULL,
  `Oneg` int(11) DEFAULT NULL,
  `BB_id` int(11) NOT NULL,
  PRIMARY KEY (`BB_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storage`
--

LOCK TABLES `storage` WRITE;
/*!40000 ALTER TABLE `storage` DISABLE KEYS */;
INSERT INTO `storage` VALUES (3,2,5,1,1,3,2,4,67),(2,1,5,4,3,1,5,2,1111),(2,4,3,2,0,4,5,3,1234),(1,3,1,5,1,2,4,5,4590),(0,1,5,2,3,1,5,3,5329);
/*!40000 ALTER TABLE `storage` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-08 18:46:36
