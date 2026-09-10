<!DOCTYPE html>
<html>
    <body>
    <?php include 'Navbar.php';?>
        <head>
            <title>Your Cart</title>
            <link rel="stylesheet" href="StyleSheet/indexStyle.css">
        </head>
        <h6>Your Cart</h6>
        <button onclick="document.location='Checkout.php'">Looks Good, Checkout</button>

        <?php include 'footer.php';?>

    </body>
</html>

<?php

if (isset($_POST['ProductID'], $_POST['CustID'], $_POST['description'])) {
  $PRODUCTID = $_POST['ProductID'];
  $CUSTOMERID = $_POST['CustID'];
  $DESCRIPTION = $_POST['description'];
  
  
  $ORDERID = uniqid();


  $query = "INSERT INTO Orders (OrderID, ProductID, CustomerID, 'description') 
            VALUES ('$ORDERID', '$PRODUCTID', '$CUSTOMERID', '$DESCRIPTION')";
  mysqli_query($conn, $query);
} else {
  echo "Missing form data.";
}

?>

