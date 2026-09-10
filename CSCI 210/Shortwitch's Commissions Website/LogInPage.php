<!DOCTYPE html>
<html>
    <body>
    <?php include 'Navbar.php';?>
        <head>
            <script>
                function validateForm() {
                  let x = document.forms["myForm"]["fname"].value;
                  if (x == "") {
                    alert("Name must be filled out");
                    return false;
                  }
                }
                </script>
            <link rel="stylesheet" href="StyleSheet/indexStyle.css">
            <?php include 'db_connect.php';?>
        </head>
        <title>Login</title>
        <h6>Login</h6>
            <!--login Form-->
         <form action="TargetLogPage.php" method="post">
         <label for="fname">Username:</label><br>
         <input type="text" id="username" name="username"><br>
         <label for="lname">Password:</label><br>
         <input type="text" id="password" name="password"><br><br>
         <input type="submit" value="Submit">
          </form>
          <button onclick="document.location='RegistrationPage.php'">New User?</button>
          <?php include 'footer.php';?>
          
    </body>
</html>