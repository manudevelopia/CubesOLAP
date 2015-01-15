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
-- Table structure for table `sonarcube`
--

DROP TABLE IF EXISTS `sonarcube`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sonarcube` (
  `timestamp` varchar(20) NOT NULL DEFAULT '',
  `it_coverage` varchar(15) DEFAULT NULL,
  `lines` varchar(15) DEFAULT NULL,
  `ncloc` varchar(15) DEFAULT NULL,
  `classes` varchar(15) DEFAULT NULL,
  `files` varchar(15) DEFAULT NULL,
  `packages` varchar(15) DEFAULT NULL,
  `functions` varchar(15) DEFAULT NULL,
  `accessors` varchar(15) DEFAULT NULL,
  `statements` varchar(15) DEFAULT NULL,
  `public_api` varchar(15) DEFAULT NULL,
  `complexity` varchar(15) DEFAULT NULL,
  `class_complexity` varchar(15) DEFAULT NULL,
  `function_complexity` varchar(15) DEFAULT NULL,
  `file_complexity` varchar(15) DEFAULT NULL,
  `comment_lines` varchar(15) DEFAULT NULL,
  `comment_lines_density` varchar(15) DEFAULT NULL,
  `public_documented_api_density` varchar(15) DEFAULT NULL,
  `public_undocumented_api` varchar(15) DEFAULT NULL,
  `tests` varchar(15) DEFAULT NULL,
  `test_execution_time` varchar(15) DEFAULT NULL,
  `test_errors` varchar(15) DEFAULT NULL,
  `skipped_tests` varchar(15) DEFAULT NULL,
  `test_failures` varchar(15) DEFAULT NULL,
  `test_success_density` varchar(15) DEFAULT NULL,
  `coverage` varchar(15) DEFAULT NULL,
  `lines_to_cover` varchar(15) DEFAULT NULL,
  `uncovered_lines` varchar(15) DEFAULT NULL,
  `line_coverage` varchar(15) DEFAULT NULL,
  `conditions_to_cover` varchar(15) DEFAULT NULL,
  `uncovered_conditions` varchar(15) DEFAULT NULL,
  `branch_coverage` varchar(15) DEFAULT NULL,
  `duplicated_lines` varchar(15) DEFAULT NULL,
  `duplicated_blocks` varchar(15) DEFAULT NULL,
  `duplicated_files` varchar(15) DEFAULT NULL,
  `duplicated_lines_density` varchar(15) DEFAULT NULL,
  `duplications_data` varchar(15) DEFAULT NULL,
  `weighted_violations` varchar(15) DEFAULT NULL,
  `violations_density` varchar(15) DEFAULT NULL,
  `violations` varchar(15) DEFAULT NULL,
  `blocker_violations` varchar(15) DEFAULT NULL,
  `critical_violations` varchar(15) DEFAULT NULL,
  `major_violations` varchar(15) DEFAULT NULL,
  `minor_violations` varchar(15) DEFAULT NULL,
  `info_violations` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`timestamp`)
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
