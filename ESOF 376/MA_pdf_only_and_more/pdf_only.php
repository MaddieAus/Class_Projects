<!--Madison Austin
// Write a PHP script to upload PDF files only-->


<!-- the assignment says just php but here is what the html would look like

<!DOCTYPE html>
<html>
<head>
    <title>Upload PDF</title>
</head>
<body>

<h2>Upload PDF File (Max 5MB)</h2>

<form action="upload.php" method="post" enctype="multipart/form-data">
    Select PDF:
    <input type="file" name="pdfFile" accept=".pdf" required>
    <br><br>
    <input type="submit" name="submit" value="Upload">
</form>

</body>
</html>

-->


<?php

$targetDir = "uploads/";
$maxSize = 5 * 1024 * 1024; // 5 MB

if(isset($_POST["submit"])){

    $fileName = $_FILES["pdfFile"]["name"];
    $fileTmp  = $_FILES["pdfFile"]["tmp_name"];
    $fileSize = $_FILES["pdfFile"]["size"];
    $fileType = mime_content_type($fileTmp);

    $fileExtension = strtolower(pathinfo($fileName, PATHINFO_EXTENSION));

    // Check file extension
    if($fileExtension != "pdf"){
        echo "Error: Only PDF files are allowed.";
        exit;
    }

    // Check MIME type
    if($fileType != "application/pdf"){
        echo "Error: File is not a valid PDF.";
        exit;
    }

    // Check file size
    if($fileSize > $maxSize){
        echo "Error: File size must be 5MB or less.";
        exit;
    }

    // Create uploads directory if not exists
    if(!is_dir($targetDir)){
        mkdir($targetDir, 0777, true);
    }

    $targetFile = $targetDir . basename($fileName);

    if(move_uploaded_file($fileTmp, $targetFile)){
        echo "Success: PDF uploaded successfully.";
    } else {
        echo "Error uploading file.";
    }
}

?>

