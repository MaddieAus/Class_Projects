<!--search bar -->

<!DOCTYPE html>

<div id="search">
    <form action = 'CommissionsInfo.php' method='get'>
        <input type='text' name='search' placeholder='search'></input>
        <input type='submit' value='search'></input>
    </form>  
</div>

<?php
   $search = $_GET['search'] ?? '';
   $conn = new mysqli("localhost", "root", "mysql", "ecommerce"); 
   if ($conn->connect_error) {
       die("Connection failed: " . $conn->connect_error);
   }
   
 if (!empty($search)) {
    $stmt = $conn->prepare("SELECT productID, imagepath, title, 'description' FROM products WHERE title = ?");
    $stmt->bind_param("s", $search);
    $stmt->execute();
    $result = $stmt->get_result();
} else {
    $result = $conn->query("SELECT productID, imagepath, title, 'description' FROM products");
}
    ?>