<?php
//// Initialize the session
//session_start();
//
//// Check if the user is logged in, if not then redirect him to login page
//if(!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true){
//    header("location: login.php");
//    exit;
//}
//?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Data</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body{ font: 14px sans-serif; text-align: center; }
    </style>
</head>
<body>
<h1>Data</h1>
<p>
    <a href="welcome.php" class="btn btn-danger ml-3">Back</a>
    <a href="search.php" class="btn btn-primary ml-3">Search</a>
</p>
</body>
</html>
