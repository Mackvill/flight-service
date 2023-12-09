-- MySQL dump 10.13  Distrib 8.0.35, for Win64 (x86_64)
--
-- Host: localhost    Database: flight_service
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Current Database: `flight_service`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `flight_service` /*!40100 DEFAULT CHARACTER SET utf8mb3 COLLATE utf8mb3_bin */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `flight_service`;

--
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS `booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking` (
  `booking_id` int NOT NULL AUTO_INCREMENT,
  `flight_id` int DEFAULT NULL,
  `passenger_id` int DEFAULT NULL,
  `booking_date` datetime DEFAULT NULL,
  `status` varchar(20) COLLATE utf8mb3_bin DEFAULT NULL,
  PRIMARY KEY (`booking_id`),
  UNIQUE KEY `unique_passenger_flight` (`passenger_id`,`flight_id`),
  KEY `flight_id` (`flight_id`),
  CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`flight_id`) REFERENCES `flights` (`flight_id`),
  CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`passenger_id`) REFERENCES `passengers` (`passenger_id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES `booking` WRITE;
/*!40000 ALTER TABLE `booking` DISABLE KEYS */;
INSERT INTO `booking` VALUES (2,2,3,'1578-04-04 00:00:00','Confirmed'),(3,2,5,'1789-04-04 00:00:00','Confirmed'),(4,2,7,'1578-04-04 00:00:00','Confirmed'),(5,2,9,'1578-04-04 00:00:00','Confirmed'),(6,2,11,'1578-04-04 00:00:00','Confirmed'),(7,2,12,'1789-04-04 00:00:00','Confirmed'),(8,2,13,'1234-02-02 00:00:00','Confirmed'),(9,2,14,'1234-02-02 00:00:00','Confirmed'),(13,2,15,'1789-04-04 00:00:00','Confirmed'),(14,2,16,'1789-04-04 00:00:00','Confirmed'),(15,1,17,'1578-04-04 00:00:00','Confirmed'),(16,2,18,'1578-04-04 00:00:00','Confirmed'),(18,2,19,'1578-04-04 00:00:00','Confirmed'),(19,2,20,'1578-04-04 00:00:00','Confirmed'),(21,2,22,'1789-04-04 00:00:00','Confirmed'),(22,2,24,'1789-04-04 00:00:00','Confirmed'),(23,2,25,'1789-04-04 00:00:00','Confirmed'),(26,2,26,'1578-04-04 00:00:00','Confirmed'),(27,2,28,'1578-04-04 00:00:00','Confirmed'),(28,2,5476,'1578-04-04 00:00:00','Confirmed'),(29,2,5478,'1578-04-04 00:00:00','Confirmed'),(30,2,5479,'1547-02-04 00:00:00','Confirmed'),(31,2,5480,'1547-02-04 00:00:00','Confirmed'),(32,2,5481,'1578-04-04 00:00:00','Confirmed'),(33,2,5482,'1578-04-04 00:00:00','Confirmed'),(34,3,5483,'1245-02-01 00:00:00','Confirmed'),(36,2,5485,'1578-04-04 00:00:00','Confirmed'),(37,2,5486,'1578-04-04 00:00:00','Confirmed'),(38,2,5487,'1578-04-04 00:00:00','Confirmed'),(39,2,5488,'1245-02-01 00:00:00','Confirmed'),(40,2,5490,'1789-04-04 00:00:00','Confirmed'),(41,2,5491,'1789-04-04 00:00:00','Confirmed'),(42,2,5492,'1245-02-01 00:00:00','Confirmed'),(43,2,5493,'1578-04-04 00:00:00','Confirmed'),(44,2,5494,'1578-04-04 00:00:00','Confirmed'),(45,2,5495,'1578-04-04 00:00:00','Confirmed'),(46,2,5496,'1578-04-04 00:00:00','Confirmed'),(47,2,5497,'1578-04-04 00:00:00','Confirmed'),(48,2,5498,'1578-04-04 00:00:00','Confirmed'),(49,2,5500,'1578-04-04 00:00:00','Confirmed'),(50,2,5502,'1578-04-04 00:00:00','Confirmed'),(51,2,5503,'1578-04-04 00:00:00','Confirmed'),(52,2,5504,'1578-04-04 00:00:00','Confirmed'),(53,2,5505,'1578-04-04 00:00:00','Confirmed'),(54,2,5506,'1578-04-04 00:00:00','Confirmed'),(55,2,5507,'1578-04-04 00:00:00','Confirmed'),(56,2,5508,'1578-04-04 00:00:00','Confirmed'),(57,2,5509,'1578-04-04 00:00:00','Confirmed'),(58,2,5510,'1578-04-04 00:00:00','Confirmed'),(59,2,5511,'1578-04-04 00:00:00','Confirmed'),(61,2,5513,'1578-04-04 00:00:00','Confirmed'),(62,2,5514,'1578-04-04 00:00:00','Confirmed'),(63,2,5515,'1578-04-04 00:00:00','Confirmed'),(64,2,5516,'1578-04-04 00:00:00','Confirmed'),(66,2,5520,'1245-02-01 00:00:00','Confirmed'),(67,1,5523,'1245-02-01 00:00:00','Confirmed'),(68,1,5525,'1234-02-02 00:00:00','Confirmed'),(70,2,5527,'1578-04-04 00:00:00','Confirmed'),(71,2,5528,'1578-04-04 00:00:00','Confirmed'),(72,2,5529,'1578-04-04 00:00:00','Confirmed'),(73,6,5530,'2023-12-01 00:00:00','Confirmed'),(74,2,5533,'1578-04-04 00:00:00','Confirmed'),(75,2,5538,'1578-04-04 00:00:00','Confirmed'),(76,2,5540,'1578-04-04 00:00:00','Confirmed'),(77,2,5541,'1578-04-04 00:00:00','Confirmed'),(78,1,5543,'1789-04-04 00:00:00','Confirmed'),(79,1,5544,'1789-04-04 00:00:00','Confirmed'),(80,1,5547,'1578-04-04 00:00:00','Confirmed'),(81,2,5549,'1475-02-02 00:00:00','Confirmed'),(82,1,5551,'1475-02-02 00:00:00','Confirmed'),(83,2,5556,'1475-02-02 00:00:00','Confirmed'),(84,1,5560,'1475-02-02 00:00:00','Confirmed');
/*!40000 ALTER TABLE `booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clients`
--

DROP TABLE IF EXISTS `clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clients` (
  `client_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) COLLATE utf8mb3_bin NOT NULL,
  `last_name` varchar(255) COLLATE utf8mb3_bin NOT NULL,
  `password` varchar(255) COLLATE utf8mb3_bin NOT NULL,
  `email` varchar(255) COLLATE utf8mb3_bin NOT NULL,
  PRIMARY KEY (`client_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clients`
--

LOCK TABLES `clients` WRITE;
/*!40000 ALTER TABLE `clients` DISABLE KEYS */;
INSERT INTO `clients` VALUES (1,'укп','укп','упуп','уп'),(2,'f','ewf','wf','wf'),(3,'куцп','цп','цпцп','цпцп'),(4,'c','c','c','c'),(6,'we','fwe','fe','fe'),(7,'','','','ца'),(16,'d','d','d','d'),(19,'pipo','egr','192837465qw','kirilharin@gmail.com'),(20,'pipo','egr','789456','pipoegr@anal');
/*!40000 ALTER TABLE `clients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `employee_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) COLLATE utf8mb3_bin NOT NULL,
  `last_name` varchar(255) COLLATE utf8mb3_bin NOT NULL,
  `password` varchar(255) COLLATE utf8mb3_bin NOT NULL,
  `email` varchar(255) COLLATE utf8mb3_bin NOT NULL,
  PRIMARY KEY (`employee_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'wef','wefw','efwf','wef'),(3,'wef','wefw','efwf','wefh'),(4,'sdf','wfw','wwf','ww'),(5,'9u9u0','99','9i9','i'),(6,'k','k','kk','k'),(7,'w','fw','fwf','wf'),(8,'pipo','egr','192837465Qw','kirilharin@gmail.com'),(10,'pipo','egr','789456','pipoegr@anal');
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flights`
--

DROP TABLE IF EXISTS `flights`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flights` (
  `flight_id` int NOT NULL,
  `airline` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
  `departure_airport` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
  `arrival_airport` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
  `departure_date` datetime DEFAULT NULL,
  `arrival_date` datetime DEFAULT NULL,
  `duration` int DEFAULT NULL,
  `available_seats` int DEFAULT NULL,
  `ticket_price` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`flight_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flights`
--

LOCK TABLES `flights` WRITE;
/*!40000 ALTER TABLE `flights` DISABLE KEYS */;
INSERT INTO `flights` VALUES (1,'1','1','1','1234-02-02 00:00:00','1982-04-02 00:00:00',985,15,1222.00),(2,'ewf','wef','wef','1475-02-02 00:00:00','1475-03-30 00:00:00',25,5,5467.00),(3,'bempa','dempa','rempa','1475-02-02 00:00:00','1987-02-02 00:00:00',234,154,6548.00),(6,'pipoairline','baldur','paladins','2023-12-01 00:00:00','2023-12-02 00:00:00',24,99,25478.00);
/*!40000 ALTER TABLE `flights` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `passengers`
--

DROP TABLE IF EXISTS `passengers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `passengers` (
  `passenger_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
  `last_name` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `gender` varchar(100) COLLATE utf8mb3_bin DEFAULT NULL,
  `contact_information` text COLLATE utf8mb3_bin,
  `passport_number` varchar(100) COLLATE utf8mb3_bin DEFAULT NULL,
  PRIMARY KEY (`passenger_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5561 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passengers`
--

LOCK TABLES `passengers` WRITE;
/*!40000 ALTER TABLE `passengers` DISABLE KEYS */;
INSERT INTO `passengers` VALUES (1,'1','1','1578-04-04','4','4',NULL),(2,'kevin','bobrikov','1789-04-04','chebupele','4484',NULL),(3,'c','c','1578-04-04','d','d',NULL),(4,'1578-04-04','1578-04-04','1578-04-04','1578-04-04','1578-04-04',NULL),(5,'c','c','1789-04-04','f','d',NULL),(6,'hl','lg','1245-02-01','wefw','42',NULL),(7,'c','c','1578-04-04','s','fs',NULL),(8,'rthh','rwh','1245-02-01','erg','erg',NULL),(9,'c','c','1578-04-04','sd','ds',NULL),(11,'c','c','1578-04-04','d','d',NULL),(12,'c','c','1789-04-04','d','d',NULL),(13,'c','c','1234-02-02','d','d',NULL),(14,'c','c','1234-02-02','d','d',NULL),(15,'c','c','1547-02-04','d','d',NULL),(16,'c','c','1789-04-04','d','d',NULL),(17,'c','c','1578-04-04','d','d',NULL),(18,'c','c','1578-04-04','d','d',NULL),(19,'c','c','1578-04-04','d','d',NULL),(20,'c','c','1578-04-04','c','c',NULL),(22,'c','c','1789-04-04','d','d',NULL),(24,'c','c','1789-04-04','s','s',NULL),(25,'c','c','1789-04-04','wefwwfgGHRB','wgeV',NULL),(26,'c','c','1578-04-04','ew','dw',NULL),(28,'c','c','1578-04-04','','',NULL),(51,'wew','wdsa','1245-02-01','efew','65165',NULL),(68,'sdgf','sgs','1987-05-05','tk','ykk',NULL),(69,'rth','erh','1987-02-07','sfe','+6618',NULL),(75,'sdgs','sef','1987-02-02','sfe','fs',NULL),(85,'erg','egr','1874-02-02','ewf','wf',NULL),(88,'gre','egr','1587-05-05','trh','tdh',NULL),(89,'rgr','egeg','1234-02-02','wtd','etw',NULL),(651,'wge','weg','1247-02-02','ewf','wef',NULL),(768,'пуек','пк','1987-02-07','пку','пк',NULL),(897,'sfsef','sefs','1475-02-02','sef','sef',NULL),(5472,'rsh','sdh','1578-04-04','eag','areg',NULL),(5473,'c','c','1578-04-04','','',NULL),(5474,'c','c','1578-04-04','','+36587243',NULL),(5475,'c','c','1578-04-04','','ds',NULL),(5476,'c','c','1578-04-04','','ytfhfbdgydnbdtdnd',NULL),(5477,'c','c','1578-04-04','','d',NULL),(5478,'c','c','1578-04-04','','','376764'),(5479,'c','c','1547-02-04','','','6587'),(5480,'c','c','1547-02-04','ds','ssds','4534'),(5481,'c','c','1578-04-04','','','652'),(5482,'c','c','1578-04-04','we','sfew','7638'),(5483,'c','c','1245-02-01','ew','dw','adwada'),(5484,'c','c','1578-04-04','we','dw','453'),(5485,'c','c','1578-04-04','gggg','gggg','1111'),(5486,'c','c','1578-04-04','1578-04-04 00:00:00','1578-04-04 00:00:00','948'),(5487,'c','c','1578-04-04','s','d','768'),(5488,'c','c','1245-02-01','dsv','sdfv','7678'),(5489,'c','c','1789-04-04','s','d','453'),(5490,'c','c','1789-04-04','sd','ds','35'),(5491,'c','c','1789-04-04','1789-04-04','1789-04-04','56'),(5492,'c','c','1245-02-01','d','d','e'),(5493,'c','c','1578-04-04','sd','sv','53'),(5494,'c','c','1578-04-04','sd','ds','34'),(5495,'c','c','1578-04-04','d','d','354'),(5496,'c','c','1578-04-04','7575','775757575','65'),(5497,'c','c','1578-04-04','s','d','465'),(5498,'c','c','1578-04-04','78','786','786'),(5499,'c','c','1578-04-04','78','786','786'),(5500,'c','c','1578-04-04','f','f','51'),(5501,'c','c','1578-04-04','d','d','51'),(5502,'c','c','1578-04-04','f','f','5353'),(5503,'c','c','1578-04-04','f','f','ds'),(5504,'c','c','1578-04-04','f','f','298'),(5505,'c','c','1578-04-04','ff','ff','645'),(5506,'c','c','1578-04-04','ff','fff','52'),(5507,'c','c','1578-04-04','d','dd','c'),(5508,'c','c','1578-04-04','f','f','f'),(5509,'c','c53','1578-04-04','d','d','336'),(5510,'c','c','1578-04-04','1578-04-04','1578-04-04','s'),(5511,'c','c','1578-04-04','1578-04-04','1578-04-04','78'),(5513,'c','c','1578-04-04','se','esf','esf'),(5514,'c','c','1578-04-04','awd','awd','awd'),(5515,'c','c','1578-04-04','d','d','123'),(5516,'c','c','1578-04-04','2','d','2'),(5520,'c','c','1245-02-01','d','d','4'),(5521,'c','c','1245-02-01','d','d','56'),(5523,'c','c','1245-02-01','sd','ef','36'),(5524,'c','c','1245-02-01','sd','ef','36'),(5525,'c','c','1234-02-02','dsf','sf','757'),(5527,'c','c','1578-04-04','sdrf','df','42'),(5528,'c','c','1578-04-04','df','df',''),(5529,'c','c','1578-04-04','df','df','463'),(5530,'pipo','egr','2023-12-01','egor','61','3252'),(5531,'c','c','1578-04-04','sdf','ds','52'),(5532,'c','c','1578-04-04','sdf','ds','52'),(5533,'c','c','1578-04-04','sd','ds','524'),(5534,'c','c','1578-04-04','s','df','53'),(5535,'c','c','1578-04-04','sd','fs','65'),(5536,'pipo','egr','1578-04-04','d','df','52'),(5537,'c','c','1578-04-04','s','d','53'),(5538,'c','c','1578-04-04','d','d','66'),(5539,'c','c','1578-04-04','d','d','66'),(5540,'c','c','1578-04-04','d','d','67'),(5541,'c','c','1578-04-04','d','d','68'),(5542,'c','c','1578-04-04','d','d','68'),(5543,'c','c','1789-04-04','sd','ds','ew'),(5544,'c','c','1789-04-04','sd','ds','yt'),(5545,'c','c','1789-04-04','sd','ds','yt'),(5546,'c','c','1789-04-04','sd','ds','78'),(5547,'c','c','1578-04-04','f','d','73'),(5548,'c','c','1475-02-02','sd','sd','453'),(5549,'c','c','1475-02-02','sd','ds','113'),(5550,'c','c','1475-02-02','sd','ds','113'),(5551,'c','c','1475-02-02','Чоловік','ds','135'),(5552,'c','c','1475-02-02','Чоловік','dsf','51'),(5553,'c','c','1475-02-02','Чоловік','dsf','52'),(5554,'c','c','1475-02-02','Чоловік','dsf','52'),(5555,'c','c','1475-02-02','Чоловік','dsf','52'),(5556,'c','c','1475-02-02','Чоловік','dsf','13'),(5557,'c','c','1475-02-02','Чоловік','dsf','13'),(5558,'c','c','1475-02-02','Чоловік','dsf','13'),(5559,'c','c','1475-02-02','Чоловік','dsf','13'),(5560,'c','c','1475-02-02','Чоловік','dsf','mk');
/*!40000 ALTER TABLE `passengers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tickets`
--

DROP TABLE IF EXISTS `tickets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tickets` (
  `ticket_id` int NOT NULL AUTO_INCREMENT,
  `flight_id` int DEFAULT NULL,
  `client_id` int DEFAULT NULL,
  `passenger_id` int DEFAULT NULL,
  `seat_number` varchar(255) COLLATE utf8mb3_bin DEFAULT NULL,
  `ticket_price` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`ticket_id`),
  UNIQUE KEY `unique_seat_per_flight` (`flight_id`,`seat_number`),
  KEY `client_id` (`client_id`),
  KEY `passenger_id` (`passenger_id`),
  CONSTRAINT `tickets_ibfk_1` FOREIGN KEY (`flight_id`) REFERENCES `flights` (`flight_id`),
  CONSTRAINT `tickets_ibfk_3` FOREIGN KEY (`client_id`) REFERENCES `clients` (`client_id`),
  CONSTRAINT `tickets_ibfk_4` FOREIGN KEY (`passenger_id`) REFERENCES `passengers` (`passenger_id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tickets`
--

LOCK TABLES `tickets` WRITE;
/*!40000 ALTER TABLE `tickets` DISABLE KEYS */;
INSERT INTO `tickets` VALUES (2,2,2,14,'a',8265.00),(5,1,4,17,'4',8265.00),(6,2,2,18,'9',8265.00),(7,2,4,20,'ad',5467.00),(10,2,1,25,'67',5467.00),(11,2,4,5482,'',5467.00),(12,3,4,5483,'02',6548.00),(13,2,4,5485,'4863',5467.00),(14,2,4,5486,'6521',5467.00),(15,2,4,5487,'768',5467.00),(16,2,4,5488,'78',5467.00),(18,2,4,5491,'56',5467.00),(19,2,4,5492,'se',5467.00),(20,2,4,5493,'573',5467.00),(21,2,4,5494,'4',5467.00),(22,2,4,5495,'453',5467.00),(23,2,4,5496,'65',5467.00),(24,2,4,5497,'5',5467.00),(25,2,4,5498,'786',5467.00),(26,2,4,5500,'51',5467.00),(27,2,4,5502,'253',5467.00),(28,2,4,5503,'sdv',5467.00),(30,2,4,5505,'54',5467.00),(31,2,4,5506,'52',5467.00),(32,2,4,5507,'c',5467.00),(33,2,4,5508,'f',5467.00),(34,2,4,5509,'6',5467.00),(35,2,4,5510,'d',5467.00),(36,2,4,5511,'87',5467.00),(38,2,4,5513,'ef',5467.00),(39,2,4,5514,'awd',5467.00),(43,2,4,5520,'2',5467.00),(44,1,4,5523,'51',1222.00),(45,2,NULL,NULL,'5500',NULL),(46,1,4,5525,'41',1222.00),(48,2,4,5527,'42',5467.00),(57,2,4,5528,'43',5467.00),(58,6,20,5530,'254',25478.00),(60,2,4,NULL,'53',5467.00),(64,1,4,5547,'7',1222.00),(65,2,4,5549,'113',5467.00),(66,1,4,5551,'213',1222.00),(68,1,4,5560,'ubhk',1222.00),(69,2,4,5527,'3',5467.00),(72,2,4,5528,'114',5467.00);
/*!40000 ALTER TABLE `tickets` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `before_insert_tickets` BEFORE INSERT ON `tickets` FOR EACH ROW BEGIN
    DECLARE total_seats INT;
    SELECT total_seats INTO total_seats
    FROM flights
    WHERE flight_id = NEW.flight_id;

    IF NEW.seat_number > total_seats THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid seat number. Exceeds total seats in the flight.';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-02 16:07:30
