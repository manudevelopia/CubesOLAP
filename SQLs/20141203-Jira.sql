CREATE DATABASE  IF NOT EXISTS `uqasar$cubes` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `uqasar$cubes`;
-- MySQL dump 10.13  Distrib 5.5.40, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: uqasar$cubes
-- ------------------------------------------------------
-- Server version	5.1.73-log

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
-- Table structure for table `jira`
--

DROP TABLE IF EXISTS `jira`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jira` (
  `Issuekey` varchar(7) NOT NULL DEFAULT '',
  `Project` varchar(6) DEFAULT NULL,
  `Summary` varchar(113) DEFAULT NULL,
  `Type` varchar(11) DEFAULT NULL,
  `Status` varchar(11) DEFAULT NULL,
  `Priority` varchar(7) DEFAULT NULL,
  `Resolution` varchar(10) DEFAULT NULL,
  `Assignee` varchar(8) DEFAULT NULL,
  `Reporter` varchar(8) DEFAULT NULL,
  `Creator` varchar(8) DEFAULT NULL,
  `Created` varchar(18) DEFAULT NULL,
  `Last_Viewed` varchar(18) DEFAULT NULL,
  `Updated` varchar(18) DEFAULT NULL,
  `Resolved` varchar(18) DEFAULT NULL,
  `Affects_Versions` varchar(15) DEFAULT NULL,
  `Fix_Versions` varchar(1) DEFAULT NULL,
  `Components` varchar(32) DEFAULT NULL,
  `Due_Date` varchar(9) DEFAULT NULL,
  `Votes` int(3) DEFAULT NULL,
  `Watchers` int(3) DEFAULT NULL,
  `Images` varchar(1) DEFAULT NULL,
  `Original_Estimate` int(5) DEFAULT NULL,
  `Remaining_Estimate` int(5) DEFAULT NULL,
  `Time_Spent` int(5) DEFAULT NULL,
  `Work_Ratio` varchar(3) DEFAULT NULL,
  `SubTasks` varchar(1) DEFAULT NULL,
  `Linked_Issues` varchar(5) DEFAULT NULL,
  `Environment` varchar(1) DEFAULT NULL,
  `Description` varchar(245) DEFAULT NULL,
  `Security_Level` varchar(1) DEFAULT NULL,
  `Progress` varchar(3) DEFAULT NULL,
  `SUM_Progress` varchar(3) DEFAULT NULL,
  `SUM_Time_Spent` int(5) DEFAULT NULL,
  `SUM_Remaining_Estimate` int(5) DEFAULT NULL,
  `SUM_Original_Estimate` int(5) DEFAULT NULL,
  `Labels` varchar(34) DEFAULT NULL,
  `Business_Value` int(3) DEFAULT NULL,
  `Epic_Colour` varchar(1) DEFAULT NULL,
  `Epic_Link` varchar(1) DEFAULT NULL,
  `Epic_Name` varchar(1) DEFAULT NULL,
  `Epic_Status` varchar(1) DEFAULT NULL,
  `EpicTheme` varchar(1) DEFAULT NULL,
  `Flagged` varchar(1) DEFAULT NULL,
  `Raised_During` varchar(1) DEFAULT NULL,
  `Rank` varchar(9) DEFAULT NULL,
  `Sprint` varchar(18) DEFAULT NULL,
  `Story` varchar(6) DEFAULT NULL,
  `Story_Points` int(3) DEFAULT NULL,
  `Team` varchar(25) DEFAULT NULL,
  `Test_Sessions` varchar(25) DEFAULT NULL,
  `Testing_Status` varchar(11) DEFAULT NULL,
  `CHART_Date_of_First_Response` int(3) DEFAULT NULL,
  PRIMARY KEY (`Issuekey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-12-03 12:02:18
