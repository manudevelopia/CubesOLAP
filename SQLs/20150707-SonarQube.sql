USE uqasar$cubes;
DROP TABLE IF EXISTS `sonarqube`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sonarqube` (
  `timestamp` varchar(30) NOT NULL DEFAULT '',
  `key` varchar(125) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `datestamp` varchar(30) DEFAULT NULL,
  `lang` varchar(50) DEFAULT NULL,
  `version` varchar(50) DEFAULT NULL,
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
  `weighted_violations` varchar(15) DEFAULT NULL,
  `violations_density` varchar(15) DEFAULT NULL,
  `violations` varchar(15) DEFAULT NULL,
  `blocker_violations` varchar(15) DEFAULT NULL,
  `critical_violations` varchar(15) DEFAULT NULL,
  `major_violations` varchar(15) DEFAULT NULL,
  `minor_violations` varchar(15) DEFAULT NULL,
  `info_violations` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
