-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1:3306
-- 產生時間： 
-- 伺服器版本： 10.4.10-MariaDB
-- PHP 版本： 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `etf`
--

-- --------------------------------------------------------

--
-- 資料表結構 `user_datatr`
--

DROP TABLE IF EXISTS `user_datatr`;
CREATE TABLE IF NOT EXISTS `user_datatr` (
  `name` varchar(10) DEFAULT NULL,
  `id` varchar(10) DEFAULT NULL,
  `start_time` date DEFAULT NULL,
  `last_time` date DEFAULT NULL,
  `target` varchar(500) DEFAULT NULL,
  `weight` varchar(500) DEFAULT NULL,
  `last_money` varchar(500) DEFAULT NULL,
  `expect_reward` varchar(20) DEFAULT NULL,
  `reward` varchar(20) DEFAULT NULL,
  `first_time` varchar(10) DEFAULT NULL,
  `in_per_year` varchar(10) DEFAULT NULL,
  `balence` varchar(10) DEFAULT NULL,
  `tolerance` varchar(10) DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  `sell_buy` varchar(500) DEFAULT NULL,
  `risk` varchar(30) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `retireAge` int(11) DEFAULT NULL,
  `expectAge` int(11) DEFAULT NULL,
  `expenses` float DEFAULT NULL,
  `want_calc` float DEFAULT NULL,
  `want_see` varchar(10) DEFAULT NULL,
  `nodiv_reward` varchar(20) DEFAULT NULL,
  `dividend` varchar(20) DEFAULT NULL,
  `last_ratio` varchar(500) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
