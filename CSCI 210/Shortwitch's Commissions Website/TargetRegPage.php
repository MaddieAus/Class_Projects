<!DOCTYPE html>
<html  lang="en">
	
<head>

<?php include 'db_connect.php';?>
<link rel="stylesheet" href="StyleSheet/indexStyle.css">

</head>

<body>
<?php include 'Navbar.php';?>
	<?php
		$CustomerID = $_POST["CustomerID"];
		$FirstName = $_POST["FirstName"];
		$LastName = $_POST["LastName"];
		$Phone = $_POST["Phone"];
		$Address = $_POST["Address"];
		$City = $_POST["City"];
		$State = $_POST["State"];
		$Zip = $_POST["Zip"];
		$Email = $_POST["Email"];
		$Password = $_POST["Password"];
		$Username = $_POST["Username"];

	?>
	

	<?php 
	
	//echo $username . "<br>";
	//echo $password . "<br><br>"; 
	
	//$sql = "INSERT INTO ecommerce.users ('Username', 'Password') VALUES ( '" . $Username ."', '" . $Password ."');";
	$sql = "INSERT INTO ecommerce.users (`Username`, `Password`) VALUES ('$Username', '$Password');";
	//$sql2= "INSERT INTO customers ('CustomerID', 'FirstName', 'LastName', 'Address', 'City', 'State', 'Zip', 'Phone', 'Email') VALUES ('" . $CustomerID ."', '" . $FirstName ."', '" . $LastName . "', '" . $Address ."', '" . $City ."', '" . $State ."', '" . $Zip ."', '" . $Phone ."' ,  '" . $Email ."');";
	$sql2 = "INSERT INTO ecommerce.customers (`CustomerID`, `FirstName`, `LastName`, `Address`, `City`, `State`, `Zip`, `Phone`, `Email`) VALUES ('$CustomerID', '$FirstName', '$LastName', '$Address', '$City', '$State', '$Zip', '$Phone', '$Email');";

	//echo $sql . "<br>";
	$result = $conn->query($sql);
	$result2 = $conn->query($sql2);
	//var_dump($result);
	if ($result && $result2) {
		echo "You are registered!";
	} else {
		echo "Registration failed: " . $conn->error;
	}	

	?>
</body>

</html>