-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: orsen_kb
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `profiler`
--

DROP TABLE IF EXISTS `profiler`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profiler` (
  `idprofiler` int NOT NULL,
  `block` int NOT NULL,
  `label` varchar(45) NOT NULL,
  `label_count` int NOT NULL,
  `question` varchar(200) NOT NULL,
  `anchor` int NOT NULL,
  PRIMARY KEY (`idprofiler`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profiler`
--

LOCK TABLES `profiler` WRITE;
/*!40000 ALTER TABLE `profiler` DISABLE KEYS */;
INSERT INTO `profiler` VALUES (1,1,'A',1,'How much of the time do you feel you are making progress towards accomplishing your goals?',1),(2,1,'E',1,'How often do you become absorbed in what you are doing? ',1),(3,1,'P',1,'In general, how often do you feel joyful?',1),(4,1,'N',1,'In general, how often do you feel anxious?',1),(5,1,'A',2,'How often do you achieve the important goals you have set for yourself?',1),(6,2,'H',1,'In general, how would you say your health is?',2),(7,3,'M',1,'In general, to what extent do you lead a purposeful and meaningful life?',3),(8,3,'R',1,'To what extent do you receive help and support from others when you need it?',3),(9,3,'M',2,'In general, to what extent do you feel that what you do in your life is valuable and worthwhile?',3),(10,3,'E',2,'In general, to what extent do you feel excited and interested in things?',3),(11,3,'L',0,'How lonely do you feel in your daily life?',3),(12,4,'H',2,'How satisfied are you with your current physical health?',3),(13,5,'P',2,'In general, how often do you feel positive?',1),(14,5,'N',2,'In general, how often do you feel angry?',1),(15,5,'A',3,'How often are you able to handle your responsibilities?',1),(16,5,'N',3,'In general, how often do you feel sad?',1),(17,5,'E',3,'How often do you lose track of time while doing something you enjoy?',1),(18,6,'H',3,'Compared to others of your same age and sex, how is your health?',2),(19,7,'R',2,'To what extent do you feel loved?',3),(20,7,'M',3,'To what extent do you generally feel you have a sense of direction in your life?',3),(21,7,'R',3,'How satisfied are you with your personal relationships?',3),(22,7,'P',3,'In general, to what extent do you feel contented?',3),(23,8,'H',0,'Taking all things together, how happy would you say you are?',3);
/*!40000 ALTER TABLE `profiler` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-11 22:40:07
