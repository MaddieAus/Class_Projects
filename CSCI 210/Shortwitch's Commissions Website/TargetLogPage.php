<!DOCTYPE html>
<html  lang="en">
	
<head>

<?php include 'db_connect.php';?>
<link rel="stylesheet" href="StyleSheet/indexStyle.css">
</head>

<body>
<?php include 'Navbar.php';?>
	<?php
	
		$username = $_POST["username"];
		$password = $_POST["password"];
		
		
	?>
	
	
	<?php 
	
	//echo $username . "<br>";
	//echo $password . "<br><br>"; 
	
	$sql = "SELECT * FROM ecommerce.users WHERE username = '" . $username . "' AND password ='"  .$password . "'";
	//echo $sql;
	$result = $conn->query($sql);
	//echo 'result'.$result;
	if ($result->num_rows > 0) {
		echo "You are logged in!";
	} 
	else {
		echo "Incorrect username or password";
	}
	$conn->close();

	?>
</body>

</html>