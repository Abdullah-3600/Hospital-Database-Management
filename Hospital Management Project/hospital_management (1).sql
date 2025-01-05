-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 05, 2025 at 04:21 PM
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
-- Database: `hospital_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_receptionist_table`
--

CREATE TABLE `admin_receptionist_table` (
  `ID` varchar(4) NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `register_as` varchar(12) DEFAULT NULL,
  `password` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin_receptionist_table`
--

INSERT INTO `admin_receptionist_table` (`ID`, `name`, `phone`, `age`, `register_as`, `password`) VALUES
('1438', 'qwert', '12346578911', 23, 'ADMIN', "123"),
('1885', 'adsf', '12345678900', 33, 'RECEPTIONIST', '111'),
('357', 'asdf', '12345678910', 22, 'RECEPTIONIST', '222'),
('426', 'qqq', '11111111111', 22, 'RECEPTIONIST', '12edf'),
('4310', 'addf', '11111111111', 23, 'RECEPTIONIST', '1234'),
('552', 'adf', '11111111111', 22, 'ADMIN', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `doctor_patient_treatment`
--

CREATE TABLE `doctor_patient_treatment` (
  `Patient_ID` varchar(4) DEFAULT NULL,
  `Patient_Name` varchar(20) DEFAULT NULL,
  `Doctor_Name` varchar(20) DEFAULT NULL,
  `Date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `doctor_patient_treatment`
--

INSERT INTO `doctor_patient_treatment` (`Patient_ID`, `Patient_Name`, `Doctor_Name`, `Date`) VALUES
('3', 'rafik', '{Md. Abdul }', '2025-01-04'),
('4', 'rei', '{Md. Abdul }', '2025-01-05'),
('5', 'ter', '{Md. Abdul }', '2025-01-05'),
('6', 'arif', '{Md. Abdul }', '2025-01-05'),
('7', 'tri', 'Md. Abdul ', '2025-01-05'),
('8', 'sfse', 'Md. Abdul ', '2025-01-05'),
('9', 'sdfs', 'Md. Abdul ', '2025-01-05'),
('10', 'me', 'Md. Abdul ', '2025-01-05'),;

-- --------------------------------------------------------

--
-- Table structure for table `doctor_registration_table`
--

CREATE TABLE `doctor_registration_table` (
  `ID` varchar(4) NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `specialized_in` varchar(15) DEFAULT NULL,
  `chamber_no` varchar(4) DEFAULT NULL,
  `password` char(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `doctor_registration_table`
--

INSERT INTO `doctor_registration_table` (`ID`, `name`, `phone`, `age`, `specialized_in`, `chamber_no`, `password`) VALUES
('4718', 'Md. Abdul ', '0192873494', 45, 'GENERAL MEDICIN', 'NULL', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `nurse_registration_table`
--

CREATE TABLE `nurse_registration_table` (
  `ID` varchar(4) NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `nurse_type` varchar(14) DEFAULT NULL,
  `doctor_id` varchar(4) DEFAULT NULL,
  `supervisor_id` varchar(4) DEFAULT NULL,
  `assigned_room` varchar(4) DEFAULT NULL,
  `password` char(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `nurse_registration_table`
--

INSERT INTO `nurse_registration_table` (`ID`, `name`, `phone`, `age`, `nurse_type`, `doctor_id`, `supervisor_id`, `assigned_room`, `password`) VALUES
('5380', 'qwer', '12345678900', 33, 'GENERAL WARD', 'NULL', 'NULL', 'NULL', NULL),
('6917', 'qwe', '11111111111', 33, 'GENERAL WARD', '2280', '5380', '1234', '111'),
('9102', 'nurse', '11111111111', 23, 'GENERAL WARD', '2350', '6917', 'R900', '1212');

-- --------------------------------------------------------

--
-- Table structure for table `patient_registration_table`
--

CREATE TABLE `patient_registration_table` (
  `ID` int(11) DEFAULT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `Age` char(2) DEFAULT NULL,
  `Phone` varchar(11) DEFAULT NULL,
  `Issues` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patient_registration_table`
--

INSERT INTO `patient_registration_table` (`ID`, `Name`, `Age`, `Phone`, `Issues`) VALUES
(1, 'asd', '12', '1111', 'fever'),
(2, 'rewq', '12', '1111111111', 'fever and cold'),
(3, 'rafik', '23', '9328747', 'autistic'),
(4, 'rei', '0', '352452', 'no issiue'),
(5, 'ter', '21', '2441', 'g'),
(6, 'arif', '0', '0195322251', 'N/A'),
(7, 'tri', '0', '2423', 'fg'),
(8, 'sfse', '0', '21412', 'dsf'),
(9, 'sdfs', '12', '1442', 'asf'),
(10, 'me', '20', '1241', 'dfsf');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_receptionist_table`
--
ALTER TABLE `admin_receptionist_table`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `doctor_registration_table`
--
ALTER TABLE `doctor_registration_table`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `nurse_registration_table`
--
ALTER TABLE `nurse_registration_table`
  ADD PRIMARY KEY (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
