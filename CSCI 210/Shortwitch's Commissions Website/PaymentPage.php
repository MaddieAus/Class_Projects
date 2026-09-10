<!DOCTYPE html>
<html>
    <body>
    <?php include 'Navbar.php';?>
        <head>
            <link rel="stylesheet" href="StyleSheet/indexStyle.css">
            <?php include 'db_connect.php';?>
        </head>
       <title>Payment</title>
        <h6>Payment</h6>
        <button onclick="document.location='index.php'">Home</button>
       <!--Payment page-->
       <!-- this should ask for payment info if there isnt any-->
       <form action="Checkout.php" method="post">
         <label for="CardNum">Card Number:</label><br>
         <input type="text" id="CardNum" name="CardNum"><br>
         <label for="ExpDate">Experation Date:</label><br>
         <input type="text" id="ExpDate" name="ExpDate"><br>
         <label for="CVV">CVV:</label><br>
         <input type="text" id="CVV" name="CVV"><br><br>
         <input type="submit" value="Submit">
          </form>

       <?php include 'footer.php';?>
       

       <?php
	
		$CardNum = $_POST['CardNum'];
		$ExpDate = $_POST['ExpDate'];
        $CVV = $_POST['CVV'];
	?>

<?php 
	
	//echo $username . "<br>";
	//echo $password . "<br><br>"; 

	$sql = "INSERT INTO  ecommerce.payment (`CardNum`, `ExpDate`, `CVV`) VALUES ('$CardNum', '$ExpDate','$CVV');";
	//echo $sql;
	$result = $conn->query($sql);
	//echo 'result'.$result;
?>
    </body>
</html>