<?php
session_start();

if (!isset($_SESSION['user']))
header('location: login.php');
else
{
echo "you are logged in! ";
echo "<br /> <br /><a href=logout.php?session=logout>logout</a>";
}
?>

