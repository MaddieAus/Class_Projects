<?php
//connecting to data base
$servername = "localhost";
$username = "root";
$password = "mysql";
$dbname = "ecommerce";

$conn = new mysqli($servername, $username, $password);

if ($conn->connect_error) {
    die("connection failed: " . $conn->connect_error);
}

?>