-- MySQL dump 10.13  Distrib 5.5.53, for Win32 (AMD64)
--
-- Host: localhost    Database: websecurity
-- ------------------------------------------------------
-- Server version	5.5.53

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `studentaddress`
--

DROP TABLE IF EXISTS `studentaddress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `studentaddress` (
  `number_id` int(11) NOT NULL,
  `telephone_number` varchar(20) DEFAULT NULL,
  `Email_address` varchar(30) DEFAULT NULL,
  `student_number` int(11) NOT NULL,
  PRIMARY KEY (`number_id`,`student_number`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studentaddress`
--

LOCK TABLES `studentaddress` WRITE;
/*!40000 ALTER TABLE `studentaddress` DISABLE KEYS */;
INSERT INTO `studentaddress` VALUES (1,'010-62000001','zhaoming@263.net',200166001),(2,'010-63000001','qianxiao@elec.bnu.edu.cn',200166002),(3,'010-63000002','qianxiao@bnu.edu.cn',200166002),(4,'010-64000001','suncheng@bnu.edu.cn',200166003);
/*!40000 ALTER TABLE `studentaddress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `studentbase`
--

DROP TABLE IF EXISTS `studentbase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `studentbase` (
  `student_number` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `age` int(11) NOT NULL,
  `sex` varchar(2) DEFAULT NULL,
  `department` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`student_number`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studentbase`
--

LOCK TABLES `studentbase` WRITE;
/*!40000 ALTER TABLE `studentbase` DISABLE KEYS */;
INSERT INTO `studentbase` VALUES (200166001,'',20,'Ů',''),(200166002,'Ǯ',21,'',''),(200166003,'',19,'','');
/*!40000 ALTER TABLE `studentbase` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `studentclass`
--

DROP TABLE IF EXISTS `studentclass`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `studentclass` (
  `lesson_number` varchar(10) NOT NULL,
  `lesson_name` varchar(10) DEFAULT NULL,
  `lesson_grade` int(11) NOT NULL,
  `lesson_time` int(11) NOT NULL,
  `other_lesson_id` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`lesson_number`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studentclass`
--

LOCK TABLES `studentclass` WRITE;
/*!40000 ALTER TABLE `studentclass` DISABLE KEYS */;
INSERT INTO `studentclass` VALUES ('A01','',6,100,'B01'),('A02','',8,160,'B02'),('A03','Ӣ',10,200,'B03');
/*!40000 ALTER TABLE `studentclass` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teacher` (
  `id` int(4) NOT NULL AUTO_INCREMENT,
  `name` char(20) NOT NULL,
  `sex` char(20) NOT NULL,
  `addr` char(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES (5,'le','male','honghai'),(2,'ab','female','hangzhou'),(3,'jo','male','shyhai'),(4,'ma','female','peiking');
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-23 11:57:08
