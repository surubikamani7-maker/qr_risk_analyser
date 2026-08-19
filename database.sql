-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 19, 2026 at 03:10 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `qr_safety_checker`
--

-- --------------------------------------------------------

--
-- Table structure for table `blacklist`
--

CREATE TABLE `blacklist` (
  `id` int(11) NOT NULL,
  `domain` varchar(255) NOT NULL,
  `reason` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `blacklist`
--

INSERT INTO `blacklist` (`id`, `domain`, `reason`) VALUES
(1, 'malicious-site.com', 'Known malicious domain'),
(2, 'phishing-example.com', 'Known phishing domain');

-- --------------------------------------------------------

--
-- Table structure for table `scans`
--

CREATE TABLE `scans` (
  `id` int(11) NOT NULL,
  `url` text NOT NULL,
  `score` int(11) NOT NULL,
  `status` varchar(30) NOT NULL,
  `scan_date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `scans`
--

INSERT INTO `scans` (`id`, `url`, `score`, `status`, `scan_date`) VALUES
(1, 'https://google.com', 5, 'Safe', '2026-08-18 23:23:44'),
(2, 'http://unknown-site.com', 35, 'Suspicious', '2026-08-18 23:23:44'),
(3, 'http://malicious-site.com', 75, 'Dangerous', '2026-08-18 23:23:44'),
(4, 'https://example.com', 10, 'Safe', '2026-08-18 23:28:23'),
(5, 'https://example.com', 10, 'Safe', '2026-08-18 23:31:09'),
(6, 'https://example.com', 10, 'Safe', '2026-08-18 23:31:09');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`) VALUES
(1, 'Test User', 'test@gmail.com'),
(2, 'Test User', 'test@example.com');

-- --------------------------------------------------------

--
-- Table structure for table `whitelist`
--

CREATE TABLE `whitelist` (
  `id` int(11) NOT NULL,
  `domain` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `whitelist`
--

INSERT INTO `whitelist` (`id`, `domain`) VALUES
(1, 'google.com'),
(2, 'github.com'),
(3, 'example.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blacklist`
--
ALTER TABLE `blacklist`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `scans`
--
ALTER TABLE `scans`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `whitelist`
--
ALTER TABLE `whitelist`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `blacklist`
--
ALTER TABLE `blacklist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `scans`
--
ALTER TABLE `scans`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `whitelist`
--
ALTER TABLE `whitelist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
