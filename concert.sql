-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 03, 2024 at 11:57 PM
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
-- Database: `concert`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `buyer_name` text NOT NULL,
  `buyer_gender` text NOT NULL,
  `buyer_phone` varchar(20) NOT NULL,
  `buyer_email` varchar(20) NOT NULL,
  `buyer_password` varchar(10) NOT NULL,
  `buyer_payment_method` varchar(20) NOT NULL,
  `num_tickets` int(10) NOT NULL,
  `total_price` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`buyer_name`, `buyer_gender`, `buyer_phone`, `buyer_email`, `buyer_password`, `buyer_payment_method`, `num_tickets`, `total_price`) VALUES
('Khairun Amin', 'Male', '0139956487', 'khairunn@gmail.com', 'khyucky76', 'Credit/Debit Card', 2, 100),
('Lia Jameela', '', '', 'liajameela@gmail.com', 'lliaa0909', 'Online Banking', 3, 150),
('Hana Marissa', 'Female', '', 'hanaa78@gmail.com', 'hanaa45685', 'E-Wallet', 1, 50),
('Ilyas Faris', 'Male', '0134298465', 'ilyasss9898@gmail.co', 'ygbhjkou45', 'Online Banking', 5, 250),
('Aisy Adha', 'Female', '0194885274', 'asyyy02@gmail.com', 'edcvbnjki4', 'Credit/Debit Card', 2, 100);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
