-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 08, 2025 at 06:00 PM
-- Server version: 8.0.36
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ecommerce`
--

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `OrderID` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `CustID` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `ProductID` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `ShippingID` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `OrderDate` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `CustomerID` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `FirstName` varchar(35) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `LastName` varchar(35) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `City` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `State` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Zip` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Phone` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Email` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`CustomerID`, `FirstName`, `LastName`, `Address`, `City`, `State`, `Zip`, `Phone`, `Email`) VALUES
('MA3359', 'Madison', 'Austin', '107 south whitehall st', 'whitehall', 'MT', '59759', '4062661636', ''),
('2230', 'will', 'austin', '105 s whitehall st', 'whitehall', 'MT', '59759', '4062661635', ''),
('009', 'bob', 'marley', 'whitehall 8', 'whitehall', 'mt', '59759', '7789052', 'bobmar09@mail.com'),
('009', 'bob', 'marley', 'whitehall 8', 'whitehall', 'mt', '59759', '7789052', 'bobmar09@mail.com'),
('009', 'bob', 'marley', 'whitehall 8', 'whitehall', 'mt', '59759', '7789052', 'bobmar09@mail.com'),
('009', 'bob', 'marley', 'whitehall 8', 'whitehall', 'mt', '59759', '7789052', 'bobmar09@mail.com'),
('009', 'bob', 'marley', 'whitehall 8', 'whitehall', 'mt', '59759', '7789052', 'bobmar09@mail.com'),
('009', 'bob', 'marley', 'whitehall 8', 'whitehall', 'mt', '59759', '7789052', 'bobmar09@mail.com'),
('009', 'bob', 'marley', 'whitehall 8', 'whitehall', 'mt', '59759', '7789052', 'bobmar09@mail.com'),
('LA9910', 'Lexie', 'Austin', '105 s Whitehall ST', 'Whitehall', 'MT', '59759', '4062661345', 'LexieA09@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `OrderID` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `CustID` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `ProductID` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `ShippingID` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `OrderDate` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `CardNum` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `ExpDate` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `CVV` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`CardNum`, `ExpDate`, `CVV`) VALUES
('', '3/27', 345);

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `productID` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `price` decimal(10,0) NOT NULL,
  `imagepath` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`productID`, `title`, `description`, `price`, `imagepath`) VALUES
('005', 'Line Torso', 'This is line art of a Torso Commission. example shown in image', 14, '\\img\\line3.png'),
('006', 'Line Bust', 'this is a Line art of a Bust Commission. example shown in image', 12, '\\img\\line2.png'),
('007', 'Flats Full Body', 'this is a Flat color full body Commission. example shown in image', 20, '\\img\\flats1.png'),
('008', 'Torso Flat', 'This is a flat color of a torso. example shown in image', 18, '\\img\\flats3.png'),
('009', 'Flat Bust', 'this is a flat color of the bust. example shown in image', 17, '\\img\\flats2.png'),
('010', 'Shaded Full', 'this is an all-out Shaded Full body. example shown in image', 35, '\\img\\full1.png'),
('011', 'Shaded Torso', 'this is an all-out Shaded Torso. example shown in image', 30, '\\img\\full3.png'),
('012', 'Shaded Bust', 'this is an all-out shaded Bust commission. example shown in image', 25, '\\img\\full2.png'),
('001', 'Sketch Bust', 'This is a sketch of the bust up. example shown in image', 5, '\\img\\sketch2.png'),
('002', 'Sketch Torso', 'This is a sketch of the torso up. example shown in image', 6, '\\img\\sketch1.png'),
('003', 'Sketch Full Body', 'this is an Full Body commission. example shown in image', 10, '\\img\\sketch3.png'),
('004', 'Line Full Body', 'this is a full body Line art commission. example in the image', 15, '\\img\\line1.png');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `Username` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Password` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`Username`, `Password`) VALUES
('Maddie01', 'Buy01'),
('', ''),
('Heidi02', 'Buy02'),
('will03', 'pass02'),
('bob', 'mar'),
('LexieA', 'PassLA');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`OrderID`,`ProductID`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`OrderID`,`ProductID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
