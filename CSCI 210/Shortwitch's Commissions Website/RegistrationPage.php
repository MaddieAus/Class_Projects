<!DOCTYPE html>
<html>
    <body>
    <?php include 'Navbar.php';?>
        <head>
            <link rel="stylesheet" href="StyleSheet/indexStyle.css">
            <?php include 'db_connect.php';?>
        </head>
        <title>Regestration</title> 
        <h6>Regestration</h6>
            <!--regestration Form-->
            <form action="TargetRegPage.php" method="post">
                <label for="CustomerID">CustomerID:</label><br>
                <input type="text" id="CustomerID" name="CustomerID" placeholder="name"><br>

                <label for="FirstName">First name:</label><br>
                <input type="text" id="FirstName" name="FirstName" placeholder="name"><br>

                <label for="LastName">Last name:</label><br>
                <input type="text" id="LastName" name="LastName" placeholder="name"><br>

                <label for="Email">Email:</label><br>
                <input type="text" id="Email" name="Email" placeholder="name"><br>

                <label for="Phone">Phone Number:</label><br>
                <input type="text" id="Phone" name="Phone" placeholder="name"><br>

                <label for="Address">address:</label><br>
                <input type="text" id="Address" name="Address" placeholder="name"><br>

                <label for="State">State:</label><br>
                <input type="text" id="State" name="State" placeholder="name"><br>

                <label for="City">City:</label><br>
                <input type="text" id="City" name="City" placeholder="name"><br>

                <label for="Zip">Zip:</label><br>
                <input type="text" id="Zip" name="Zip" placeholder="name"><br>

                <label for="Username">Username:</label><br>
                <input type="text" id="Username" name="Username" placeholder="name"><br>

                <label for="Password">Password:</label><br>
                <input type="text" id="Password" name="Password" placeholder="name"><br><br>
                
                <input type="submit" value="Submit">

         </form> 
         <button onclick="document.location='LogInPage.php'">Login</button>
         <?php include 'footer.php';?>
    </body>
</html>