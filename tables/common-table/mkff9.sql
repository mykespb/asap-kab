-- MySQL dump 10.13  Distrib 5.7.31, for Linux (x86_64)
--
-- Host: localhost    Database: mkff
-- ------------------------------------------------------
-- Server version	5.7.31-0ubuntu0.18.04.1

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
-- Table structure for table `arch`
--

DROP TABLE IF EXISTS `arch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `arch` (
  `number` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `fname` varchar(1024) NOT NULL DEFAULT '',
  `fext` varchar(45) NOT NULL DEFAULT '',
  `filename` varchar(1024) NOT NULL DEFAULT '',
  `fpath` varchar(1024) NOT NULL DEFAULT '',
  `ftype` varchar(45) NOT NULL DEFAULT '',
  `fullpath` varchar(1024) NOT NULL DEFAULT '',
  PRIMARY KEY (`number`),
  UNIQUE KEY `number_UNIQUE` (`number`),
  KEY `index2` (`fname`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=cp1251;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `main`
--

DROP TABLE IF EXISTS `main`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main` (
  `number` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `record_code` int(10) DEFAULT '0',
  `archive_owner` varchar(255) DEFAULT '',
  `digitize` varchar(255) DEFAULT '',
  `device_no` varchar(255) DEFAULT '',
  `file_name` varchar(255) DEFAULT '',
  `no_on_device` varchar(255) DEFAULT '',
  `timer` varchar(255) DEFAULT '',
  `quality` varchar(255) DEFAULT '',
  `song_line1` varchar(255) DEFAULT '',
  `rem_date_work` varchar(255) DEFAULT '',
  `song_name` varchar(255) DEFAULT '',
  `singer` varchar(255) DEFAULT '',
  `rem_singer` varchar(255) DEFAULT '',
  `song_author` varchar(255) DEFAULT '',
  `music_author` varchar(255) DEFAULT '',
  `rem_music` varchar(255) DEFAULT '',
  `verses_author` varchar(255) DEFAULT '',
  `record_type` varchar(255) DEFAULT '',
  `record_owner` varchar(255) DEFAULT '',
  `archive_code` varchar(45) DEFAULT NULL,
  `name_coded` varchar(256) DEFAULT NULL,
  `line1_coded` varchar(255) DEFAULT NULL,
  `music_coded` varchar(255) DEFAULT NULL,
  `author_coded` varchar(255) DEFAULT NULL,
  `verses_coded` varchar(255) DEFAULT NULL,
  `uuid_record` varchar(255) DEFAULT NULL,
  `uuid_original` varchar(255) DEFAULT NULL,
  `etc_auto` varchar(255) DEFAULT NULL,
  `rem_dt` varchar(255) DEFAULT '',
  `quality_coded` varchar(45) DEFAULT NULL,
  `dt_exec` varchar(45) DEFAULT '',
  PRIMARY KEY (`number`),
  KEY `index3` (`file_name`),
  KEY `index4` (`name_coded`),
  KEY `index5` (`line1_coded`),
  KEY `index6` (`music_coded`),
  KEY `index7` (`author_coded`),
  KEY `index8` (`verses_coded`),
  KEY `index9` (`uuid_record`),
  KEY `index10` (`uuid_original`),
  KEY `index11` (`dt_exec`)
) ENGINE=InnoDB AUTO_INCREMENT=119205 DEFAULT CHARSET=cp1251;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-02  1:56:46
