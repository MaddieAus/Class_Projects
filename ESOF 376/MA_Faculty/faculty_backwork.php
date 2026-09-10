<!--Madison Austin, the backwork for searching-->

<?php
// Database connection
$host = "localhost";
$user = "root";
$password = "";
$dbname = "enrollment";

$conn = mysqli_connect($host, $user, $password, $dbname);

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// variables
$facID = "";
$facName = "";

// Checking if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $facID = trim($_POST["facID"]);
    $facName = trim($_POST["facName"]);

    // Server-side

    // If the Faculty ID provided
    if (!empty($facID)) {

        // Validating the numeric integer only
        if (!ctype_digit($facID)) {
            die("Invalid Faculty ID. Must be numeric.");
        }

        $query = "SELECT facID, facName, dept, address FROM faculty WHERE facID = ?";
        $stmt = mysqli_prepare($conn, $query);

        mysqli_stmt_bind_param($stmt, "i", $facID);
    }

    // If Faculty Name is provided
    elseif (!empty($facName)) {

        // Validate letters and spaces only (max 35)
        if (!preg_match("/^[A-Za-z ]{1,35}$/", $facName)) {
            die("Invalid Faculty Name. Letters and spaces only, max 35 characters.");
        }

        $query = "SELECT facID, facName, dept, address FROM faculty WHERE facName = ?";
        $stmt = mysqli_prepare($conn, $query);

        mysqli_stmt_bind_param($stmt, "s", $facName);
    }

    else {
        die("Please provide either Faculty ID or Faculty Name.");
    }

    // Execute a single prepared query
    mysqli_stmt_execute($stmt);

    $result = mysqli_stmt_get_result($stmt);

    if (mysqli_num_rows($result) > 0) {
        while ($row = mysqli_fetch_assoc($result)) {
            echo "<h3>Faculty Record Found:</h3>";
            echo "ID: " . htmlspecialchars($row["facID"]) . "<br>";
            echo "Name: " . htmlspecialchars($row["facName"]) . "<br>";
            echo "Department: " . htmlspecialchars($row["dept"]) . "<br>";
            echo "Address: " . htmlspecialchars($row["address"]) . "<br><br>";
        }
    } else {
        echo "No record found.";
    }

    mysqli_stmt_close($stmt);
}

mysqli_close($conn);
?>
