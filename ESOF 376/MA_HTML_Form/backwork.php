<!--Madsion Austin, HTML regastration form-->
<?php

function sanitize($data) {
    return htmlspecialchars(trim($data));
}

$errors = [];

// Sanitize inputs
$firstname = sanitize($_POST['firstname']);
$lastname = sanitize($_POST['lastname']);
$password = $_POST['passwd'];
$confirm = $_POST['confirm_passwd'];
$email = sanitize($_POST['email']);
$url = sanitize($_POST['url']);
$age = sanitize($_POST['age']);
$zipcode = sanitize($_POST['zipcode']);
$intro = sanitize($_POST['introduction']);

// First name: alphabetical, max 25 chars
if (!preg_match("/^[A-Za-z]{1,25}$/", $firstname)) {
    $errors[] = "Invalid first name.";
}
// Last name 
if (!preg_match("/^[A-Za-z]{1,25}$/", $lastname)) {
    $errors[] = "Invalid last name.";
}

// Password at least 8 characters
if (strlen($password) < 8) {
    $errors[] = "Password must be at least 8 characters.";
}

// Confirm password
if ($password !== $confirm) {
    $errors[] = "Passwords do not match.";
}

// Email validation
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    $errors[] = "Invalid email address.";
}

// URL 
if (!empty($url) && !filter_var($url, FILTER_VALIDATE_URL)) {
    $errors[] = "Invalid URL.";
}

// Age between 25 and 50
if (!filter_var($age, FILTER_VALIDATE_INT) || $age < 25 || $age > 50) {
    $errors[] = "Age must be between 25 and 50.";
}

// Zip code exactly 5 digits
if (!preg_match("/^[0-9]{5}$/", $zipcode)) {
    $errors[] = "Zip code must be 5 digits.";
}

// Introduction max 500 characters
if (strlen($intro) > 500) {
    $errors[] = "Introduction must be under 500 characters.";
}

// results
if (empty($errors)) {
    echo "<h2>Registration Successful!</h2>";
} else {
    echo "<h2>Errors:</h2>";
    echo "<ul>";
    foreach ($errors as $error) {
        echo "<li>$error</li>";
    }
    echo "</ul>";
}
?>
